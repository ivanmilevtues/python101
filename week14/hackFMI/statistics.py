from pprint import pprint
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from prettytable import PrettyTable

from model import SkillList, PublicTeam, MentorList
from start import Base
# from getInfo import mentors, public_teams, skills

engine = create_engine("sqlite:///hackaton.db")
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()


def take_mentor_stats(name):
    mentor = session.query(MentorList).filter(MentorList.name == name)
    mentor_teams = ''
    for mentor_team in mentor:
        curr_team = session.query(PublicTeam)\
                           .filter(PublicTeam.id == mentor_team.teams)\
                           .first()
        id = mentor_team.id
        name = mentor_team.name
        pict = mentor_team.picture

        mentor_teams += (curr_team.name if curr_team else curr_team) + ', '
    mentor_teams = mentor_teams[:-2:]

    table = PrettyTable(['ID', 'Name', 'Picture', 'Teams'])
    table.add_row([id, name, pict, mentor_teams])

    print(table)


def take_team_stats(name):
    team = session.query(PublicTeam).filter(PublicTeam.name == name)
    tech_list = ''
    for team_skill in team:
        curr_skill = session.query(SkillList)\
                            .filter(SkillList.id ==
                                    team_skill.technologies_full)\
                            .first()
        id = team_skill.id
        name = team_skill.name
        repo = team_skill.repository
        need_members = 'Yes' if team_skill.need_more_members else 'No'
        tech_list += (curr_skill.name if curr_skill else '') + ', '
        room = team_skill.room
        place = team_skill.place

    table = PrettyTable(['ID', 'Name', 'Repository', 'Members needed',
                         'Techonologies used', 'room', 'place'])
    tech_list = tech_list[:-2:]
    table.add_row([id, name, repo, need_members, tech_list, room, place])

    print(table)


def take_all_mentors():
    all_mentors = session.query(MentorList).all()
    mentor_list = set()
    for mentor in all_mentors:
        mentor_list.add(mentor.name)
    return mentor_list


def take_all_teams():
    all_teams = session.query(PublicTeam).all()
    team_list = set()
    for team in all_teams:
        team_list.add(team.name)
    return team_list


def convert_time(hour, mins):
    if mins > 60:
        hour += mins / 60
        mins = mins % 60
    if mins < 10:
        return str(hour) + ':' + str(mins)
    else:
        return str(hour) + ':0' + str(mins)


def manage_hack(teams):
    mins = 0
    hour = 19
    agenta = []
    for team in teams:
        start = convert_time(hour, mins)
        mins += 15
        end = convert_time(hour, mins)
        agenta.append((team, start, end))
    return agenta


def main():
    # take_mentor_stats("Явор Стойчев")
    # take_team_stats("2b|!2b")
    teams = take_all_teams()
    pprint(manage_hack(teams))


if __name__ == '__main__':
    main()

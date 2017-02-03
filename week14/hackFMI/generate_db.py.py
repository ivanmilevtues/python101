from copy import deepcopy
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from model import SkillList, PublicTeam, MentorList
from start import Base
from getInfo import mentors, public_teams, skills

engine = create_engine("sqlite:///hackaton.db")
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()


def push_skills():
    for elem in skills.json():
        s = SkillList(name=elem['name'])
        session.add(s)
        session.commit()


def push_teams():
    for elem in public_teams.json():
        s = PublicTeam(name=elem['name'],
                       idea_description=elem['idea_description'],
                       repository=elem['repository'],
                       need_more_members=elem['need_more_members'],
                       members_needed_desc=elem['members_needed_desc'],
                       room=elem['room'],
                       place=elem['place'])

        for t in elem['technologies_full']:
            k = deepcopy(s)
            k.technologies_full = session.query(SkillList)\
                                         .filter(SkillList.name == t["name"])\
                                         .first().id
            session.add(k)
        if not s.technologies_full:
            session.add(s)
        session.commit()


def push_mentors():
    for elem in mentors.json():
        team_add = False
        m = MentorList(name=elem['name'],
                       description=elem['description'],
                       picture=elem['picture'])

        for team in elem['teams']:
            mentor_team = deepcopy(m)
            mentor_team.teams = session.query(PublicTeam)\
                                       .filter(PublicTeam.name ==
                                               team['name'])\
                                       .first()
            if mentor_team.teams:
                mentor_team.teams = mentor_team.teams.id

            session.add(mentor_team)
            team_add = True

        if not team_add:
            session.add(m)
        session.commit()


def main():
    push_skills()
    push_teams()
    push_mentors()


if __name__ == '__main__':
    main()

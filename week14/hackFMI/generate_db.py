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


def take_teams():
    team_cols = []
    for team in public_teams:
        new_team = PublicTeam(name=team['name'],
                              idea_description=team['idea_description'],
                              repository=team['repository'],
                              need_more_members=team['need_more_members'],
                              room=team['room'],
                              place=team['place'])
        if team['technologies_full']:
            for skill in team['technologies_full']:
                try:
                    curr_sk = session.query(SkillList)\
                                     .filter(SkillList.name == skill['name'])\
                                     .one()
                    new_team.skill.append(curr_sk)
                except Exception:
                    new_team.skill = [SkillList(name=skill['name'])]

        team_cols.append(new_team)


def main():
    teams = take_teams()
    session.add_all(teams)
    session.commit()

if __name__ == '__main__':
    main()

from sqlalchemy import Column, Integer, String, ForeignKey
from start import Base


class SkillList(Base):
    __tablename__ = 'skills'
    id = Column(Integer, primary_key=True)
    name = Column(String)


class PublicTeam(Base):
    __tablename__ = 'team'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    idea_description = Column(String)
    repository = Column(String)
    need_more_members = Column(Integer)
    members_needed_desc = Column(String)
    technologies_full = Column(Integer, ForeignKey(SkillList.id))
    room = Column(String)
    place = Column(String)


class MentorList(Base):
    __tablename__ = 'mentors'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    description = Column(String)
    picture = Column(String)
    teams = Column(Integer, ForeignKey(PublicTeam.id))

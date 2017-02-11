from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String, ForeignKey, Table
from start import Base


team_technologies = Table('team_skills', Base.metadata,
                          Column('team_id', ForeignKey('team.id'),
                          Column('skill_id', ForeignKey('skills.id'))))


team_mentors = Table('team_mentors', Base.metadata,
                     Column('team_id', ForeignKey('team.id'),
                     Column('mentor_id'), ForeignKey('mentors.id')))


class SkillList(Base):
    __tablename__ = 'skills'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    teams = relationship('PublicTeam', back_populates='team',
                         secondary=team_technologies)


class PublicTeam(Base):
    __tablename__ = 'team'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    idea_description = Column(String)
    repository = Column(String)
    need_more_members = Column(Integer)
    members_needed_desc = Column(String)
    technologies_full = relationship('PublicTeam',
                                     back_populates='team',
                                     secondary=team_mentors)
    mentors = relationship('MentorList',
                           back_populates='team',
                           secondary=team_mentors)
    room = Column(String)
    place = Column(String)


class MentorList(Base):
    __tablename__ = 'mentors'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    description = Column(String)
    picture = Column(String)
    teams = relationship('PublicTeam',
                         back_populates='team', secondary=team_mentors)

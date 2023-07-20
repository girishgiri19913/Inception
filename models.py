from sqlalchemy import Boolean, Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class Projects(Base):
    __tablename__ = "projects"

    id = Column(Integer, primary_key=True, index=True)
    project_name = Column(String, unique=True, index=True)
    project_test = Column(String, unique=True, index=True)
    activation_status = Column(Boolean, default=True)
   
    routes = relationship("Route", back_populates="project")
    signals = relationship("Signal", back_populates="project")
    tracks = relationship("Track", back_populates="project")

class Route(Base):
    __tablename__ = "route"

    id = Column(Integer, primary_key=True, index=True)
    category = Column(String)
    s_signal = Column(Integer)
    x_signal = Column(Integer)
    g_button = Column(String)
    route = Column(String)
    u_route = Column(String)
    number_input_yu = Column(Integer)
    option_input_yu = Column(String)
    number_input_y = Column(Integer)
    option_input_y = Column(String)
    number_input_yy = Column(Integer)
    option_input_yy = Column(String)
    number_input_g = Column(Integer)
    option_input_g = Column(String)
    project_id = Column(Integer, ForeignKey("projects.id"))

    project = relationship("Projects", back_populates="routes")

class Signal(Base):
    __tablename__ = "signal"

    id = Column(Integer, primary_key=True, index=True)
    point = Column(Integer)
    a_point = Column(String)
    a_Track_point = Column(String)
    b_point = Column(String)
    b_Track_point = Column(String)
    char = Column(String)
    project_id = Column(Integer, ForeignKey("projects.id"))

    project = relationship("Projects", back_populates="signals")

class Track(Base):
    __tablename__ = "track"

    id = Column(Integer, primary_key=True, index=True)
    tc = Column(String)
    name = Column(String)
    project_id = Column(Integer, ForeignKey("projects.id"))

    project = relationship("Projects", back_populates="tracks")
from sqlalchemy import Boolean, Column, Integer, String, ForeignKey
from database import Base
from sqlalchemy.orm import relationship

class Users(Base):
    __tablename__ = "users"
    
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(50), unique=True)
    password = Column(String(20), unique=True)
    subscribed = Column(Boolean, default=False)
    role = Column(String, default="regular")
    
    proyect = relationship("Proyects", back_populates="involved")
    
    
class Proyects(Base):
    __tablename__ = "proyects"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50))
    progress = Column(Integer, default=0)
    user_id = Column(Integer, ForeignKey('users.id'))
    
    involved = relationship("Users", back_populates="proyect")
    
from typing import List, Optional
from pydantic import BaseModel

class UserBase(BaseModel):
    username: str
    password: str
    subscribed: bool
    role: str
    
class ShowUser(BaseModel):
    username: str
    subscribed: bool
    role: str
    Proyect: List[ProyectBase] = []
    
    class Config():
        orm_mode = True
    
class ProyectBase(BaseModel):
    
    name: str
    progress: int
    
    class Config():
        orm_mode = True
    
class ShowProyect(BaseModel):
    name: str
    progress: int
    involved: ShowUser
    
    class Config():
        orm_mode = True
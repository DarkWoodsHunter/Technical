from typing import List, Optional
from pydantic import BaseModel

class UserBase(BaseModel):
    username: str
    password: str
    subscribed: bool
    role: str
    

    
class ProyectBase(BaseModel):
    
    name: str
    progress: int
    
    class Config():
        orm_mode = True
        
class smalluser(BaseModel):
    username: str
    subcribed: int
    role:str
    
    class Config():
        orm_mode = True

class ShowUser(BaseModel):
    username: str
    subscribed: bool
    role: str
    proyect: List[ProyectBase] = []
    
    class Config():
        orm_mode = True   
         
class ShowProyect(BaseModel):
    name: str
    progress: int
    involved: ShowUser
    
    class Config():
        orm_mode = True
        
class Login(BaseModel):
    username: str
    password: str
    
class Token(BaseModel):
    access_toekn: str
    token_type: str
    
class TokenData(BaseModel):
    username: Optional[str] = None
from sqlalchemy.orm import Session
from fastapi import HTTPException, status
import models, schemas
from Hashing import Hash



#Create a User
def create_user(resquest: schemas.UserBase, db:Session):
    db_user = models.Users(username=resquest.username, password=Hash.brcrypt(resquest.password), subscribed=resquest.subscribed, role=resquest.role)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return "User added to DB"
    
#Get a user by id
def read_user(user_id: int, db: Session):
    user = db.query(models.Users).filter(models.Users.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

#Update a User
def update(id: int, request: schemas.UserBase, db:Session):
    
    edit_user = db.query(models.Users).filter(models.Users.id == id)
    
    if not edit_user.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"User with the id {id} not found")
    
    edit_user.update(request)
    db.commit()
    return "User Updated"

################################################################################

def get_all(db:Session):
    all_proyects = db.query(models.Proyects).all()
    return all_proyects

#Create a Proyect
def create(request: schemas.ProyectBase, db:Session):
    new_Proyect = models.Proyects(name=request.name, progress=request.progress, user_id=1)
    db.add(new_Proyect)
    db.commit()
    db.refresh(new_Proyect)
    return new_Proyect
    
#Get a single Proyect
def read_Proyect(proyect_id: int, db: Session):
    proyect = db.query(models.Proyects).filter(models.Proyects.id == proyect_id).first()
    if proyect is None:
        raise HTTPException(status_code=404, detail="Proyect not found")
    return proyect

#Delete a single Proyect
def Delete_Proyect(proyect_id: int, db: Session):
    proyect = db.query(models.Proyects).filter(models.Proyects.id == proyect_id)
    if not proyect.first():
        raise HTTPException(status_code=404, detail="Proyect not found")
    proyect.delete(synchronize_session=False)
    db.commit()
    return 'Proyect Deleted'
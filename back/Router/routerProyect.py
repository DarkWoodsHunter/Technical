from fastapi import APIRouter, Depends, status
import oauth2
from sqlalchemy.orm import Session
from ModelsSchemas import schemas
from Controllers import controllers
from Database import database

router = APIRouter(
    prefix="/Proyect",
    tags=["Proyects"]
)

get_db = database.get_db

#Create a Proyect
@router.post("/", status_code=status.HTTP_201_CREATED)
def create_proyect(request: schemas.ProyectBase, db: Session = Depends(get_db), current_user: schemas.UserBase = Depends(oauth2.get_current_user)):
    return controllers.create(request, db)
    
#Get a single Proyect
@router.get("/{proyect_id}", status_code=status.HTTP_200_OK, response_model=schemas.ShowProyect)
def read_Proyect(proyect_id: int, db: Session = Depends(get_db)):
    return controllers.read_Proyect(proyect_id, db)

#Delete a single Proyect
@router.delete("/{proyect_id}", status_code=status.HTTP_204_NO_CONTENT)
def read_Proyect(proyect_id: int, db: Session = Depends(get_db),  current_user: schemas.UserBase = Depends(oauth2.get_current_user)):
    return controllers.Delete_Proyect(proyect_id, db)
from fastapi import APIRouter, Depends, status
import database, schemas, controllers
from sqlalchemy.orm import Session

router = APIRouter(
    prefix="/user",
    tags=["users"]
)

get_db = database.get_db

@router.post("/", status_code=status.HTTP_201_CREATED)
def create_user(request: schemas.UserBase, db: Session = Depends(get_db)):
    return controllers.create_user(request, db)

@router.get('/{id}', response_model=schemas.UserBase)
def get_user(id:int, db: Session = Depends(get_db)):
    return controllers.read_user(id, db)

@router.put('/{id}', status_code=status.HTTP_202_ACCEPTED)
def update_user(id: int, request: schemas.UserBase, db: Session = Depends(get_db)):
    return controllers.update(id, request, db)
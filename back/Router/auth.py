from fastapi import APIRouter, Depends, status, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
import JWTtoken
from sqlalchemy.orm import Session
from Hashing import Hash
from ModelsSchemas import models
from Database import database

router = APIRouter(tags=["Authentication"])

@router.post('/login')
def login(request: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(database.get_db)):
    user = db.query(models.Users).filter(models.Users.username == request.username).first()
    
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Invalid Credentials")
    
    if not Hash.veryfy(user.password, request.password):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Incorrect Password")
    
    access_token = JWTtoken.create_access_token(data={"sub": user.username})
    
    return {"access_token": access_token, "token_type": "bearer"}
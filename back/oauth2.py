from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
import JWTtoken

OAuth2_scheme = OAuth2PasswordBearer(tokenUrl="login")

def get_current_user(data: str=Depends(OAuth2_scheme)):
    credentials_exections = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    
    return JWTtoken.verify_token(data, credentials_exections)
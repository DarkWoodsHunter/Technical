from passlib.context import CryptContext

pwd = CryptContext(schemes=["bcrypt"], deprecated="auto")

class Hash():
    def brcrypt(password: str):
        return pwd.hash(password)
    
    def veryfy(hashed_password, plain_password):
        return pwd.verify(plain_password, hashed_password)
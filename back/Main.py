from fastapi import FastAPI
import models
from database import engine

from database import engine
from Router import routerUser, routerProyect



app = FastAPI()

models.Base.metadata.create_all(engine)

app.include_router(routerUser.router)
app.include_router(routerProyect.router)

'''
################################################################################
models.Base.metadata.create_all(bind=engine)

class UserBase(BaseModel):
    username: str
    password: str
    subscribed: bool
    role: str
    
class ProyectBase(BaseModel):
    
    name: str
    progress: int
    
def get_bd():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
        
db_dependecy = Annotated[Session, Depends(get_bd)]

################################################################################
#Create a User
@app.post("/user/", status_code=status.HTTP_201_CREATED)
async def create_user(user: UserBase, db:db_dependecy):
    db_user = models.Users(username=user.username, password=user.password, subscribed=user.subscribed, role=user.role)
    db.add(db_user)
    db.commit()
    return "User added to DB"
    
#Get a user by id
@app.get("/user/{id}", status_code=status.HTTP_200_OK)
async def read_user(user_id: int, db: db_dependecy):
    user = db.query(models.Users).filter(models.Users.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@app.put("/user/{id}", status_code=status.HTTP_202_ACCEPTED)
async def update_user(user_id: int, user:UserBase, db:db_dependecy):
    db.query(models.Users).filter(models.Users.id == user_id).update(UserBase)
    db.commit()
    return "updated"
################################################################################
#Create a Proyect
@app.post("/proyect/", status_code=status.HTTP_201_CREATED)
async def create_proyect(proyect: ProyectBase, db: db_dependecy):
    db_proyect = models.Proyects(**proyect.model_dump())
    db.add(db_proyect)
    db.commit()
    
#Get a single Proyect
@app.get("/proyects/{proyect_id}", status_code=status.HTTP_200_OK)
async def read_Proyect(proyect_id: int, db: db_dependecy):
    proyect = db.query(models.Proyects).filter(models.Proyects.id == proyect_id).first()
    if proyect is None:
        raise HTTPException(status_code=404, detail="Proyect not found")
    return proyect

#Delete a single Proyect
@app.delete("/proyects/{proyect_id}", status_code=status.HTTP_200_OK)
async def read_Proyect(proyect_id: int, db: db_dependecy):
    proyect = db.query(models.Proyects).filter(models.Proyects.id == proyect_id)
    if not proyect.first():
        raise HTTPException(status_code=404, detail="Proyect not found")
    proyect.delete(synchronize_session=False)
    db.commit()
    return 'Proyect Deleted'

'''
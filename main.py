from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

import crud
import models
import schemas
from database import SessionLocal, engine


models.Base.metadata.create_all(bind=engine)

#initialize the app
app = FastAPI()

#Get the db connection
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()




#EXAMPLE CREATE TASK REQUEST
#@app.post("/task/create", response_model=schemas.Task)
#def create_task(name: str, desc: str, db: Session = Depends(get_db)):
#    db_task = crud.get_task_by_name(db, name=name)
#    if db_task:
#        raise HTTPException(status_code=400, detail="Task already Exists")
#    return crud.create_task(db=db, name=name,desc=desc)


#EXAMPLE GET TASKS REQUEST
#@app.get("/tasks", response_model=List[schemas.Task])
#def read_tasks(db: Session = Depends(get_db)):
#    tasks = crud.get_tasks(db)
#    return tasks





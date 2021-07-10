from sqlalchemy.orm import Session
import datetime
from datetime import date,timedelta

from sqlalchemy.util.langhelpers import symbol
import models, schemas

#EXAMPLE GET
#def get_tasks(db: Session):
#    return db.query(models.Task).all()

#EXAMPLE CREATE
#def create_task(db: Session, name: str, desc: str):
#    db_task = models.Task(Name = name, Description = desc)
#    db.add(db_task)
#    db.commit()
#    db.refresh(db_task)
#    return db_task

#EXAMPLE GET BY FIELD
#def get_task_by_name(db: Session, name:str):
#    return db.query(models.Task).filter(models.Task.Name == name).first()





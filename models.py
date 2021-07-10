import datetime
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Float, DateTime, VARCHAR, VARBINARY
from sqlalchemy.orm import relationship

from database import Base

#EXAMPLE TASK DB TABLE MODEL
#class Task(Base):
#    __tablename__ = "task"
#    id = Column(Integer, primary_key=True, index=True)
#    Description = Column(String, unique=True, index=True)
#    Name = Column(String)

     #THIS IS HOW TO DEFINE A RELATIONSHIP
#    dailydata = relationship("DailyData", back_populates="task")
     #ON DAILYDATA THIS MUST ALSO BE PRESENT BUT AS
     #task = relationship("Task", back_populates="dailydata")
     #IN DAILYDATA THE TASK_ID FIELD WOULD BE POPULATED BY THIS RELATIONSHIP AS SO
     #Task_ID = Column(Integer, ForeignKey("task.id"))

    


    

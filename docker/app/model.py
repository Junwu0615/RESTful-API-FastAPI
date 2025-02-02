# -*- coding: utf-8 -*-

from sqlalchemy import Column, Integer, String, DateTime
from database import Base

class Job(Base):
    __tablename__ = "job"
    job_id = Column(String, primary_key=True, index=True)
    reported_date = Column(DateTime, index=True)
    company = Column(String, index=True)
    title = Column(String, index=True)
    location = Column(String, index=True)
    pay = Column(Integer, index=True)
    pay_unit = Column(String, index=True)
# -*- coding: utf-8 -*-

from datetime import datetime
from sqlalchemy.orm import Session
from model import Job

# 1️⃣ 建立工作
def create_user(db: Session, job_id: str, reported_date: datetime,  company: str, title: str,
                location: str, pay: int, pay_unit: str):
    db_user = Job(job_id=job_id, reported_date=reported_date, company=company,
                  title=title, location=location, pay=pay, pay_unit=pay_unit)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

# 2️⃣ 查詢所有工作
def get_users(db: Session):
    return db.query(Job).all()

# 3️⃣ 查詢特定工作
def get_user(db: Session, job_id: int):
    return db.query(Job).filter(Job.job_id == job_id).first()

# 4️⃣ 更新工作
def update_user(db: Session, job_id: str, reported_date: datetime,  company: str, title: str,
                location: str, pay: int, pay_unit: str):
    data = db.query(Job).filter(Job.job_id == job_id).first()
    if data:
        data.reported_date = reported_date
        data.company = company
        data.title = title
        data.location = location
        data.pay = pay
        data.pay_unit = pay_unit
        db.commit()
        db.refresh(data)
        return data
    return None

# 5️⃣ 刪除工作
def delete_user(db: Session, job_id: str):
    user = db.query(Job).filter(Job.job_id == job_id).first()
    if user:
        db.delete(user)
        db.commit()
        return True
    else:
        return False
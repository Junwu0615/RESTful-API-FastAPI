# -*- coding: utf-8 -*-

import os
from datetime import datetime
from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session

from database import SessionLocal, save_json_to_db
from crud import create_user, get_users, get_user, update_user, delete_user

app = FastAPI()

# 啟動時建立資料庫
@app.on_event("startup")
def startup():
    path = '../sqlite_data'
    if not os.path.exists(path + '/fast_api.db'):
        save_json_to_db(path + '/hr_vacancies_100.json')

# 獲取資料庫
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# 初始介面
@app.get("/")
def root():
    return {"message": "Hello World"}

# 1️⃣ 創建工作
@app.post("/jobs/")
def create_user_api(job_id: str, reported_date: datetime,  company: str, title: str, location: str, pay: int, pay_unit: str,
                    db: Session=Depends(get_db)):
    return create_user(db, job_id, reported_date,  company, title, location, pay, pay_unit)

# 2️⃣ 取得所有工作
@app.get("/jobs/")
def read_users_api(db: Session=Depends(get_db)):
    return get_users(db)

# 3️⃣ 取得特定工作
@app.get("/jobs/{job_id}")
def read_user_api(job_id: str, db: Session=Depends(get_db)):
    user = get_user(db, job_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

# 4️⃣ 更新工作
@app.put("/jobs/{job_id}")
def update_user_api(job_id: str, reported_date: datetime,  company: str, title: str, location: str, pay: int, pay_unit: str,
                    db: Session=Depends(get_db)):
    updated_user = update_user(db, job_id, reported_date,  company, title, location, pay, pay_unit)
    if not updated_user:
        raise HTTPException(status_code=404, detail="User not found")
    return updated_user

# 5️⃣ 刪除工作
@app.delete("/jobs/{job_id}")
def delete_user_api(job_id: str, db: Session=Depends(get_db)):
    if not delete_user(db, job_id):
        raise HTTPException(status_code=404, detail="User not found")
    else:
        return {"message": "User deleted successfully"}
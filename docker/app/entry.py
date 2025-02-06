# -*- coding: utf-8 -*-

from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session

from database import SessionLocal, init_db
from model import Base
from crud import create_user, get_users, get_user, update_user, delete_user

# 初始化 FastAPI 應用
app = FastAPI()

# 啟動時建立資料庫
@app.on_event("startup")
def startup():
    init_db()

# 依賴注入：獲取資料庫 session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# 1️⃣ 創建使用者
@app.post("/users/")
def create_user_api(name: str, email: str, db: Session = Depends(get_db)):
    return create_user(db, name, email)

# 2️⃣ 取得所有使用者
@app.get("/users/")
def read_users_api(db: Session = Depends(get_db)):
    return get_users(db)

# 3️⃣ 取得特定使用者
@app.get("/users/{user_id}")
def read_user_api(user_id: int, db: Session = Depends(get_db)):
    user = get_user(db, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

# 4️⃣ 更新使用者
@app.put("/users/{user_id}")
def update_user_api(user_id: int, name: str, email: str, db: Session = Depends(get_db)):
    updated_user = update_user(db, user_id, name, email)
    if not updated_user:
        raise HTTPException(status_code=404, detail="User not found")
    return updated_user

# 5️⃣ 刪除使用者
@app.delete("/users/{user_id}")
def delete_user_api(user_id: int, db: Session = Depends(get_db)):
    if not delete_user(db, user_id):
        raise HTTPException(status_code=404, detail="User not found")
    else:
        return {"message": "User deleted successfully"}
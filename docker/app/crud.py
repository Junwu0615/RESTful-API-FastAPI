# -*- coding: utf-8 -*-

from sqlalchemy.orm import Session
from model import User

# 1️⃣ 建立使用者 (Create)
def create_user(db: Session, name: str, email: str):
    db_user = User(name=name, email=email)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

# 2️⃣ 查詢所有使用者 (Read)
def get_users(db: Session):
    return db.query(User).all()

# 3️⃣ 查詢特定使用者
def get_user(db: Session, user_id: int):
    return db.query(User).filter(User.id == user_id).first()

# 4️⃣ 更新使用者 (Update)
def update_user(db: Session, user_id: int, name: str, email: str):
    user = db.query(User).filter(User.id == user_id).first()
    if user:
        user.name = name
        user.email = email
        db.commit()
        db.refresh(user)
        return user
    return None

# 5️⃣ 刪除使用者 (Delete)
def delete_user(db: Session, user_id: int):
    user = db.query(User).filter(User.id == user_id).first()
    if user:
        db.delete(user)
        db.commit()
        return True
    else:
        return False
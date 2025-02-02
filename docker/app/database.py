# -*- coding: utf-8 -*-

import os, json
from datetime import datetime
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

DATABASE_PATH = os.getenv("DATABASE_PATH", "sqlite:///../sqlite_data/fast_api.db")
engine = create_engine(DATABASE_PATH, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

def init_db():
    Base.metadata.create_all(bind=engine)

def save_json_to_db(file_path: str):
    from model import Job
    loader = [json.loads(i) for i in open(file_path, "r", encoding="utf-8")][0]

    init_db()
    db = SessionLocal()
    try:
        for k,v in loader.items():
            data = Job(
                job_id=k,
                reported_date=datetime.strptime(v["刊登時間"], '%Y-%m-%d'),
                company=v["公司"],
                title=v["職缺"],
                location=str(v["部門"]),
                pay=0 if v["薪水"] is None else int(v["薪水"]),
                pay_unit=v["薪水_單位"],
            )
            db.add(data)

        db.commit()
        print("✅ 數據成功存入資料庫 !")

    except Exception as e:
        db.rollback()
        print(f"⚠️ 發生錯誤: {e}")

    finally:
        db.close()
        print("✅ 關閉連線 !")
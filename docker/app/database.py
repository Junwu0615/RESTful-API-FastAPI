# -*- coding: utf-8 -*-

import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base


# # 連接到本機的 SQLite（實際上是 Docker 內部的檔案）
# conn = sqlite3.connect("sqlite_data/test.db")
# cursor = conn.cursor()
#
# # 查詢所有使用者
# cursor.execute("SELECT * FROM users")
# users = cursor.fetchall()
#
# print(users)
#
# conn.close()

# 取得環境變數中的 SQLite 資料庫路徑
DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///../sqlite_data/test.db")

# 設定資料庫連線
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# 建立資料表
def init_db():
    Base.metadata.create_all(bind=engine)
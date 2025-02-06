<a href='https://github.com/Junwu0615/RESTful-API-FastAPI'><img alt='GitHub Views' src='https://views.whatilearened.today/views/github/Junwu0615/RESTful-API-FastAPI.svg'> 
<a href='https://github.com/Junwu0615/RESTful-API-FastAPI'><img alt='GitHub Clones' src='https://img.shields.io/badge/dynamic/json?color=success&label=Clone&query=count_total&url=https://gist.githubusercontent.com/Junwu0615/732741678dbe23fa2369b6a0c13846fa/raw/RESTful-API-FastAPI_clone.json&logo=github'> <br>
[![](https://img.shields.io/badge/Project-RESTful_API-blue.svg?style=plastic)](https://github.com/Junwu0615/RESTful-API-FastAPI)
[![](https://img.shields.io/badge/Deploy-Docker_27.3.1-blue.svg?style=plastic)](https://www.docker.com/) 
[![](https://img.shields.io/badge/Language-Python_3.12.0-blue.svg?style=plastic)](https://www.python.org/) <br>
[![](https://img.shields.io/badge/Database-SQLite-yellow.svg?style=plastic)](https://www.sqlite.org/)
[![](https://img.shields.io/badge/Package-FastAPI_0.87.0-yellow.svg?style=plastic)](https://pypi.org/project/fastapi/)
[![](https://img.shields.io/badge/Package-Uvicorn_0.34.0-yellow.svg?style=plastic)](https://pypi.org/project/uvicorn/)
[![](https://img.shields.io/badge/Package-SQL_Alchemy_2.0.37-yellow.svg?style=plastic)](https://pypi.org/project/sqlalchemy/) <br>

<br>

# **** 尚在開發中 ****

<br>

## *A.　Showcase Results*
### *任務 : 人力職缺的 API 串流文件*

### *存儲數據 : SQLite*
- #### SQLite 無需獨立伺服器的資料庫 ; 而獨立伺服器的有 PostgreSQL, SQL Server, MySQL...etc.
- #### 它會將數據存儲在一個本地檔案 (.db)

### *專案功能 : CRUD*
- ### *[ C ] reate*
- ### *[ R ] ead*
- ### *[ U ] pdate*
- ### *[ D ] elete*


## *B.　How To Use*
### *Directory Structure Diagram*
```commandline
RESTful-API-FastAPI/docker
  ├── app
  │   ├── crud.py
  │   ├── database.py
  │   ├── entry.py
  │   ├── model.py
  │   └── requirements.txt
  │
  ├── sqlite_data
  │
  └── script
      ├── docker-compose.yaml
      └── Dockerfile.fastapi
```

### *STEP.1　Clone*
```bash
git clone https://github.com/Junwu0615/RESTful-API-FastAPI.git
```

### *STEP.2　Enter path*
```bash
cd docker/app
```

### *STEP.3　Requirements*
```bash
pip install -r requirements.txt
```

### *STEP.4　Run Service*
```bash
uvicorn entry:app --reload --port 8000
```

### *STEP.5　Open Swagger API*
```text
http://127.0.0.1:8000/docs
```

## *C.　Dockerization*
### *STEP.1　Enter `docker` path*
```bash
cd docker
```

### *STEP.2　Create `sqlite_data` Folder*
```bash
md sqlite_data
```

### *STEP.3　基於 Dockerfile build images*
```bash
docker compose --file script/docker-compose.yaml build --no-cache
```

### *STEP.4　背景執行服務*
```bash
docker compose --file script/docker-compose.yaml up -d
```

### *STEP.5　檢視服務啟動狀態*
```bash
docker ps -a
```

## *D.　Reference*
-  ### [[Day7] 簡單搞懂Restful API Python 實作範例](https://ithelp.ithome.com.tw/m/articles/10295371)
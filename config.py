import os

BASE_URL = "http://31.178.216.240:8855/"
BASE_API_URL = f"{BASE_URL}api/v1"


class DBInfo:
    HOST = "mongodb://31.178.216.240:8866/"
    DB_NAME = "main_db"
    USER = os.getenv("DB_USER") or "test_user"
    PASS = os.getenv("DB_PASS") or "test_pass"

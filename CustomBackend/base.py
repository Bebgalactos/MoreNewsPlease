# mysql_backend_custom/base.py
from typing import Any
from django.db.backends.mysql.base import DatabaseWrapper as MySQLDatabaseWrapper

class DatabaseWrapper(MySQLDatabaseWrapper):
    
    def check_database_version_supported(self) -> None:
        pass

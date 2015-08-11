#!/usr/bin/env python
# coding: utf-8

import json
import backup_config

import sys
sys.path.append("..")
from config import AppConfig
from db_connect.MySQL_lightweight import MySQL_lightweight

class FileBackup(object):
    _file_backup_db = 'DbBak'
    _db = None
    
    def __init__(self):
        dbconfig = {'host':backup_config.BACKUP_INFO_DB_IP, 
                    'port':backup_config.BACKUP_INFO_DB_PORT, 
                    'user':AppConfig.MYSQL_ADMIN_USR, 
                    'passwd':AppConfig.MYSQL_ADMIN_PSWORD, 
                    'db':self._file_backup_db, 
                    'charset':'utf8'}
        self._db = MySQL_lightweight(dbconfig)

    def yesterday_file_backup(self):
        sql = "SELECT name,file_name,file_size,bak_keep_host FROM file_backup WHERE TIME >= DATE(now()) - INTERVAL 1 DAY AND TIME < DATE(now()) order by name"
        self._db.query(sql);
        result = self._db.fetchAllRows();
        return result

if __name__ == '__main__':
    test = FileBackup()
    result = test.yesterday_file_backup()
    print result


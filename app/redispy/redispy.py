#!/usr/bin/env python
# coding: utf-8

import json
import redispy_config
import time
import sys
import redis
sys.path.append("..")
from config import AppConfig

from cmdb.server import ServerList
from cmdb.instance import InstList
from cmdb.backup import BackupList

from db_connect.MySQL_lightweight import MySQL_lightweight

def is_valid_date(str_in):
    '''Test if it is a valid string of date.'''
    try:
        time.strptime(str_in, "%Y-%m-%d")
        return True
    except:
        return False

class DBAPortalRedis(object):
    _redis = None
    
    def __init__(self):
        self._redis = redis.StrictRedis(host=redispy_config.REDIS_IP, port=redispy_config.REDIS_PORT, encoding='utf-8')

    def init_dba_portal_redis(self):
        self._redis.flushall()

        print 'add server data into redis...'        
        server_list = ServerList()
        server_all = server_list.list_all()
        server_all = json.dumps(server_all,ensure_ascii=False)
        self._redis.set('server_all', server_all)
        time.sleep(3)
        server_available = server_list.list_available()
        server_available = json.dumps(server_available,ensure_ascii=False)
        self._redis.set('server_available', server_available)
        time.sleep(3)
        server_total_count = server_list.get_total_count()
        server_total_count = json.dumps(server_total_count,ensure_ascii=False)
        self._redis.set('server_total_count', server_total_count)
        time.sleep(3)

        print 'add instance data into redis...'        
        instance_list = InstList()
        instance_total_count = instance_list.get_total_count()
        instance_total_count = json.dumps(instance_total_count,ensure_ascii=False)
        self._redis.set('instance_total_count', instance_total_count)
        time.sleep(3)

        print 'add backup data into redis...'
        backup_list = BackupList()
        backup_mha = backup_list.mha()
        backup_mha = json.dumps(backup_mha,ensure_ascii=False)
        self._redis.set('backup_mha', backup_mha)
        time.sleep(3)
        backup_single_instance = backup_list.single_instance()
        backup_single_instance = json.dumps(backup_single_instance,ensure_ascii=False)
        self._redis.set('backup_single_instance', backup_single_instance)
        time.sleep(3)
        backup_configure = backup_list.configure()
        backup_configure = json.dumps(backup_configure,ensure_ascii=False)
        self._redis.set('backup_configure', backup_configure)
        time.sleep(3)
        backup_email_backup_report = backup_list.email_backup_report()
        backup_email_backup_report = json.dumps(backup_email_backup_report,ensure_ascii=False)
        self._redis.set('backup_email_backup_report', backup_email_backup_report)
        time.sleep(3)

        return True

    def get_backup_mha(self):
        backup_mha = json.loads(self._redis.get('backup_mha'))
        return backup_mha

    def get_backup_single_instance(self):
        backup_single_instance = json.loads(self._redis.get('backup_single_instance'))
        return backup_single_instance

    def get_backup_configure(self):
        backup_configure = json.loads(self._redis.get('backup_configure'))
        return backup_configure

    def get_backup_email_backup_report(self):
        backup_email_backup_report = json.loads(self._redis.get('backup_email_backup_report'))
        return backup_email_backup_report



    def get_server_all(self):
        server_all = json.loads(self._redis.get('server_all'))
        return server_all

    def get_server_available(self):
        server_available = json.loads(self._redis.get('server_available'))
        return server_available

    def get_server_total_count(self):
        server_total_count = json.loads(self._redis.get('server_total_count'))
        return server_total_count


    def get_instance_total_count(self):
        instance_total_count = json.loads(self._redis.get('instance_total_count'))
        return instance_total_count



if __name__ == '__main__':
    test = FileBackup()
    result = test.get_file_backup_info()
    print result


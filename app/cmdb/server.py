#-*- coding: utf-8 -*-
__author__ = 'cenalulu'
import urllib2
import urllib
import json,requests
from cmdb_api_base import CmdbApiBase

class ServerList(CmdbApiBase):

    def list_all(self, data=None):
        #result = self.__call_serverlist_interface__('api/v0.1/products/DBA/devices', json_obj=data)
        if data:
            data['count'] = 1000
        else:
            data = {'count':1000}
        result = requests.get('http://api.cmdb.dp/api/v0.1/products/DBA/devices',data=data,timeout=20).json()
        if 'sn' in data and len(result['devices']) ==0:
            data['server_sn'] = data.pop('sn')
            #result = requests.get('http://api.cmdb.dp/api/v0.1/products/DBA/devices',data=data,timeout=3).json()
        for dev in result['devices']:
            dev['private_ip'] = dev['private_ip'][0]
            if 'server_sn' in dev:
                dev['sn'] = dev['server_sn']
        return result['devices']

    def list_supported_type(self):
        result = self.__call_interface__('CMDB', 'gettype')
        type_list = list()
        type_list.append('')
        if result:
            for entry in result:
                type_list.append(entry['status'])
        else:
            return False
        return type_list

    def list_supported_dba(self):
        query_obj = {"role": "DBA", "status": "在职"}
        result = self.__call_interface__('USER', 'getuser', json_obj=query_obj)
        dba_list = list()
        dba_list.append('')
        if result:
            for user in result:
                dba_list.append(user['realname'])
        else:
            return False
        return dba_list

    def list_available(self, data=None):
        result = self.__call_interface__('CMDB', 'getuseableserver', json_obj=data)
        return result

    def list_selected_server(self, data=None, api=None):
	if (api == 'getuseableserver'):
	     item_name = 'server_id'
	else:
	     item_name = 'sn' 
        #result = self.__call_interface__('CMDB', 'getuseableserver', json_obj=data)
	datastr = data.split(',')
	apply_list = list()
	for serverid in datastr:
	    request_value = self.__call_interface__('CMDB', api + '?data={"' + item_name + '":"' + serverid + '"}')
            if request_value:
                apply_list.append(request_value[0])
        return apply_list

    def getApplyresult(self, data=None):
        result = self.__call_interface__('CMDB', 'init_system', json_obj=data)
        return result

    def online_by_id(self, server_id):
        data = {
            "server_id": server_id,
            "server_status": "在线"
        }
        result = self.__call_interface__('CMDB', 'serverstatechange/0', json_obj=data)
        return result

    def offline_by_id(self, server_id):
        data = {'ip':server_id,'cause':''}
        result = self.__call_interface__('CMDB', 'offline_server', json_obj=data)
        return result

    def delete_by_id(self, server_id):
        data = {"server_id": server_id}
        result = self.__call_interface__('CMDB', 'deleteserver', json_obj=data)
        return result

    def machine_info_by_id(self, server_id):
        data = {"server_id": server_id}
        result = self.__call_interface__('CMDB', 'getengineinfo', json_obj=data)
        return result

    def info_by_id(self, server_id):
        data = {"server_id": server_id}
        result = self.__call_interface__('CMDB', 'getserverinfo', json_obj=data)
        return result

    def get_ip_by_id(self, server_id=None):
        data = {"server_id": server_id}
        result = self.__call_interface__('CMDB', 'getserverinfo', json_obj=data)
        return result[0]['server_ip']

    def init_system_with_mirror(self, info):
        result = self.__call_interface__('CMDB', 'init_system', json_obj=info)
        return result

    def save_server_info(self, info):
        result = self.__call_interface__('CMDB', 'serverstatechange/0', json_obj=info)
        return result

    def get_total_count(self):
        result = self.__call_interface__('CMDB', 'getservercount')
        return result

    def add_server(self, info):
        result = self.__call_interface__('CMDB', 'addserver', json_obj=info)
        return result

    def list_supported_bu(self):
        result = requests.get('http://api.cmdb.dp/api/v0.1/bu').json()
        bu_list = list()
        bu_list.append('')
        if result:
            for bu in result['bu']:
                bu_list.append(bu['bu_name'])
            return zip(bu_list, bu_list)
        else:
            return False

    def list_supported_product(self, bu):
        result = []
        url = "http://api.cmdb.dp/api/v0.1/bu/"+bu+"/products"
        rep = requests.get(url).json()
        for re in rep['products']:
            result +=[re['product_name']]
        return json.dumps(result)

    def list_supported_env(self):
        result = self.__call_interface__('CMDB', 'getenv')
        env_list = list()
        env_list.append('')
        if result:
            for env in result:
                env_list.append(env)
            return zip(env_list,env_list)
        else:
            return False

    def list_supported_dba(self):
        query_obj = {"role": "DBA", "status": "在职"}
        result = self.__call_interface__('USER', 'getuser', json_obj=query_obj)
        dba_list = list()
        dba_list.append('')
        if result:
            for user in result:
                dba_list.append(user['realname'])
            return zip(dba_list, dba_list)
        else:
            return False

    def list_user_privilege(self,real_name=None,domain_name=None):
        query_obj = {"realname": real_name, "domain_name": domain_name}
        result = self.__call_interface__('USER', 'getuser', json_obj=query_obj)
        if result:
            if result[0]['priv'] == 1:
                return 1
        return 0

    def list_supported_use_status(self):
        result = self.__call_interface__('CMDB', 'getusestatus')
        status_list = list()
        status_list.append('')
        if result:
            for status in result:
                status_list.append(status['status'])
            return zip(status_list, status_list)
        else:
            return False

    def list_supported_status(self):
        result = self.__call_interface__('CMDB', 'getserverstatus')
        status_list = list()
        status_list.append('')
        if result:
            for status in result:
                status_list.append(status['status'])
            return zip(status_list, status_list)
        else:
            return False

    def list_supported_ram_size(self):
        #result = self.__call_interface__('CMDB', 'getmeminfo')
	result = ["16GB","24GB","32GB","48GB","64GB","96GB"]
        env_list = list()
        env_list.append('')
        if result:
            for env in result:
                env_list.append(env)
            return zip(env_list,env_list)
        else:
            return False

    def list_supported_cpu(self):
        #result = self.__call_interface__('CMDB', 'getcpuinfo')
        result = ["12","16","20","24","32","40"]
        env_list = list()
        env_list.append('')
        if result:
            for env in result:
                env_list.append(env)
            return zip(env_list,env_list)
        else:
            return False

    def list_supported_idc(self):
        #result = self.__call_interface__('CMDB', 'getdatacenter')
        result = ["南汇","宝山"]
        env_list = list()
        env_list.append('')
        if result:
            for env in result:
                env_list.append(env)
            return zip(env_list,env_list)
        else:
            return False

    def list_supported_mysql_version(self):
        #result = self.__call_interface__('CMDB', 'getdatacenter')
        result = ["Percona-5.1.58-OS5-x86_64","Percona-5.1.58-OS6-x86_64","Percona-5.6.19-OS6-x86_64","Percona-5.6.24-OS6-x86_64"]
        env_list = list()
        env_list.append('')
        if result:
            for env in result:
                env_list.append(env)
            return zip(env_list,env_list)
        else:
            return False

    def list_supported_mongodb_version(self):
        #result = self.__call_interface__('CMDB', 'getdatacenter')
        result = ["2.0.7","2.0.9","2.2.4","2.4.4","2.6.9","3.0.1","3.0.4"]
        env_list = list()
        env_list.append('')
        if result:
            for env in result:
                env_list.append(env)
            return zip(env_list,env_list)
        else:
            return False

    def list_supported_memcache_version(self):
        #result = self.__call_interface__('CMDB', 'getdatacenter')
        result = ["Memcached-1.4.15-OS6-x86_64","Memcached-1.4.15-OS5-x86_64"]
        env_list = list()
        env_list.append('')
        if result:
            for env in result:
                env_list.append(env)
            return zip(env_list,env_list)
        else:
            return False

    def list_supported_biz(self):
        #result = self.__call_interface__('CMDB', 'getdatacenter')
        result = ["交易前台","大搜索和基础体验部","平台产品部","平台技术中心","企业系统","预定外卖与企业发展","推广结婚亲子家装","未知BU","商家平台","交易后台"]
        env_list = list()
        env_list.append('')
        if result:
            for env in result:
                env_list.append(env)
            return zip(env_list,env_list)
        else:
            return False

if __name__ == '__main__':
    test_server = ServerList()
    print test_server.list_selected_server(*data)
    print 'a'

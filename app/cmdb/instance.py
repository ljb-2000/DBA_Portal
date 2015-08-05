#-*- coding: utf-8 -*-
from cmdb_api_base import CmdbApiBase


class InstList(CmdbApiBase):

    def list_all(self, data=None):
        result = self.__call_interface__('CMDB', 'getinstanceinfo', json_obj=data)
        return result

    def list_server_ip(self, data=None):
        result = self.__call_interface__('CMDB', 'get_server_ip')
        return result

    def list_supported_cluster(self):
        result = self.__call_interface__('CLUSTER', 'get_cluster_name')
        cluster_list = list()
        cluster_list.append('')
        if result:
            for cluster_name in result:
                cluster_list.append(cluster_name)
        else:
            return False
        return zip(cluster_list, cluster_list)

    def list_supported_type(self):
        result = self.__call_interface__('CMDB', 'gettype')
        type_list = list()
        type_list.append('')
        if result:
            for entry in result:
                type_list.append(entry['status'])
        else:
            return False
        return zip(type_list, type_list)

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

        return zip(dba_list, dba_list)

    def list_supported_status(self):
        result = self.__call_interface__('CMDB', 'getinstancestatus')
        status_list = list()
        status_list.append('')
        if result:
            for status in result:
                status_list.append(status['status'])
        else:
            return False
        return zip(status_list, status_list)

    def info_by_id(self, instance_id):
        data = {"id": instance_id}
        result = self.__call_interface__('CMDB', 'getinstanceinfo', json_obj=data)
        return result

    def add_instance(self, info):
        result = self.__call_interface__('CMDB', 'init_instance_flow', json_obj=info, timeout=1000)
        return result

    def get_total_cnt(self):
        result = self.__call_interface__('CMDB', 'getinstancecount')
        return result

    def online_instance(self, data):
        result = self.__call_interface__('CMDB', 'OnlineInstance', json_obj=data)
        return result

    def pre_offline_instance(self, data):
        result = self.__call_interface__('CMDB', 'PreOfflineInstance', json_obj=data)
        return result

    def offline_instance(self, data):
        result = self.__call_interface__('CMDB', 'OfflineInstance', json_obj=data)
        return result

    def my_instance_workflow(self, data):
        result = self.__call_interface__('TEMPLATE', 'get_user_flows', json_obj=data)
        return result

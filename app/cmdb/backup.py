from cmdb_api_base import CmdbApiBase

class BackupList(CmdbApiBase):
    def mha(self):
        result = self.__call_interface__('BACKUP','backup_info/Mysql_Cluster',json_obj=None)
        return result

    def single_instance(self):
        result = self.__call_interface__('BACKUP','backup_info/Single',json_obj=None)
        return result

    def configure(self):
        result = self.__call_interface__('BACKUP','get_config',json_obj=None)
        return result

    def email_backup_report(self):
        result = self.__call_interface__('BACKUP','report',json_obj=None)
        return result

    def add_backup(self,data):
        result = self.__call_interface__('BACKUP','addbackup',json_obj=data)
        return result

    def del_backup(self,data):
        result = self.__call_interface__('BACKUP','delbackup',json_obj=data)
        return result

    def switch_flag(self,data):
        result = self.__call_interface__('BACKUP','switch_flag',json_obj=data)
        return result

from cmdb_api_base import CmdbApiBase

class BackupList(CmdbApiBase):
    def mha(self):
        result = self.__call_interface__('BACKUP','backup_info',json_obj=None)
        return result

    def backup_report(self):
        result = self.__call_interface__('BACKUP','backup_report',json_obj=None)
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

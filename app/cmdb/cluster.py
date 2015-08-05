from cmdb_api_base import CmdbApiBase

class Cluster(CmdbApiBase):
    def get_cluster_list(self):
        result = self.__call_interface__('CLUSTER','cluster_status')
        return result

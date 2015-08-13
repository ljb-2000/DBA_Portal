# coding: utf-8

import requests as requests
import json
from cmdb_config import CMDB_API_ADDR


class CmdbApiCallException(Exception):
    def __init__(self, error_no=0, msg='', module='', interface='', param=''):
        self.error_no = error_no
        self.message = msg
        self.module = module
        self.interface = interface
        self.param = param

    def detail_msg(self):
        template_msg = "CMDB API Error: Module %s; Interface %s; Error Code: %s; Message: %s"
        msg = template_msg % (self.module, self.interface, self.error_no, self.message)
        return msg


class CmdbApiBase:
    __api_addr = ""
    __last_error = 0
    __last_error_msg = ''

    def __init__(self, __api_addr=CMDB_API_ADDR):
        self.__api_addr = __api_addr

    def __call_interface__(self, module_name, interface_name, json_obj=None,timeout=20):
        """
        :rtype : dict
        """
        try:
            if json_obj:
                query_obj = {"data": json.dumps(json_obj)}
            else:
                query_obj = {"data": "{}"}
            fp = requests.get(self.__api_addr + module_name + '/' + interface_name, params=query_obj, timeout=timeout)
            if fp.status_code == requests.codes.ok:
                result = fp.json()
                if not result:
                    raise CmdbApiCallException(error_no=0, msg="Result from remote api is not a valid json str",
                                               module=module_name, interface=interface_name, param=json.dumps(json_obj))
                if result['status'] == 0:
                    return result['data']
                else:
                    raise CmdbApiCallException(error_no=result['status'], msg=result['data'],module=module_name, interface=interface_name, param=json.dumps(json_obj))
                                               
            else:
                fp.raise_for_status()
        except Exception, e:
            msg = "Fail to call CMDB service. %s: %s" % (type(e).__name__, e.message)
            raise Exception(msg)
        #raise Exception('Fail to call CMDB service...')
            

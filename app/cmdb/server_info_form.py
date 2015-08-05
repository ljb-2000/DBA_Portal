# -*- coding: utf-8 -*-
from flask.ext.wtf import Form
import wtforms
from server import ServerList


class ServerInitForm(Form):
    server_id = wtforms.StringField('SerialNO', validators=[])
    server_ip = wtforms.StringField('Server IP', validators=[wtforms.validators.IPAddress()])
    mirror = wtforms.SelectField('Mirror', validators=[], choices=[])
    comment = wtforms.TextAreaField('Memo', validators=[])

class ServerInfoForm(Form):
    ram_size = wtforms.SelectField('&nbsp;&nbsp;内存', validators=[], choices=[])
    idc = wtforms.SelectField('机房', validators=[], choices=[])
    logic_cpu_count = wtforms.SelectField('&nbsp;&nbsp;CPU核数', validators=[], choices=[])

class StandbyServerInfoForm(Form):
    server_id = wtforms.StringField('SerialNO', validators=[])
    ram_size = wtforms.SelectField('&nbsp;&nbsp;内存大于', validators=[], choices=[])
    idc = wtforms.SelectField('机房', validators=[], choices=[])
    cpu = wtforms.SelectField('&nbsp;&nbsp;CPU核数大于', validators=[], choices=[])

class ApplyServerForm(Form):
    bu = wtforms.SelectField('选择业务线', validators=[], choices=[])
    product = wtforms.SelectField('子业务', validators=[], choices=[])
    type = wtforms.SelectField('数据库类型', validators=[],choices=[])
    dba_owner = wtforms.SelectField('负责人', validators=[],choices=[])
    ip = wtforms.HiddenField('', validators=[])

class InstallDbForm(Form):
    buss = wtforms.SelectField('业务线', validators=[], choices=[])
    version = wtforms.SelectField('数据库版本', validators=[], choices=[])
    dba_owner = wtforms.SelectField('负责人', validators=[], choices=[])
    port = wtforms.SelectField('端口', validators=[], choices=[])
    mem = wtforms.IntegerField('内存大小（单位MB）', validators=[])
    backup = wtforms.BooleanField('配置备份', validators=[])
    zabbix = wtforms.BooleanField('配置监控', validators=[])
    comment = wtforms.StringField('实例描述', validators=[])
    replSet = wtforms.StringField('集群名', validators=[])
    server_id = wtforms.HiddenField('', validators=[])

class InstanceInfoForm(Form):
    server_id = wtforms.StringField('SerialNO', validators=[])
    server_ip = wtforms.StringField('Server IP', validators=[wtforms.validators.IPAddress()])
    port = wtforms.StringField('端口', validators=[])
    status = wtforms.SelectField('状态', validators=[], choices=[])
    type = wtforms.SelectField('数据库类型', validators=[], choices=[])
    dba_owner = wtforms.SelectField('负责人', validators=[], choices=[])
    buss = wtforms.StringField('部门', validators=[])
    cluster_name = wtforms.SelectField('集群名', validators=[], choices=[])

class BackupForm(Form):
    buss =wtforms.SelectField('Buss',validators=[])
    ip = wtforms.SelectField('IP',validators=[])
    port = wtforms.SelectField('Port',validators=[])
    type =wtforms.SelectField('Type',validators=[])

if __name__ == '__main__':
    test = ServerInfoForm()

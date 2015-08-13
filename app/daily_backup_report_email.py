#!/usr/bin/python
#coding:utf-8
import requests
import urllib2
import time
import re
from config import AppConfig

def add_full_path_to_url(prefix, line):
    """
    Description: add full path to url.
    Parameters format:
    ### prefix: '10.1.1.193:5000'
    ### line: '<script src="/static/js/jquery-1.11.0.js"></script>'
    Example:
    ### line1 = add_full_path_to_url('10.1.1.193:5000', '<script src="/static/js/jquery-1.11.0.js"></script>')
    ### line1 is '<script src="10.1.1.193:5000/static/js/jquery-1.11.0.js"></script>'
    ### line2 = add_full_path_to_url('10.1.1.193:5000', '<link href="/static/css/plugins/morris.css" rel="stylesheet"')
    ### line2 is '<link href="10.1.1.193:5000/static/css/plugins/morris.css" rel="stylesheet">'
    """
    if not (prefix and line):
        return ''
    re_js = re.compile('\s+\<script src\=\"(?P<js_link>[\w\/\.\-]+)\"\>.*')
    re_css = re.compile('\s+\<link href\=\"(?P<css_link>[\w\/\.\-]+)\".*')
    m_js = re_js.match(line)
    m_css = re_css.match(line)
    if m_js:
        line = '<script src="%s"></script>' % (prefix + m_js.group("js_link"))
    if m_css:
        line = '<link href="%s" rel="stylesheet">' % (prefix + m_css.group("css_link"))
    return line

def get_data_from_link(prefix, line):
    """
    Description: get_data_from_link.
    Parameters format:
    ### prefix: '10.1.1.193:5000'
    ### line: '<script src="/static/js/jquery-1.11.0.js"></script>'
    Example:
    ### line1 = get_data_from_link('10.1.1.193:5000', '<script src="/static/js/jquery-1.11.0.js"></script>')
    ### line1 is '<js_string>'
    """
    if not (prefix and line):
        return ''
    re_js = re.compile('\s+\<script src\=\"(?P<js_link>[\w\/\.\-]+)\"\>.*')
    re_css = re.compile('\s+\<link href\=\"(?P<css_link>[\w\/\.\-]+)\".*')
    m_js = re_js.match(line)
    m_css = re_css.match(line)
    if m_js:
        print line
        site = prefix + m_js.group("js_link")
        line = urllib2.urlopen(site).read()
        print line
    if m_css:
        print line
        site = prefix + m_css.group("css_link")
        line = urllib2.urlopen(site).read()
        print line
    return line


if __name__ == '__main__':
    email_backup_report = AppConfig.PORTAL_SITE + '/email_backup_report'
    content = urllib2.urlopen(email_backup_report).read()
    conn_count = 1
    while conn_count < 1024 and ('Connection aborted' in content or '10.1.1.193' in content or 'read timeout' in content or 'Fail to call CMDB service' in content):
        print 'connect fail, reconnect after %d s...' % conn_count
        time.sleep(conn_count)
        conn_count *= 4
        content = urllib2.urlopen(email_backup_report).read()
        
    # content_list = content.split('\n')
    # content_need = ''

    # flag = 0 #0:need, 1:ignore
    # re_wrapper = re.compile('\<div id=\"wrapper\"\>')
    # re_start_report = re.compile('\<div class=\"start_div_email_backup_report\"\>')
    # re_end_report = re.compile('\<div class=\"end_div_email_backup_report\"\>')
    # for line in content_list:
    #     if flag == 0:
    #         m_wrapper = re_wrapper.match(line)
    #         if m_wrapper:
    #             flag = 1
    #     elif flag == 1:
    #         m_start = re_start_report.match(line)
    #         if m_start:
    #             flag = 0
    #     if flag == 0:
    #         content_need += ('\n' + line)

    if not ('Connection aborted' in content and '10.1.1.193' in content and 'read timeout' in content and 'Fail to call CMDB service' in content):
        sendTo = AppConfig.SEND_TO
        sendmail_data = {'sendTo':sendTo, 'subject':'数据库备份日报', 'message':''}
        sendmail_data['message'] = content
        tool_sendmail = AppConfig.CMDB_SITE + '/TOOL/sendmail'
        print requests.get(tool_sendmail, data=sendmail_data).text
    elif 'cluster_backup_report_detail' in content:
        sendTo = AppConfig.SEND_TO_DEV
        sendmail_data = {'sendTo':sendTo, 'subject':'出错了！！！', 'message':'数据库备份日报, dev:192.168.222.156; online:10.1.1.193;'}
        tool_sendmail = AppConfig.CMDB_SITE + '/TOOL/sendmail'
        print requests.get(tool_sendmail, data=sendmail_data).text

pid=`ps -ef | grep /usr/local/app/DBA_Portal/app/env/bin/python.*DBA_Portal | grep -v grep | awk '$3!=1{print $2}'`
if [ "${pid}" != "" ]; then
    kill  ${pid}
    echo "${pid} killed"
fi

env PYTHONIOENCODING=utf-8 nohup /usr/local/app/DBA_Portal/app/env/bin/python /usr/local/app/DBA_Portal/app/DBA_Portal.py  & 1>/dev/null 2>&1
#

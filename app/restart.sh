pid=`ps -ef | grep /usr/local/app/dba_portoal/app/index | grep -v grep | awk '$3!=1{print $2}'`
if [ "${pid}" != "" ]; then
    kill  ${pid}
    echo "${pid} killed"
fi

env PYTHONIOENCODING=utf-8 nohup /usr/local/app/dba_portoal/app/env/bin/python /usr/local/app/dba_portoal/app/index.py  & 1>/dev/null 2>&1
#

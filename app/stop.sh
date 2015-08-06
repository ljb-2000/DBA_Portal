pid=`ps -ef | grep /usr/local/app/DBA_Portal/app/DBA_Portal | grep -v grep | awk '$3!=1{print $2}'`
if [ "${pid}" != "" ]; then
    kill  ${pid}
    echo "${pid} killed"
fi

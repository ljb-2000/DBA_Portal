import PySQLPool

connection = PySQLPool.getNewConnection(username='ape', password='ape123ASD123!@#', host='10.2.15.12', db='ape')
query = PySQLPool.getNewQuery(connection)
query.Query('select * from  config')
for row in query.record:
    print row['name']

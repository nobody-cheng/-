import pymysql
# 将包安装为mysqldb，因为django内部的orm使用的名称为mysqldb
pymysql.install_as_MySQLdb()
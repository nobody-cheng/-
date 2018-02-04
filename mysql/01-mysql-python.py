from pymysql import *


def main():
    """
    1.创建数据库的连接
    host=None,user=None,password=''
    database=None,port=0,unix_slcket=None,charset=''
    """
    conn = connect(host='localhost',
                   user='root',
                   password='mysql',
                   database='jing_dong',
                   port=3306,
                   charset='utf8')
    """
    2.获取数据库操作对象
    """
    cur = conn.cursor()
    # 3.sql
    sql = "insert into goods_cates (name) values('洗衣机')"

    # 4.执行sql
    cur.execute(sql)

    # 5.如果是更新数据的操作应该是commit
    conn.commit()
    # 6.关闭cursor,关闭连接
    cur.close()
    conn.close()

if __name__ == '__main__':
    main()





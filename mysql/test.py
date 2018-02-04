from pymysql import *


def main():

    conn = connect(host='localhost',
                   port=3306,
                   database='jing_dong',
                   user='root',
                   password='mysql',
                   charset='utf8')

    cur = conn.cursor()
    sql = 'insert into goods_cates(name) values ("啦啦")'
    cur.execute(sql)
    conn.commit()
    cur.close()
    conn.close()


if __name__ == '__main__':
    main()
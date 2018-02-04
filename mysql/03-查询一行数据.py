from pymysql import *


def main():
    conn = connect(host='localhost',
                   port=3306,
                   user='root',
                   password='mysql',
                   database='jing_dong',
                   charset='utf8')

    cs1 = conn.cursor()

    # count = cs1.execute('select id,name from goods where id>=4')
    count = cs1.execute('select * from goods')
    print('查询到%d条数据' % count)

    for i in range(count):
        result = cs1.fetchone()
        print(result)

    # result = cs1.fetchone()
    # print(result)


    result = cs1
    cs1.close()
    conn.close()

if __name__ == '__main__':
    main()
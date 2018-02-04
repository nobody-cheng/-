from pymysql import *


def main():
    # 创建connection连接
    conn = connect(host='localhost',
                   database='jing_dong',
                   port=3306,
                   user='root',
                   password='mysql',
                   charset='utf8')
    # 获取cursor对象
    cs1 = conn.cursor()
    # 执行insert语句，并返回受影响的行数，添加一条数据
    sql = 'insert into goods_cates(name) values("光驱")'
    sql1 = 'insert into goods_cates(name) values("机械硬盘")'

    count = cs1.execute(sql)
    count = cs1.execute(sql1)

    print(count)

    # 更新
    count = cs1.execute('update goods_cates set name="固态硬盘" where name="机械硬盘"')

    # # 删除
    # count = cs1.execute('delete from goods_cates where id=6')

    # 提交之前的操作，如果之前已经执行过多次的execute，那么就都提交
    conn.commit()
    # 关闭cursor对象
    cs1.close()
    # 关闭connection
    conn.close()

if __name__ == '__main__':
    main()
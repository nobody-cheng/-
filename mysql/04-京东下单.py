from pymysql import *
import time


class JD(object):
    def __init__(self):
        # 连接
        self.db = connect(host='localhost',
                          port=3306,
                          user='root',
                          password='mysql',
                          database='stock_db',
                          charset='utf8')
        # 操作对象
        self.cursor = self.db.cursor()
        # 用户登陆的标示
        self.custoner = None

    def print_menu(self):
        """打印功能"""
        print("------京东商城-------")
        print("1: 显示所有的商品")
        print("2: 下订单")
        print("3: 登录")
        print("4: 注册")
        print("5: 退出")
        op = input("请输入对应的数字: ")

        return op
    def __del__(self):
        self.cursor.close()
        self.db.close()


    def run(self):
        while True:
            op = self.print_menu()
            if op == '1':
                self.show_all_goods()
            elif op == '2':
                self.order()
            elif op == '3':
                self.login()
            elif op == '4':
                self.register()
            elif op =='5':
                break
            else:
                print('输入有误，请重新输入')

    def show_all_goods(self):
        sql = """select g.id,g.name,c.name,b.name,g.price from goods as g
                     inner join goods_cates as c on g.cate_id = c.id
                     inner join goods_brands as b on g.brand_id = b.id"""
        self.cursor.execute(sql)
        ret = self.cursor.fetchall()

    def login(self):
        """登陆"""
        name = input('请输入用户名')
        pwd = input('请输入密码')
        # 查询
        sql = 'select * from customer where name = %s and pass = %'
        ret = self.cursor.execute(sql, [name, pwd])
        ret = self.cursor.fetchone()
        if ret is None:
            # 没找到数据，登陆失败
            print('用户名或者密码错误，登陆失败，请重试')
            return
        print(">>>>>登录成功>>>>>")
        self.customer_id = ret[0]

    def register(self):
        """注册"""
        name = input('请输入用户名：')
        tel = input('请输入电话号码：')
        pwd = input('请输入密码：')
        # 判断用户名是否已经存在
        sql = 'select * from customer where name = %s'
        self.cursor.execute(sql, [name])
        ret = self.cursor.fetchone()

        # 存在就不能注册
        if ret:
            print('用户名已经存在，请重新注册')
            return
        # 不存在才能注册
        sql = 'insert into customer(name,tel,passwd) values (%s, %s, %s)'
        # 操作数据库，插入数据
        self.cursor.execute(sql, [name, tel, pwd])
        # 提交
        self.db.commit()
        print('注册成功')

    def order(self):
        """下订单"""
        if self.customer_id is None:
            print('请先登陆，再下订单')
            return
        goods_id = input('请输入商品的编号：')
        if goods_id.isdigit():
            # 订单详情表中生成详情的信息
            # 如何获得刚插入的订单id
            #lastrowid 是刚获取到上次sql语句执行后最后一行的主键的值
            order_id = self.cursor.lastrowid
            # sql = 'insert into order_detail(order_id, goods_id, customer_id) values (%s, %s)'
            self.cursor.execute(sql, [order_id, goods_id, '1'])




def main():
    jd = JD()
    jd.run()

if __name__ == '__main__':
    main()

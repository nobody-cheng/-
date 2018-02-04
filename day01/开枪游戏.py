#  定义玩家类
class Player(object):
    def __init__(self, name):
        self.name = name
        self.hp = 100

    def __str__(self):
        return '%s血量为%d' % (self.name, self.hp)

    def zhuang_zi_dan(self, box, bullet):
        box.add_bullet(bullet)

    def zhuang_dan_jia(self, gun, box):
        gun.add_box(box)

    def take_gun(self, gun):
        self.gun = gun

    def biu_biu(self, enemy):
        self.gun.shoot(enemy)

    def drop_hp(self, power):
        """被子弹射中扣血"""
        self.hp -= power


#  定义枪类
class Gun(object):
    def __init__(self, name):
        self.name = name
        self.box = None

    def add_box(self, box):
        if self.box == None:
            self.box = box
        else:
            print('已有弹夹，无法再装弹夹')

    def __str__(self):
        if self.box == None:
            return '%s没有弹夹' % self.name
        else:
            return '%s，弹夹信息为%s' % (self.name, self.box)

    def shoot(self, enemy):
        bullet = self.box.pop_bullet()

        if bullet != None:
            bullet.hurt(enemy)


#  定义弹夹类
class Box(object):
    def __init__(self, max_size):
        self.max_size = max_size
        self.bullets = []

    def add_bullet(self, bullet):
        if len(self.bullets) < len(self.max_size):
            self.bullets.append(bullet)
        else:
            print('弹夹已满')

    def __str__(self):
        return '弹夹容量%s,剩余子弹个数为%s' % (self.max_size, len(self.bullets))

    def pop_bullet(self):
        if len(self.bullets) != 0:
            bullet= self.bullets.pop()
            return bullet
        else:
            print('没有子弹')
            return None


#  定义子弹类
class Bullet(object):
    def __init__(self, power):
        self.power = power

    def __str__(self):
        return '伤害为%d' % self.power

    def hurt(self, enmey):
        """伤害敌人"""
        enemy.drop_hp(self.power)

#  创建玩家对象
xidada = Player('中国')
print(xidada)

#  创建枪对象
gun = Gun('ak47')
print(gun)

#  创建弹夹对象
box = Box('20')
print(box)

#  创建子弹对象
bullet = Bullet(22)
print(bullet)

"""============组装枪支============="""
xidada.zhuang_zi_dan(box, bullet)
print(box)

# 再装一个子弹
bullet1 = Bullet(22)
xidada.zhuang_zi_dan(box, bullet1)
print(box)

xidada.zhuang_dan_jia(gun, box)
print(gun)

"""============组装枪支============="""
#  创建敌人对象
enemy = Player('日本')
print(enemy)

xidada.take_gun(gun)
print(xidada)

xidada.biu_biu(enemy)
print(enemy)

xidada.biu_biu(enemy)
print(enemy)






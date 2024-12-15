class Character:
    """
    класс существа на карте
    """

    # параметры
    _HP = 1
    _armour = 1
    _damage = 1
    _cool_down = 5
    _x = 0
    _y = 0
    _direction = 0

    def __int__(self, hp, arm, dmg, cd, x, y):
        self._HP = hp
        self._armour = arm
        self._damage = dmg
        self._cool_down = cd
        self._x = x
        self._y = y

    # регистрация урона, полученного персонажем
    def received_damage(self, received_dmg):
        """
        снижение брони и здоровья в результате полученного урона
        :param received_dmg: полученный персонажем урон
        :return: void
        """
        self._HP = min(self._HP, self._HP - (received_dmg - self._armour))
        self._armour = max(self._armour - received_dmg, 0)


class Hero(Character):
    """
    класс нашего персонажа
    """

    def __init__(self, hp, arm, dmg, cd, x, y):
        super().__int__(hp, arm, dmg, cd, x, y)
        self._crit = 0.1

    def moveX(self, dif_x):
        self._x += dif_x

    def moveY(self, dif_y):
        self._y += dif_y

    def get_position(self):
        return self._x, self._y

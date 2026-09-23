class Hero:
    def __init__(self, name, hp):
        self.name = name
        self.hp = hp

    def take_damage(self, amount):
        self.hp -= amount


arthur = Hero("Arthur", 100)
morgana = Hero("Morgana", 100)

arthur.take_damage(10)

print("Arthur:", arthur.hp,"HP")
print("Morgan:", morgana.hp,"HP")

obj1 = Hero("Arthur", 100)
obj2 = Hero ("Morgana", 100)
class Dish:
    def __init__(self, name, description, price):
        self.name = name
        self.description = description
        self.price = price

class MenuCategory:
    def __init__(self, name, dishes):
        self.name = name
        self.dishes = dishes

class Order:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def remove_item(self, item):
        self.remove_item(item)

    def calculate_total(self):
        total = 0
        for item in self.items:
            total += item.price
        return total

#Страви
dish1 = Dish("Капрезе","Салат з помідорів, моцарелли та базиліку",10)
dish2 = Dish("Стейк", "М'ясний стейк з соусом", 20)
dish3 = Dish("Тірамісу", "Десерт з кави", 10)

#Категорії страв
category1 = MenuCategory("закуски",[dish1])
category2 = MenuCategory("основні страви",[dish2])
category3 = MenuCategory("десерти",[dish3])

#Додавання страв
order = Order()
order.add_item(dish1)
order.add_item(dish2)
order.add_item(dish3)

#Виведення на екран
for item in order.items:
    print(f"Назва: {item.name}, Опис: {item.description}, Ціна: ${item.price}")
print(f"Загальна сума: ${order.calculate_total()}")
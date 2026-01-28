##1-Masala:
# class CartItem:
#     def __init__(self, name, price, quantity, discount):
#         # Mahsulot nomi
#         self.name = name
#         # Mahsulot narxi
#         self.price = price
#         # Mahsulot miqdori
#         self.quantity = quantity
#         # Chegirma foizi
#         self.discount = discount
#
#     def total_cost(self):
#         # Chegirma qo'llangan umumiy narxni hisoblash
#         return self.price * self.quantity * (1 - self.discount / 100)
#
#
# # Oziq-ovqat mahsulotlari uchun sinf
# class FoodItem(CartItem):
#     def total_cost(self):
#         # Asosiy sinfdagi hisoblash metodidan foydalanish
#         cost = super().total_cost()
#         # Formatlangan natijani qaytarish
#         return f"Oziq-ovqat mahsuloti: {self.name} -> {cost:.2f}$"
#
#
# # Oziq-ovqat bo'lmagan mahsulotlar uchun sinf
# class NonFoodItem(CartItem):
#     def total_cost(self):
#         # Asosiy sinfdagi hisoblash metodidan foydalanish
#         cost = super().total_cost()
#         # Formatlangan natijani qaytarish
#         return f"Oziq-ovqat mahsuloti: {self.name} -> {cost:.2f}$"
#
#
# # Savatchadagi mahsulotlar ro'yxati
# items = [
#     FoodItem("Olma", 1.5, 3, 10),
#     FoodItem("Non", 2.0, 2, 5)
# ]
#
# # Barcha mahsulotlar bo'yicha umumiy summani hisoblash
# total_sum = 0
#
# # Har bir mahsulotning narxini chiqarish
# for item in items:
#     print(item.total_cost())
#     total_sum += item.price * item.quantity * (1 - item.discount / 100)
#
# # Umumiy savatcha narxini chiqarish
# print("Umumiy summa:", round(total_sum, 2), "$")
#
#

##2-Masala:
# class Vehicle:
#     def __init__(self, name, distance, fuel_efficiency, fuel_price):
#         self.name = name
#         self.distance = distance
#         self.fuel_efficiency = fuel_efficiency
#         self.fuel_price = fuel_price
#
#     def trip_cost(self):
#         return self.distance * self.fuel_efficiency * self.fuel_price
#
#
# class Car(Vehicle):
#     def show_cost(self):
#         cost = self.trip_cost()
#         return f"Transport nomi: {self.name} -> {cost:.2f}"
#
#
# class Motorcycle(Vehicle):
#     def show_cost(self):
#         cost = self.trip_cost()
#         return f"Transport nomi: {self.name} -> {cost:.2f}"
#
#
# items = [
#     Car("Avto", 130, 5, 8),
#     Motorcycle("Motosikl", 78, 7, 9)
# ]
#
# total_cost = 0
# for item in items:
#     print(item.show_cost())
#     total_cost += item.trip_cost()
#
# print("Umumiy xarajat:", round(total_cost, 2))

##3-Masala:
# Hayvonlar = [{"It", 500}, {"Mushuk", 200}]
# class Pet:
#     def __init__(self,name, daily_food):
#         self.name = name
#         self.daily_food = daily_food
#
#
#     def fedding_plan(self):
#         return self.daily_food
#
#
# class Dog(Pet):
#     def fedding_plan(self):
#         amount = super().fedding_plan()
#         return f"It nomi;{self.name},kunlik ovqat miqdori;{amount} gramm"
#
#
# class Cat(Pet):
#     def fedding_plan(self):
#         amount = super().fedding_plan()
#         return f"Mushuk nomi;{self.name},kunlik ovqat miqdori;{amount} gramm"
#
# if __name__ == '__main__':
#     dog = Dog("Olapar", 500)
#     cat = Cat("Mosh",200)
#
#     print(dog.fedding_plan())
#     print(cat.fedding_plan())

















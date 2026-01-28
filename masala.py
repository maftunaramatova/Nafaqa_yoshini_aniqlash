##1-Masala:
# class Transport:
#     def __init__(self,model:str,yil:int):
#         self.model = model
#         self.yil = yil
#
#     def malumot(self)-> str:
#         return f"Model: {self.model} Yil: {self.yil}"
#
# class Avtomobil(Transport):
#     def __init__(self, model: str , yil:int, yonilgi_turi: str):
#         super().__init__(model,yil)
#         self.yonilgi_turi = yonilgi_turi
#
#     def malumot(self):
#         baza = super().malumot()
#         return f"{baza} , Yonilg'i:{self.yonilgi_turi}"
#
# class Avtobus(Transport):
#     def __init__(self, model: str , yil:int,orinlar_soni: str ):
#         super().__init__(model,yil)
#         self.orinlar_soni = orinlar_soni
#     def malumot(self):
#         baza = super().malumot()
#         return f"{baza} , O'rindiqlar soni:{self.orinlar_soni}"
#
# a = Avtomobil("Cobalt",2022,"benzin")
# print(a.malumot())
#
# b = Avtomobil("Isuzu",2018,"40")
# print(b.malumot())
#

##2-masala:
# class Kitob:
#     def __init__(self, nom,muallif,yil):
#         self.nom = nom
#         self.muallif = muallif
#         self.yil = yil
#
#     def taqdimot(self):
#         return f"Kitob nomi:{self.nom},Kitob muallifi:{self.muallif},Yili: {self.yil}"
#
# class ElektronKitob(Kitob):
#     def __init__(self, nom,muallif,yil,fayl_hajmi_mb):
#         super().__init__(nom,muallif,yil)
#         self.fayl_hajmi_mb = fayl_hajmi_mb
#
#     def taqdimot(self):
#         baza = super().taqdimot()
#         return f"{baza}, [Elektron :{self.fayl_hajmi_mb}]"
#
# class AudioKitob(Kitob):
#     def __init__(self, nom,muallif,yil,davomiylik_soat):
#         super().__init__(nom, muallif, yil)
#         self.davomiylik_soat = davomiylik_soat
#
#     def taqdimot(self):
#         baza = super().taqdimot()
#         return f"{baza}, [Audio :{self.davomiylik_soat} soat]"
#
# e = ElektronKitob("Python asoslari", "Ali", 2023, 5)
# print(e.taqdimot())
#
# a = AudioKitob("O'tkan kunlar", "Abdulla Qodiriy", 2020, 12)
# print(a.taqdimot())

##3-Masala:
# class Xodim:
#     def __init__(self, ism,asosiy_maosh):
#         self.ism = ism
#         self.asosiy_maosh = asosiy_maosh
#
#     def oylik(self):
#         return self.asosiy_maosh
#
#     def malumot(self):

























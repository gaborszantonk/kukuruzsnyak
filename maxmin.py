print("Ez a program számokat kér be, majd megmondja, \n melyik volt a legnagyobb és a legkisebb szám")
lista = []
a = int(input("Hányszor fogsz megadni számokat?: "))
for i in range(1, 6):
    ele = int(input())
    lista.append(ele)
print(lista)
print (max(lista ))
print (min(lista ))

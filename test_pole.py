import time
import sys

def animace1():
    animation = "|/-\\"
    start_time = time.time()
    while True:
        for i in range(4):
            time.sleep(0.2)  # Feel free to experiment with the speed here
            sys.stdout.write("\r" + animation[i % len(animation)])
            sys.stdout.flush()
        if time.time() - start_time > 1:  # The animation will last for 10 seconds
            break
    sys.stdout.write("\nPřidáno do košíku!")

def zbozi_pod():
    for x in zbozi:
        print(x)

zbozi = ["1. Ipad", "2. Macbook", "3. Iphone", "4. Imac", "5. Airpods"]
kosik = []

print('''\   
                         ,--./,-.
                        / #      (
                       |          |
                        \        /  
                         `._,._,'
''')

print("------------------------------------------------------------------")
print("                     Vítejte v AppleShopu")
print("------------------------------------------------------------------")

while True:
    print("Dostupné zboží: ")
    zbozi_pod()    
    print("------------------------------------------------------------------")
    print("Váš košík: ", kosik)
    print("------------------------------------------------------------------")
    n = input("Vyberte zboží: ")

    if n == "Ipad" or "ipad" or "1" or "1." :
        animace1()
        print("\n------------------------------------------------------------------")
        kosik.append("Ipad")
        zbozi.pop(0)
        m = input("Chcete pokračovat v nákupu ?")
        if m.lower == "ano":
            print("Dobře")
            print("------------------------------------------------------------------")
        else:
            break
    elif n == "Macbook" or "macbook" or "2" or "2.":
        animace1()
        print("\n------------------------------------------------------------------")
        kosik.append("Macbook")
        zbozi.pop(1)
        m = input("Chcete pokračovat v nákupu ?")
        if m.lower == "ano":
            print("Dobře")
            print("------------------------------------------------------------------")
        else:
            break
    elif n == "Iphone" or "iphone" or "3" or "3.":
        animace1()
        print("\n------------------------------------------------------------------")
        kosik.append("Iphone")
        zbozi.pop(2)
        m = input("Chcete pokračovat v nákupu ?")
        if m.lower == "ano":
            print("Dobře")
            print("------------------------------------------------------------------")
        else:
            break
    elif n == "Imac" or "imac" or "4" or "4.":
        animace1()
        print("\n------------------------------------------------------------------")
        kosik.append("Imac")
        zbozi.pop(3)
        m = input("Chcete pokračovat v nákupu ?")
        if m.lower == "ano":
            print("Dobře")
            print("------------------------------------------------------------------")
        else:
            break
    elif n == "Airpods":
        animace1()
        print("\n------------------------------------------------------------------")
        kosik.append("Airpods")
        zbozi.pop(4)
        m = input("Chcete pokračovat v nákupu ?")
        if m.lower == "ano":
            print("Dobře")
            print("------------------------------------------------------------------")
        else:
            break
    else:
        print("Něco je špatně")
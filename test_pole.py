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
        if time.time() - start_time > 10:  # The animation will last for 10 seconds
            break
    sys.stdout.write("\rDone!")

def cislovany_zbozi():
    nove_zbozi = 

zbozi = ["Ipad", "Macbook", "Iphone", "Imac", "Airpods"]
kosik = []

print("------------------------------------------------------------------")
print("                     Vítejte v AppleShopu")
print("------------------------------------------------------------------")

while True:
    print("Dostupné zboží: ", zbozi)
    print("Váš košík: ", kosik)
    print("------------------------------------------------------------------")
    n = input("Vyberte zboží: ")
    
    if 


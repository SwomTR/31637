import requests
import random
import string
import time
print('''                       
  ____   ____ ____ 
 / ___| / ___/ ___|
 \___ \| |  | |  _ 
  ___) | |__| |_| |
 |____/ \____\____|                       
\n''')
time.sleep(0.2)
num = int(input('Kaç Key Üretilsin : '))
with open("Steam Key Codes.txt", "w", encoding='utf-8') as file:

    start = time.time()
 
    for i in range(num):
        code = "".join(random.choices(
            string.ascii_uppercase + string.digits,
            k = 5
        ))
        cod = "".join(random.choices(
            string.ascii_uppercase + string.digits,
            k = 5
        ))

        co = "".join(random.choices(
            string.ascii_uppercase + string.digits,
            k = 5
        ))

        c = "".join(random.choices(
            string.ascii_uppercase + string.digits,
            k = 5
        ))
 
        steam = "".join(random.choices(
            string.ascii_uppercase + string.digits,
            k = 5
        ))
        stea = "".join(random.choices(
            string.ascii_uppercase + string.digits,
            k = 5
        ))

        ste = "".join(random.choices(
            string.ascii_uppercase + string.digits,
            k = 5
        ))

        st = "".join(random.choices(
            string.ascii_uppercase + string.digits,
            k = 5
        ))
        s = "".join(random.choices(
            string.ascii_uppercase + string.digits,
            k = 5
        ))
        k = "".join(random.choices( string.digits,
            k = 3
        ))
        ke = "".join(random.choices(
            string.ascii_uppercase,
            k = 12
        ))
        key = "".join(random.choices( string.digits,
            k = 2
        ))
    
 
        file.write(f"{code}-{cod}-{co}-{c} \n")
        file.write(f"{steam}-{stea}-{ste}-{st}-{s} \n")
        file.write(f"{k}{ke} {key} \n")
    print(f"\n")
    print(f"Üretilen Key {num} | Ne Kadar Zaman Aldı : {time.time() - start}\n")
    input("\nSteam Kodları Hazır Steam Key Codes.txt Adlı Dosyaya Kaydetmek \nİçin Enter Tuşuna Basman Yeterli :)")
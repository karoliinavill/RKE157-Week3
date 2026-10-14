""" 
Programm palub kasutajal sisestada arvu. Kasutaja sisestab arvu. 
Programm määrab, kas arv on paaris või paaritu, ja annab vastava tagasiside. 
"""

#modulus ( % )
from colorama import Fore, Style
n = int(input("Sisesta täisarv: "))

# if n % 2 == 0:
#     print("Arv on paaris.")
# else:
#     print("Arv on paaritu.")

#ternary operator
#print("Arv on paaris." if n % 2 == 0 else "Arv on paaritu.")

#match case
match n % 2:
    case 0:
        print(Fore.GREEN + "Arv on paaris." + Style.RESET_ALL)
    case _:
        print(Fore.RED + "Arv on paaritu." + Style.RESET_ALL)

""" 
Kirjuta programm, mis küsib kasutajalt tema lemmikvärvi ja väljastab selle põhjal tema temperamendi.
punane --> energiline
roosa --> romantik
roheline --> rahulik
sinine --> keskendunud
muu --> imeline ükssarvik 
"""

from colorama import Fore, Style

colour = input("Sisesta oma lemmikvärv:").lower() #PUNANE --> punane

#variant 1
""" 
if colour == "punane":
    print("Sa oled energiline!")
elif colour == "roosa":
    print("Sa oled romantik!")
elif colour == "roheline":
    print("Sa oled rahulik")
elif colour == "sinine":
    print("Sa oled keskendunud!")
elif colour == "kollane":
    print("Sa oled rõõmsameelne!")
elif colour == "lilla":
    print("Sa oled loominguline!")
elif colour == "oranž":
    print("Sa oled seikluslik!")
elif colour == "must":
    print("Sa oled salapärane!")
else:
    print("Sa oled imeline ükssarvik!") """

#variant 2
match colour:
    case "punane":
        print(Fore.RED + "Sa oled energiline!" + Style.RESET_ALL)
    case "roosa":
        print(Fore.MAGENTA + "Sa oled romantik!" + Style.RESET_ALL)
    case "roheline":
        print(Fore.GREEN + "Sa oled rahulik" + Style.RESET_ALL)
    case "sinine":
        print(Fore.BLUE + "Sa oled keskendunud!" + Style.RESET_ALL)
    case "kollane":
        print(Fore.YELLOW + "Sa oled rõõmsameelne!" + Style.RESET_ALL)
    case "lilla":
        print(Fore.MAGENTA + "Sa oled loominguline!" + Style.RESET_ALL)
    case "oranž":
        print(Fore.RED + "Sa oled seikluslik!" + Style.RESET_ALL)
    case "must":
        print(Fore.BLACK + "Sa oled salapärane!" + Style.RESET_ALL)
    case _:
        print(Fore.CYAN + "Sa oled imeline ükssarvik!" + Style.RESET_ALL)

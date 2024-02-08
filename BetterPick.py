# Better Pick
from colorama import init as colorama_init
from colorama import Fore
from colorama import Style
import keyboard,os,time
colorama_init()

INDICATOR = ">"
def Pick(pick_title,listc,multiselect=False,highlight_color=Fore.GREEN,key={"UP":"w","DOWN":"s","SUBMIT":"enter","MULTISELECT_CHOOSE":"space"}):
    select = 0
    if multiselect:
        multiselectc = []
        utype = "( )"
        ctype = "(x)"
    else:
        utype = ""
        ctype = ""

    while True:
        if type(pick_title) == str: 
            print(pick_title)
        else:
            pick_title()
        for i in range(0,len(listc)):
            if multiselect:
                if i in multiselectc:
                    cm = ctype
                else:
                    cm = utype
                prefix = INDICATOR + " "
                if i == select:
                    prefix = INDICATOR + " "
                    print(prefix + cm + " "  + f"{highlight_color}{listc[i]}{Style.RESET_ALL}")
                else:
                    prefix = (len(INDICATOR)+1) * " "
                    print(prefix + cm + " " + listc[i])
            elif multiselect == False: 
                if i == select:
                    prefix = INDICATOR
                    print(prefix + " " + f"{highlight_color}{listc[i]}{Style.RESET_ALL}")
                else:
                    prefix = (len(INDICATOR)+1) * " "
                    print(prefix + " " + listc[i])
        while True:
            if keyboard.is_pressed(key["UP"]):
                if not select == 0:
                    select -= 1
                    break
            elif keyboard.is_pressed(key["DOWN"]):
                if not select == len(listc)-1:
                    select += 1
                    break
            elif keyboard.is_pressed(key["SUBMIT"]):
                if multiselect:
                    return multiselectc
                else:
                    return (listc[select],select)
            elif keyboard.is_pressed(key["MULTISELECT_CHOOSE"]):
                if multiselect:
                    if not select in multiselectc:
                        multiselectc.append(select)
                    else:
                        multiselectc.remove(select)
                    break
        time.sleep(0.1)
        os.system('cls' if os.name == 'nt' else 'clear')
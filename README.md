# BetterPick
> Modern menu selection in command prompt for command lines app! 
# How to install
Easily download `.py` files from `Release` tab than drag it into your Project folder.
+ Install Library
> BetterPick use [Colorama](https://pypi.org/project/colorama/) and [Keyboard](https://pypi.org/project/keyboard/)  
Install with `pip install colorama keyboard`
## Compatibility
Support: Python 3.x & Windows (Linux seems supported too but I haven't tested yet)
# Examples
> `BetterPick` is very easy too use!
## For regular use:  
`Pick("Your menu title goes here!",["Your selection here","Sec1","Sec2"],(True or False - Multiselect) )`  
**Note:** In Default, To move up or down selection use key `W,S` . Press `Enter` to submit choose. Also in multichoose , press `Spacebar` to check a selection (To change these key , look for "Change key-binding" in Advance use below)

Code: 
```
from BetterPick import Pick
# For single choose
# print(Pick("Your menu title goes here!",["Your selection here","Sec1","Sec2"],False))
# For multiselect
# print(Pick("Your menu title goes here!",["Your selection here","Sec1","Sec2"],True))
```

### Output:
+ Single-Choose (Multiselect = False)  
![image](https://github.com/ScadeBlock/BetterPick/assets/89845150/ff7bb2a9-adbb-4591-b811-8e8f7f38d188)
+ Multiselect  
![image](https://github.com/ScadeBlock/BetterPick/assets/89845150/37b09583-8986-433e-848f-fee62b324f10)

## For advance-use
+ Set highlight color  
```
from BetterPick import Pick
from colorama import Fore
print(Pick("Programming Languages",["Python","Java","C++"],highlight_color=Fore.BLUE))
# Set highlight color to blue
```
> BetterPick's Highlight use [`Colorama`](https://pypi.org/project/colorama/) (Really Good Library).
+ Output  
![image](https://github.com/ScadeBlock/BetterPick/assets/89845150/4631f67f-7fd2-41c0-86b5-e2a067d265a5)
------
+ Change indicator
```
import BetterPick
from BetterPick import Pick
BetterPick.INDICATOR = "*"
# Set INDICATOR from ">" to "*"
print(Pick("Programming Languages",["Python","Java","C++"]))
```
+ Output:  
![image](https://github.com/ScadeBlock/BetterPick/assets/89845150/1ffdcb42-3331-4db2-a83c-1845184991e3)
---
+ Change Key-binding  
```
from BetterPick import Pick
Key = {
    "UP":"up arrow", # Change UP key from "W" to Arrow-Up
    "DOWN":"down arrow", # Change DOWN key from "S" to Arrow-Down
    "SUBMIT":"enter",
    "MULTISELECT_CHOOSE":"space"
} 
print(Pick("Programming Languages",["Python","Java","C++"],key=Key))
```
--- 
**Fun Fact:** The menu title argument can be `String` or `Function`!

# (C) ScadeBlock

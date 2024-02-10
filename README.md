# BetterPick 💬
> Modern menu selection in command prompt for command lines app! 
# 👋 How to install
+ 🧡 Option 1 (Recommend) : Pip
    - Easily run: `pip install better-pick`
+ Option 2 : Manual Install
    - Easily download `.py` files from `Release` tab than drag it into your Project folder.
    - Install requirements with `pip install colorama keyboard`
## Compatibility 💥
Support: Python 3.x & Windows (Linux seems supported too but I haven't tested yet)
# ✨ Examples
> `BetterPick` is very easy too use! 🍖
## Supereme Demo
+ Combine BetterPick with [PyEmoji](https://pypi.org/project/emoji/) and [PyStyle](https://pypi.org/project/pystyle)  
![bandicam 2024-02-10 10-51-38-986](https://github.com/ScadeBlock/BetterPick/assets/89845150/7117cafb-56c8-48d9-adf6-8a73bbf94fa6)

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
![image](https://github.com/ScadeBlock/BetterPick/assets/89845150/425d53bf-068d-4e6d-9e5e-ec1f3bdfc4d9)
+ Multiselect  
![image](https://github.com/ScadeBlock/BetterPick/assets/89845150/65d3e606-9a51-4ed8-a30a-1da9fca317a9)

## For advance-use
### Set highlight color  
```
from BetterPick import Pick
from colorama import Fore
print(Pick("Programming Languages",["Python","Java","C++"],highlight_color=Fore.BLUE))
# Set highlight color to blue
```
> BetterPick's Highlight use [`Colorama`](https://pypi.org/project/colorama/) (Really Good Library).
+ Output  
![image](https://github.com/ScadeBlock/BetterPick/assets/89845150/b4149c05-621b-433b-bbdf-8b01bd98790f)
------
### Change indicator
```
import BetterPick
from BetterPick import Pick
BetterPick.INDICATOR = "*"
# Set INDICATOR from ">" to "*"
print(Pick("Programming Languages",["Python","Java","C++"]))
```
+ Output:  
![image](https://github.com/ScadeBlock/BetterPick/assets/89845150/bc39b17d-6672-4861-b151-d57c7b38155f)

**Fun Fact:** You can add color to BetterPick's Indicator too(Only recommend for v1.1a and above & I recommend using `Colorama` for colors). For example :  
```
import BetterPick
from BetterPick import Pick
from colorama import Fore,Style

BetterPick.COLOR_INDICATOR = f"{Fore.RED}*{Style.RESET_ALL}" # Indicator WITH color
BetterPick.INDICATOR = "*" # Indicator WITHOUT color
print(Pick("Programming Languages",["Python","Java","C++"]))
```
---
### Change checkbox in multiselect mode(For `Betterpick v1.1a` and above)
```
import BetterPick
from BetterPick import Pick
BetterPick.MULTISELECT_CHECK = "[x]"
BetterPick.MULTISELECT_UNCHECK = "[ ]"
print(Pick("Programming Languages",["Python","Java","C++"],multiselect=True))
```
![image](https://github.com/ScadeBlock/BetterPick/assets/89845150/a0b67b28-2d71-4407-a610-923365a59100)

**Fun Fact:** You can set Select box with colors too!

---
### Default choice(auto choose) in MultiSelect (`BetterPick 1.2` or above)
```
from BetterPick import Pick
print(Pick("Programming Languages",["Python","Java","C++"],multiselect=True,auto_choose=[0]))
```
![image](https://github.com/ScadeBlock/BetterPick/assets/89845150/0ad02b6a-44a4-4de9-ac43-7a7f99ae30b3)


---
### Pop-up animation (`v1.1a` or above)

```
import BetterPick
from BetterPick import Pick
from colorama import Fore,Style

print(Pick("Programming Languages",["Python","Java","C++"],popup_animation=True))
```

| Without Pop-up animation   | With Pop-up animation |
|----------------------------|-----------------------|
|![image](https://github.com/ScadeBlock/BetterPick/assets/89845150/aff129cf-0bcd-4ecb-8402-976eb6a1b4b0)|![image](https://github.com/ScadeBlock/BetterPick/assets/89845150/536d55a6-f3cf-468a-9b9c-6927fa24aae2)|

---
### Change Key-binding  
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

# (C) 2024 - Made By ScadeBlock

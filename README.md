## Animation Button
### Example-1
![animation_button.gif](/image/animation_button.gif)

### Python Code
```py
from tkinter import RIGHT, SE
from animationButton import AnimationButton

'''app is a master (root) window object
   first please create reference for Tk class
'''
AnimationButton(app, text='accept', fgcolor='black', event='1').pack(side=RIGHT, anchor=SE, padx=(5,10), pady=(0,5))
AnimationButton(app, text='cancel', fgcolor='black', event='1').pack(side=RIGHT, anchor=SE, pady=(0,5))
```

### Example-2
![animation_button-2.gif](/image/animation_button-2.gif)

### Python Code
```py
from tkinter import LEFT, X, NW
from animationButton import AnimationButton

#Frame - container for buttons
M = Frame()
M.pack(side=LEFT, padx=15)

#Button - animated menu
AnimationButton(M, text='Monday', bgcolor='green', fgcolor='black').pack(anchor=NW, fill=X)
AnimationButton(M, text='Tuesday', bgcolor='green', fgcolor='black').pack(anchor=NW, fill=X)
AnimationButton(M, text='Wednesday', bgcolor='green', fgcolor='black').pack(anchor=NW, fill=X)
AnimationButton(M, text='Thursday', bgcolor='green', fgcolor='black').pack(anchor=NW, fill=X)
AnimationButton(M, text='Friday', bgcolor='green', fgcolor='black').pack(anchor=NW, fill=X)
AnimationButton(M, text='Saturday', bgcolor='blue').pack(anchor=NW, fill=X)
AnimationButton(M, text='Sunday', bgcolor='blue').pack(anchor=NW, fill=X)
```

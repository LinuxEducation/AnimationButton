from tkinter import Tk, Label, Frame, SOLID, NW, W, LEFT, X

class AnimationButton(Label):
    def __init__(self, container, text='Button', event='Enter', bgcolor='green', fgcolor='white', command=None):
        Label.__init__(self, container)
        
        self.bgcolor = bgcolor
        self.fgcolor = fgcolor
        self.text = text
        self.command = command
        self.__color_number_idx = 0

        settings = {'text':                 text,
                    'bg':                   self.__get_colors()[0],
                    'fg':                   fgcolor,
                    'font':                 ('Verdana', 26, 'bold'),
                    'highlightthickness':   0,
                    'highlightbackground': 'black',
                    'relief':               SOLID,
                    'padx':                 20,
                    'pady':                 2}

        self.configure(**settings, anchor=W)
        self.event(event)

    def event(self, event):
        self.bind(f'<{event}>', self)
        if event == 'Enter':
            self.bind('<Button-1>', self)

    def __get_colors(self):
        animation_colors = {'green': ['#018201', '#009902', '#00b300', '#02cb00', '#00e600', '#00ff01', '#1aff10'],
                            'blue':  ['#012a84', '#00339b', '#003cb4', '#0043ce', '#004de2', '#0353fe', '#1865ff']}
        return animation_colors[self.bgcolor]

    def __animation(self):
        colors = self.__get_colors() + self.__get_colors()[:-1][::-1]
        if self.__color_number_idx <= colors.__len__()-1:
            self['background'] = colors[self.__color_number_idx]
            self.__color_number_idx += 1
            self.after(40, self.__animation)
        else:
            self.__color_number_idx = 0

    def __str__(self):
        return 'AppButton: ' + self.text

    def __dir__(self):
        return AnimationButton.__dict__

    def __call__(self, mouse):
        self.__animation()
        if self.command:
            return self.command()
        print(self.__str__())

    @staticmethod
    def test():
        print('Button Clicked!')


def main():
    app = Tk()
    app.geometry('650x400')
    app['background'] = '#424242'

    M = Frame()
    M.pack(side=LEFT, padx=15)

    AnimationButton(M, text='Monday', bgcolor='green', fgcolor='black').pack(anchor=NW, fill=X)
    AnimationButton(M, text='Tuesday', bgcolor='green', fgcolor='black').pack(anchor=NW, fill=X)
    AnimationButton(M, text='Wednesday', bgcolor='green', fgcolor='black').pack(anchor=NW, fill=X)
    AnimationButton(M, text='Thursday', bgcolor='green', fgcolor='black').pack(anchor=NW, fill=X)
    AnimationButton(M, text='Friday', bgcolor='green', fgcolor='black').pack(anchor=NW, fill=X)
    AnimationButton(M, text='Saturday', bgcolor='blue').pack(anchor=NW, fill=X)
    AnimationButton(M, text='Sunday', bgcolor='blue').pack(anchor=NW, fill=X)

    app.mainloop()

if __name__ == '__main__':
    main()
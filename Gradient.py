from tkinter import *

root = Tk()

root.geometry("500x500+200+200")
root.title("Gradient color change")
root.resizable(width = FALSE, height = FALSE)
def gradient(Start_at):
    def HEXcov(r,g,b):
        return(f'#{r:02x}{g:02x}{b:02x}')


    Out = []
    for i in range(int(Start_at[0]),226):
        Out.append(HEXcov(i,Start_at[1],Start_at[2]))

    return(Out)


def get_colour():
    colours = gradient([138, 43, 225])
    retreve_colors = colours[::-1]
    while True:
        for c in colours+retreve_colors:
            yield c
def start():
    root.configure(background=next(colour_getter))
    root.after(50, start)

colour_getter = get_colour()
start()

root.mainloop()

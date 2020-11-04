"""Put all code in window_loop()"""


def initWindow():
    global tkinter
    import tkinter
    global time
    import time

    global window
    window = tkinter.Tk()
    window.title("Hi")
    global windowLbl
    windowLbl = tkinter.Label(window, text="dddsdfs")
    windowLbl.pack()
def window_open():

    window.title("")
    window.after(1, window_after)
    window.mainloop()
def window_close():
    window.destroy()
    print("Window closed")
def window_change_title(strTitle):
    window.title(strTitle)
def window_change_content(strContent):
    windowLbl['text'] = strContent
def window_loop():#Put all code in this function!
    # ------------------------HERE------------------------
    window_change_title("Titel")
    window_change_content("Dies ist ein toller Test!       \nHallo!")


    # ------------------------HERE------------------------
    window.after(1, window_loop)
def window_after():
    print("Window opened")

    window.after(1, window_loop)

initWindow()
window_open()


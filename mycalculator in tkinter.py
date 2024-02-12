
 # This code was written to make a simple gui calculator !
 
  
#####################################NECESSAY-IMPORTS################################################
from tkinter import *
import tkinter.messagebox as m
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
from datetime import datetime
import sys ,os
#####################################NECESSAY-IMPORTS################################################


#####################################Functions################################################

   #loading screen ########################################
def simulate_loading():
    loading_text_label.config()
    h1_label.config() 

    progress_bar.stop()
    progress_bar.destroy()

    # Remove loading screen components
    h1_label.pack_forget()
    loading_text_label.pack_forget()

    # Display the calculator interface
    f.pack()

#####################################Function for image parsing ################################################
def resource_path(relative_path):
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except AttributeError:
        # Running as a script, use the current working directory
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)
#####################################FUNCTIONS FOR SOLVING EXPRESSIONS################################################
def click(event):
    global scvalue
    text = event.widget.cget("text")
    if text == "=":
        if scvalue.get().isdigit():
            value = int(scvalue.get())
        else:
            try:
                value = eval(screen.get().replace("**","^2").replace("X","*"))

            except Exception as e:
                print(e)
                value = "Error"
                m.showwarning("Syntax error", "Illegal operation!")

        scvalue.set(value)
        screen.update()

    elif text == "C":
        scvalue.set("")
        screen.update()

    else:
        scvalue.set(scvalue.get() + text)
        screen.update()
        
        
#####################################FUNCTION TO SHOW TIME################################################


def showtime():
    current_time=datetime.now().strftime("%H:%M:%S")
    m.showinfo("Current Time",f"The Current time is : {current_time}")
    
    
#####################################NECESSAY-IMPORTS################################################

#####################################WINDOW+ NECESSAY COMPONENTS################################################
root = tk.Tk()

root.geometry("560x700")
root.minsize(500, 650)
root.maxsize(580, 700)
root.title("My calculator in Tkinter")
root.wm_iconbitmap(resource_path("icon1.ico"))

#####################################START################################################
loading_label = tk.Label()

loading_text_label = tk.Label(
    root, text="Calculator App ", bg="#333333", fg="green", font="ar 20 bold"
)
loading_text_label.pack(pady=35, side="top", padx=50)

photo3 = PhotoImage(file="image1.png")

# name then method PhotoImage then use file and name of png files
h1_label = tk.Label(root, image=photo3)  # make label then image=name of ...
h1_label.pack(padx=50, pady=10)  # pack the label used above to display on screen!
loaded_image = Image.open(resource_path("image1.png")) # Replace with the path to your loaded image
loaded_image = ImageTk.PhotoImage(loaded_image)
# Add a loading animation using ttk.Progressbar

progress_bar = ttk.Progressbar(
    root, mode="indeterminate", cursor="hand2", orient="horizontal", length=200
)
progress_bar.pack(pady=30, side="bottom")
progress_bar.start()

root.after(5000, simulate_loading)

scvalue = StringVar()
scvalue.set("")
screen = Entry(root,cursor="ibeam",font="helvetica 40 bold",textvariable=scvalue,bg="cyan",justify="right",relief="sunken")
screen.pack(pady=12, padx=12, ipadx=8, ipady=8, fill=X)



#####################################MAIN-MENU BAR ON TOP################################################
menu_bar = tk.Menu(root)
root.config(menu=menu_bar)

file_menu = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="More Features", menu=file_menu)
file_menu.add_command(label="See Time", command=showtime)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=root.destroy)

help_menu = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Help", menu=help_menu)
help_menu.add_command(
    label="About",
    command=lambda: tk.messagebox.showinfo(
        "About","Calculator App by Muhammad Hasnat Rasool For more info contact on hasnatrasool163@gmail.com", ),)

#####################################FRAMES################################################


f = Frame(root, bg="#FF5733")  # 333333 #FF5733
a = Button(f,font="ar 30 ",text="C",borderwidth=5,justify="center",relief=SOLID,width=4,cursor="hand2",)
a.pack(side=LEFT, padx=10, pady=5)
a.bind("<Button-1>", click)
a = Button(f,font="ar 30 ",text="00",borderwidth=5,justify="center",relief=SOLID,cursor="hand2",width=4,)
a.pack(side=LEFT, padx=10, pady=5)
a.bind("<Button-1>", click)
a = Button(f,font="ar 30 ",text="^2",borderwidth=5,justify="center",relief=SOLID,cursor="hand2",width=4)
a.pack(side=LEFT, padx=10, pady=5)
a.bind("<Button-1>", click)
a = Button(f,font="ar 30 ",text="/",borderwidth=5,justify="center",relief=SOLID,cursor="hand2",width=4)
a.pack(side=LEFT, padx=10, pady=5)
a.bind("<Button-1>", click)
f.pack()


f = Frame(root, bg="#FF5733")
b = Button(
    f,font="ar 30 ",text="9",borderwidth=5,padx=8,pady=10,justify="center",relief=SOLID,width=3,cursor="hand2")
b.pack(side=LEFT, padx=10, pady=5)
b.bind("<Button-1>", click)
b = Button(f,font="ar 30 ",text="8",borderwidth=5,padx=8,pady=10,justify="center",relief=SOLID,width=3,cursor="hand2",
)
b.pack(side=LEFT, padx=10, pady=5)
b.bind("<Button-1>", click)
b = Button(f,font="ar 30 ",text="7",borderwidth=5,padx=8,pady=10,justify="center",relief=SOLID,width=3,cursor="hand2",)
b.pack(side=LEFT, padx=10, pady=5)
b.bind("<Button-1>", click)
b = Button(f,font="ar 30 ",text="X",borderwidth=5,padx=8,pady=10,justify="center",relief=SOLID,width=3,cursor="hand2")
b.pack(side=LEFT, padx=10, pady=5)
b.bind("<Button-1>", click)
f.pack()

f = Frame(root, bg="#FF5733")
c = Button(f,font="ar 30 ",text="4",borderwidth=5,padx=9,pady=10,justify="center",relief=SOLID,width=3,cursor="hand2",)
c.pack(side=LEFT, padx=10, pady=5)
c.bind("<Button-1>", click)
c = Button(f,font="ar 30 ",text="5",borderwidth=5,padx=9,pady=10,justify="center",relief=SOLID,width=3,cursor="hand2",)
c.pack(side=LEFT, padx=10, pady=5)
c.bind("<Button-1>", click)
c = Button(f,font="ar 30 ",text="6",borderwidth=5,padx=9,pady=10,justify="center",relief=SOLID,width=3,cursor="hand2")
c.pack(side=LEFT, padx=10, pady=5)
c.bind("<Button-1>", click)
c = Button(f,font="ar 30 ",text="-",borderwidth=5,padx=9,pady=10,justify="center",relief=SOLID,width=3,cursor="hand2")
c.pack(side=LEFT, padx=10, pady=5)
c.bind("<Button-1>", click)
f.pack()


#####################################BUTTTONS+FRAMES################################################


f = Frame(root, bg="#FF5733")
d = Button(
    f,
    font="ar 30 ",
    text="1",
    borderwidth=5,
    padx=10,
    pady=10,
    justify="center",
    relief=SOLID,
    width=3,
    cursor="hand2",
)
d.pack(side=LEFT, padx=10, pady=5)
d.bind("<Button-1>", click)
d = Button(
    f,
    font="ar 30 ",
    text="2",
    borderwidth=5,
    padx=10,
    pady=10,
    justify="center",
    relief=SOLID,
    width=3,
    cursor="hand2",
)
d.pack(side=LEFT, padx=10, pady=5)
d.bind("<Button-1>", click)
d = Button(
    f,
    font="ar 30 ",
    text="3",
    borderwidth=5,
    padx=10,
    pady=10,
    justify="center",
    relief=SOLID,
    width=3,
    cursor="hand2",
)
d.pack(side=LEFT, padx=10, pady=5)
d.bind("<Button-1>", click)
d = Button(
    f,
    font="ar 30 ",
    text="+",
    borderwidth=5,
    padx=10,
    pady=10,
    justify="center",
    relief=SOLID,
    width=3,
    cursor="hand2",
)
d.pack(side=LEFT, padx=10, pady=5)
d.bind("<Button-1>", click)
f.pack()

f = Frame(root, bg="#FF5733")
e = Button(
    f,
    font="ar 30 ",
    text="%",
    borderwidth=5,
    padx=10,
    pady=10,
    justify="center",
    relief=SOLID,
    width=3,
    cursor="hand2",
)
e.pack(side=LEFT, padx=10, pady=5)
e.bind("<Button-1>", click)
e = Button(
    f,
    font="ar 30 ",
    text="0",
    borderwidth=5,
    padx=10,
    pady=10,
    justify="center",
    relief=SOLID,
    width=3,
    cursor="hand2",
)
e.pack(side=LEFT, padx=10, pady=5)
e.bind("<Button-1>", click)
e = Button(
    f,
    font="ar 30 ",
    text=".",
    borderwidth=5,
    padx=10,
    pady=10,
    justify="center",
    relief=SOLID,
    width=3,
    cursor="hand2",
)
e.pack(side=LEFT, padx=10, pady=5)
e.bind("<Button-1>", click)
e = Button(
    f,
    font="ar 30 ",
    text="=",
    borderwidth=5,
    padx=10,
    pady=10,
    justify="center",
    relief=SOLID,
    width=3,
    cursor="hand2",
)
e.pack(side=LEFT, padx=10, pady=5)
e.bind("<Button-1>", click)
f.pack()
Label(text="Muhammad Hasnat Rasool", fg="green", font="ar 15 bold", pady=5).pack(
    side="bottom", anchor="s", fill=X, pady=1
)
root.config(bg="#333333")
#####################################END OF BUTTONS + FRAMES################################################
root.mainloop()
#####################################END OF SIMPLE GUI CALCULATOR APP################################################
#####################################################################################
#####################################################################################
#####################################################################################
# This code is a simple start feel free to expand and make a best possible calculator , 
#                   possibilities are endless!
#####################################-END-################################################
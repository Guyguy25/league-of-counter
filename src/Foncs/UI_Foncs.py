# === UI Modules ===
from tkinter import *
from tkinter import ttk
import tkinter.font as tkFont
from PIL import Image, ImageTk
import io
# ==================

# === Back Modules ===
import urllib.request
import requests # ?
# ====================


def modify(root, TK_Label_Level, TK_Label_Pseudo, TK_Label_PFP, Player_Name, Player_icon, Data_Level, Tk_Menu_Region, Tk_Entry, TK_Label_RankSolo, TK_Label_RankFlex, Tk_Label_Icon):
    root.title(f"{Player_Name} - Stats")
    root.geometry('450x400')
    root.configure(bg="#88A290")

    Tk_Label_Icon.destroy()
    Tk_Entry.delete(0, 'end')

    if Data_Level < 10:
        TK_Label_Level["text"]=Data_Level
        TK_Label_Level.place(x=69, y=73)
        TK_Label_Level.config(background="#f25f25", foreground="#fff")
    else:
        TK_Label_Level["text"]=Data_Level
        TK_Label_Level.place(x=64, y=73)
        TK_Label_Level.config(background="#f25f25", foreground="#fff")

    if Data_Level >= 100:
        TK_Label_Level["text"]=Data_Level
        TK_Label_Level.place(x=59, y=73)
        TK_Label_Level.config(background="#f25f25", foreground="#fff")

    if Data_Level >= 1000:
        TK_Label_Level["text"]=Data_Level
        TK_Label_Level.place(x=53, y=73)
        TK_Label_Level.config(background="#f25f25", foreground="#fff")

    TK_Label_Pseudo["text"]=Player_Name
    TK_Label_Pseudo.place(x=125, y=105)

    raw_data = urllib.request.urlopen(Player_icon).read()

    im = Image.open(io.BytesIO(raw_data)).resize((80,80))
    im = ImageTk.PhotoImage(im)

    TK_Label_PFP["image"] = im
    TK_Label_PFP.image = im
    TK_Label_PFP.place(x=35, y=100)
    TK_Label_PFP.config(background="#f25f25")

    Tk_Menu_Region.place(x=175, y=22)
    Tk_Entry.place(x=50, y=22)

    TK_Label_RankSolo["text"]= "Ranked Solo"
    TK_Label_RankSolo.place(x=10, y=200)
    TK_Label_RankFlex["text"]= "Ranked flex"
    TK_Label_RankFlex.place(x=10, y=280)
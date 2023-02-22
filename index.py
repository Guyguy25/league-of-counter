from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from src.Foncs.back_Foncs import api

root = Tk()
root.geometry('400x500')
root.resizable(0, 0)

root.title('League Of Counter')
root.iconbitmap('src/ico/icon.ico')
root.configure(bg="gray")
root.tk.call('tk::PlaceWindow', root , 'center')

level = ttk.Label(root, text="", font=("Roboto", 15))
pseudo = ttk.Label(root, text="", font="Helvetica 18 bold")
pseudo.config(background="#88A290")
labelPDP = ttk.Label(root, text="")

rankSolo = ttk.Label(root, text="")
rankSolo.config(background="#88A290")
tier_rank_solo = ttk.Label(root, text="", font="Helvetica 10 bold")
tier_rank_solo.config(background="#88A290")
lp_solo = ttk.Label(root, text="", font="Helvetica 8")
lp_solo.config(background="#88A290")
win_loose_solo = ttk.Label(root, text="")
win_loose_solo.config(background="#88A290")
winrate_solo = ttk.Label(root, text="")
winrate_solo.config(background="#88A290")

rankFlex = ttk.Label(root, text="")
rankFlex.config(background="#88A290")
tier_rank_flex = ttk.Label(root, text="", font="Helvetica 10 bold")
tier_rank_flex.config(background="#88A290")
lp_flex = ttk.Label(root, text="", font="Helvetica 8")
lp_flex.config(background="#88A290")
win_loose_flex = ttk.Label(root, text="")
win_loose_flex.config(background="#88A290")
winrate_flex = ttk.Label(root, text="")
winrate_flex.config(background="#88A290")

icon1_display = ImageTk.PhotoImage(Image.open("src/ico/icon.ico").resize((90,90)))
labelIcon = ttk.Label(image=icon1_display, background="gray")
labelIcon.place(x=150, y=20)

champions = ttk.Label(root, text="")
champions.config(background="#88A290")

champion_name1 = ttk.Label(root, text="")
champion_name1.config(background="#88A290")
champion_name2 = ttk.Label(root, text="")
champion_name2.config(background="#88A290")
champion_name3 = ttk.Label(root, text="")
champion_name3.config(background="#88A290")
champion_name4 = ttk.Label(root, text="")
champion_name4.config(background="#88A290")
champion_name5 = ttk.Label(root, text="")
champion_name5.config(background="#88A290")

champion_mastery1 = ttk.Label(root, text="")
champion_mastery1.config(background="#88A290")
champion_mastery2 = ttk.Label(root, text="")
champion_mastery2.config(background="#88A290")
champion_mastery3 = ttk.Label(root, text="")
champion_mastery3.config(background="#88A290")
champion_mastery4 = ttk.Label(root, text="")
champion_mastery4.config(background="#88A290")
champion_mastery5 = ttk.Label(root, text="")
champion_mastery5.config(background="#88A290")

champion_mastery_points1 = ttk.Label(root, text="")
champion_mastery_points1.config(background="#88A290")
champion_mastery_points2 = ttk.Label(root, text="")
champion_mastery_points2.config(background="#88A290")
champion_mastery_points3 = ttk.Label(root, text="")
champion_mastery_points3.config(background="#88A290")
champion_mastery_points4 = ttk.Label(root, text="")
champion_mastery_points4.config(background="#88A290")
champion_mastery_points5 = ttk.Label(root, text="")
champion_mastery_points5.config(background="#88A290")

liste_region = ["BR1", "EUN1", "EUW1", "JP1", "KR", "LA1", "LA2", "NA1", "OC1", "RU", "TR1"]
menu_region = ttk.Combobox(root, values=liste_region)
menu_region.current(0)
menu_region.config(width=5)
menu_region.place(x=245, y=225)
menu_region.bind("<<ComboboxSelected>>", lambda event: api(root=root, Tk_Entry=entry, TK_Label_Level=level, TK_Label_Pseudo=pseudo, TK_Label_PFP=labelPDP, TK_Label_RankSolo=rankSolo, TK_Label_RankFlex=rankFlex, Tk_Menu_Region=menu_region, Tk_Label_lp_flex=lp_flex, Tk_Label_lp_solo=lp_solo, TK_Label_Tier_Rankflex=tier_rank_flex, TK_Label_Tier_Ranksolo=tier_rank_solo, Tk_Label_Icon=labelIcon, Tk_Label_win_loose_flex=win_loose_flex, Tk_Label_win_loose_solo=win_loose_solo, Tk_Label_winrate_flex=winrate_flex, Tk_Label_winrate_solo=winrate_solo, TK_Champion_Name1=champion_name1, TK_Champion_Name2=champion_name2, TK_Champion_Name3=champion_name3, TK_Champion_Name4=champion_name4, TK_Champion_Name5=champion_name5, TK_Champion_Mastery1=champion_mastery1, TK_Champion_Mastery2=champion_mastery2, TK_Champion_Mastery3=champion_mastery3, TK_Champion_Mastery4=champion_mastery4, TK_Champion_Mastery5=champion_mastery5, TK_Champion_Points1=champion_mastery_points1, TK_Champion_Points2=champion_mastery_points2, TK_Champion_Points3=champion_mastery_points3, TK_Champion_Points4=champion_mastery_points4, TK_Champion_Points5=champion_mastery_points5))

entry = ttk.Entry(root)
entry.insert(0, 'Username')
entry.place(x=120, y=225)
entry.bind("<FocusIn>", lambda args: entry.delete(0, 'end'))
entry.bind('<Return>', lambda event: api(root=root, Tk_Entry=entry, TK_Label_Level=level, TK_Label_Pseudo=pseudo, TK_Label_PFP=labelPDP, TK_Label_RankSolo=rankSolo, TK_Label_RankFlex=rankFlex, Tk_Menu_Region=menu_region, Tk_Label_lp_flex=lp_flex, Tk_Label_lp_solo=lp_solo, TK_Label_Tier_Rankflex=tier_rank_flex, TK_Label_Tier_Ranksolo=tier_rank_solo, Tk_Label_Icon=labelIcon, Tk_Label_win_loose_flex=win_loose_flex, Tk_Label_win_loose_solo=win_loose_solo, Tk_Label_winrate_flex=winrate_flex, Tk_Label_winrate_solo=winrate_solo, TK_Champion_Name1=champion_name1, TK_Champion_Name2=champion_name2, TK_Champion_Name3=champion_name3, TK_Champion_Name4=champion_name4, TK_Champion_Name5=champion_name5, TK_Champion_Mastery1=champion_mastery1, TK_Champion_Mastery2=champion_mastery2, TK_Champion_Mastery3=champion_mastery3, TK_Champion_Mastery4=champion_mastery4, TK_Champion_Mastery5=champion_mastery5, TK_Champion_Points1=champion_mastery_points1, TK_Champion_Points2=champion_mastery_points2, TK_Champion_Points3=champion_mastery_points3, TK_Champion_Points4=champion_mastery_points4, TK_Champion_Points5=champion_mastery_points5))

credits = ttk.Label(root, text="Create by Guyguy25 (v0.1)", background="gray")
credits.place(x=10, y=470)

root.mainloop()
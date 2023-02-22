# === UI Modules ===
from tkinter import *
from tkinter import messagebox
# ==================

# === Back Modules ===
import requests
import json
# ====================

# === Functions ===
from src.Foncs.UI_Foncs import modify
# =================

def api(root, TK_Label_Level, TK_Label_Pseudo, TK_Label_PFP, Tk_Entry, TK_Label_RankSolo, TK_Label_RankFlex, Tk_Menu_Region, Tk_Label_lp_flex, Tk_Label_lp_solo, TK_Label_Tier_Ranksolo, TK_Label_Tier_Rankflex, Tk_Label_Icon, Tk_Label_win_loose_solo, Tk_Label_win_loose_flex, Tk_Label_winrate_solo, Tk_Label_winrate_flex, TK_Champion_Name1, TK_Champion_Name2, TK_Champion_Name3, TK_Champion_Name4, TK_Champion_Name5, TK_Champion_Mastery1, TK_Champion_Mastery2, TK_Champion_Mastery3, TK_Champion_Mastery4, TK_Champion_Mastery5, TK_Champion_Points1, TK_Champion_Points2, TK_Champion_Points3, TK_Champion_Points4, TK_Champion_Points5):
        
    select_region = Tk_Menu_Region.get()

    entryURL = Tk_Entry.get()
    Tk_Entry.delete(0, 'end')

    jsonFile = json.load(open("src/json/config.json"))
    api_url = f"https://{select_region}.api.riotgames.com/lol/summoner/v4/summoners/by-name/{entryURL}?api_key={jsonFile['api']['key']}"
    resp = requests.get(api_url)
    player_info = resp.json()
    
    try:
        encryptedSummonerId = player_info['id']
    except(KeyError):
        messagebox.showerror("Error: EmptyInput", "Nom d'utilisateur introuvable")
    player_icoId = player_info['profileIconId']
    player_level = player_info['summonerLevel']
    player_name = player_info['name']

    api_url_user_stats = f"https://{select_region}.api.riotgames.com/lol/league/v4/entries/by-summoner/{encryptedSummonerId}?api_key={jsonFile['api']['key']}"
    resp1 = requests.get(api_url_user_stats)
    player_info_stats = resp1.json()

    api_user_mastery = f"https://{select_region}.api.riotgames.com/lol/champion-mastery/v4/champion-masteries/by-summoner/{encryptedSummonerId}?api_key={jsonFile['api']['key']}"
    resp2 = requests.get(api_user_mastery)
    player_mastery = resp2.json()

    Tk_Label_lp_flex["text"]= ""
    Tk_Label_lp_solo["text"]= ""

    TK_Label_Tier_Ranksolo["text"]= "Non classé(e)"
    TK_Label_Tier_Ranksolo["font"]= ""
    TK_Label_Tier_Ranksolo.place(x=30, y=225)

    TK_Label_Tier_Rankflex["text"]= "Non classé(e)"
    TK_Label_Tier_Rankflex["font"]= ""
    TK_Label_Tier_Rankflex.place(x=30, y=305)

    Tk_Label_win_loose_solo["text"]=""
    Tk_Label_win_loose_solo.place(x=110, y=225)

    Tk_Label_winrate_solo["text"]= ""
    Tk_Label_winrate_solo.place(x=110, y=240)

    Tk_Label_win_loose_flex["text"]=""
    Tk_Label_win_loose_solo.place(x=110, y=225)

    Tk_Label_winrate_flex["text"]= ""
    Tk_Label_winrate_solo.place(x=110, y=240)

    if len(player_info_stats) == 0:
        Tk_Label_lp_flex["text"]= ""
        Tk_Label_lp_solo["text"]= ""

        TK_Label_Tier_Ranksolo["text"]= "Non classé(e)"
        TK_Label_Tier_Ranksolo.place(x=30, y=225)

        TK_Label_Tier_Rankflex["text"]= "Non classé(e)"
        TK_Label_Tier_Rankflex["font"]= ""
        TK_Label_Tier_Rankflex.place(x=30, y=305)

        Tk_Label_win_loose_solo["text"]= ""
        Tk_Label_winrate_solo["text"]= ""
        Tk_Label_win_loose_flex["text"]= ""
        Tk_Label_winrate_flex["text"]= ""
    else:
        for player_infos_stats in player_info_stats:

            if 'RANKED_FLEX_SR' in player_infos_stats['queueType']:

                if player_infos_stats["queueType"] == 'RANKED_FLEX_SR':
                    tier = player_infos_stats["tier"]
                    rank = player_infos_stats['rank']
                    lp = player_infos_stats["leaguePoints"]
                    win = player_infos_stats["wins"]
                    loose = player_infos_stats["losses"]

                    TK_Label_Tier_Rankflex["text"]=f"{tier} {rank}"
                    TK_Label_Tier_Rankflex["font"]= "Helvetica 10 bold"
                    TK_Label_Tier_Rankflex.place(x=30, y=305)

                    Tk_Label_lp_flex["text"]= f"{lp} LP"
                    Tk_Label_lp_flex.place(x=30, y=320)

                    Tk_Label_win_loose_flex["text"]=f"{win}W {loose}L"
                    Tk_Label_win_loose_flex.place(x=120, y=305)
                    Tk_Label_winrate_flex["text"]= f"{round(int(win / (win + loose) * 100))} %"
                    Tk_Label_winrate_flex.place(x=120, y=320)

            if 'RANKED_SOLO_5x5' in player_infos_stats['queueType']:
                if player_infos_stats['queueType'] == 'RANKED_SOLO_5x5':
                    tier = player_infos_stats['tier']
                    rank = player_infos_stats['rank']
                    lp = player_infos_stats["leaguePoints"]
                    win = player_infos_stats["wins"]
                    loose = player_infos_stats["losses"]

                    TK_Label_Tier_Ranksolo["text"]=f"{tier} {rank}"
                    TK_Label_Tier_Ranksolo["font"]= "Helvetica 10 bold"
                    TK_Label_Tier_Ranksolo.place(x=30, y=225)

                    Tk_Label_lp_solo["text"]= f"{lp} LP"
                    Tk_Label_lp_solo.place(x=30, y=240)

                    Tk_Label_win_loose_solo["text"]=f"{win}W {loose}L"
                    Tk_Label_win_loose_solo.place(x=120, y=225)
                    Tk_Label_winrate_solo["text"]= f"{round(int(win / (win + loose) * 100))} %"
                    Tk_Label_winrate_solo.place(x=120, y=240)

    if len(player_mastery) >= 5:
        liste = [(champion["championId"], champion["championLevel"], champion["championPoints"]) for champion in player_mastery[:5]]

        TK_Champion_Name1["text"] = jsonFile['api']['id_champ'][str(liste[0][0])]
        TK_Champion_Name1.place(x=200, y=215)
        TK_Champion_Name2["text"] = jsonFile['api']['id_champ'][str(liste[1][0])]
        TK_Champion_Name2.place(x=200, y=230)
        TK_Champion_Name3["text"] = jsonFile['api']['id_champ'][str(liste[2][0])]
        TK_Champion_Name3.place(x=200, y=245)
        TK_Champion_Name4["text"] = jsonFile['api']['id_champ'][str(liste[3][0])]
        TK_Champion_Name4.place(x=200, y=260)
        TK_Champion_Name5["text"] = jsonFile['api']['id_champ'][str(liste[4][0])]
        TK_Champion_Name5.place(x=200, y=275)

        TK_Champion_Mastery1["text"] = "Mastery." + str(liste[0][1])
        TK_Champion_Mastery1.place(x=310, y=215)
        TK_Champion_Mastery2["text"] = "Mastery." + str(liste[1][1])
        TK_Champion_Mastery2.place(x=310, y=230)
        TK_Champion_Mastery3["text"] = "Mastery." + str(liste[2][1])
        TK_Champion_Mastery3.place(x=310, y=245)
        TK_Champion_Mastery4["text"] = "Mastery." + str(liste[3][1])
        TK_Champion_Mastery4.place(x=310, y=260)
        TK_Champion_Mastery5["text"] = "Mastery." + str(liste[4][1])
        TK_Champion_Mastery5.place(x=310, y=275)

        if liste[0][2] >= 1000000:
            value = "%.0f%s" % (liste[0][2]/1000000.00, 'M')
        else:
            if liste[0][2] >= 1000:
                value = "%.0f%s" % (liste[0][2]/1000.0, 'k')

        if liste[1][2] >= 1000000:
            value1 = "%.0f%s" % (liste[1][2]/1000000.00, 'M')
        else:
            if liste[1][2] >= 1000:
                value1 = "%.0f%s" % (liste[1][2]/1000.0, 'k')

        if liste[2][2] >= 1000000:
            value2 = "%.0f%s" % (liste[2][2]/1000000.00, 'M')
        else:
            if liste[2][2] >= 1000:
                value2 = "%.0f%s" % (liste[2][2]/1000.0, 'k')
        
        if liste[3][2] >= 1000000:
            value3 = "%.0f%s" % (liste[3][2]/1000000.00, 'M')
        else:
            if liste[3][2] >= 1000:
                value3 = "%.0f%s" % (liste[3][2]/1000.0, 'k')

        if liste[4][2] >= 1000000:
            value4 = "%.0f%s" % (liste[4][2]/1000000.00, 'M')
        else:
            if liste[4][2] >= 1000:
                value4 = "%.0f%s" % (liste[4][2]/1000.0, 'k')

        TK_Champion_Points1["text"] = value
        TK_Champion_Points1.place(x=380, y=215)
        TK_Champion_Points2["text"] = value1
        TK_Champion_Points2.place(x=380, y=230)
        TK_Champion_Points3["text"] = value2
        TK_Champion_Points3.place(x=380, y=245)
        TK_Champion_Points4["text"] = value3
        TK_Champion_Points4.place(x=380, y=260)
        TK_Champion_Points5["text"] = value4
        TK_Champion_Points5.place(x=380, y=275)

    elif len(player_mastery) == 0:
        TK_Champion_Name1["text"] = ""
        TK_Champion_Name2["text"] = ""
        TK_Champion_Name3["text"] = ""
        TK_Champion_Name4["text"] = ""
        TK_Champion_Name5["text"] = ""
        TK_Champion_Mastery1["text"] = ""
        TK_Champion_Mastery2["text"] = ""
        TK_Champion_Mastery3["text"] = ""
        TK_Champion_Mastery4["text"] = ""
        TK_Champion_Mastery5["text"] = ""
        TK_Champion_Points1["text"] = ""
        TK_Champion_Points2["text"] = ""
        TK_Champion_Points3["text"] = ""
        TK_Champion_Points4["text"] = ""
        TK_Champion_Points5["text"] = ""

    else:
        for i in liste:
            print(jsonFile['api']['id_champ'][str(i[0])])
            print(str(i[1]))
            print(str(i[2]))
        
    ico_player = f"https://static.u.gg/assets/lol/riot_static/12.23.1/img/profileicon/{player_icoId}.png"

    modify(root=root, TK_Label_Level=TK_Label_Level, TK_Label_Pseudo=TK_Label_Pseudo, TK_Label_PFP=TK_Label_PFP, Player_Name=player_name, Player_icon=ico_player, Data_Level=player_level, Tk_Menu_Region=Tk_Menu_Region, Tk_Entry=Tk_Entry, TK_Label_RankSolo=TK_Label_RankSolo, TK_Label_RankFlex=TK_Label_RankFlex, Tk_Label_Icon=Tk_Label_Icon)
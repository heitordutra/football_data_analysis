# %%
import requests
import json
import pandas as pd
from datetime import date
from PIL import Image
import openpyxl
from mplsoccer.pitch import Pitch, VerticalPitch
from collections.abc import KeysView
import warnings
warnings.filterwarnings("ignore")

# %%
team_id = 1968
last_10_matches = "https://www.sofascore.com/api/v1/team/"+str(team_id)+"/performance"

headers = {
  "Accept":"*/*" ,
  "Accept-Language":"en-US,en;q=0.9,pt;q=0.8,fr;q=0.7,pt-BR;q=0.6,pt-PT;q=0.5",
  "Cache-Control":"max-age=0",
  "Connection":"keep-alive",
  "Cookie":"_scid=a2c64644-8845-4c87-a02d-10300efe6317; _ga=GA1.1.1480352166.1694613292; _uc_referrer=https://www.sofascore.com/pt/; _tt_enable_cookie=1; _ttp=UKKbqjh7Fg57k9kijgFu-n1uvDt; _scid_r=a2c64644-8845-4c87-a02d-10300efe6317; _gcl_au=1.1.1302485585.1714668818; _ga_QH2YGS7BB4=GS1.1.1714668820.3.1.1714670868.0.0.0; _ga_3KF4XTPHC4=GS1.1.1714668820.2.1.1714670868.60.0.0; _ga_HNQ9P9MGZR=GS1.1.1714668825.3.1.1714670868.60.0.0" ,
  "DNT":"1" ,
  "If-None-Match":"W/^\^1cee2d0260^\^'^",
  #"Referer":referer,
  "Referer": "https://www.sofascore.com/",
  "Sec-Fetch-Dest":"empty" ,
  "Sec-Fetch-Mode":"cors" ,
  "Sec-Fetch-Site":"same-origin" ,
  "User-Agent":"Mozilla/5.0 (Windows NT 10.0, Win64, x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36 Edg/124.0.0.0",
  "X-Requested-With":"2060c8" ,
  "sec-ch-ua": "^\^'Chromium^\^';v=^\^'124^\^', ^\^'Microsoft Edge^\^';v=^\^'124^\^', ^\^'Not-A.Brand^\^';v=^\^'99^\^'^'",
  "sec-ch-ua-mobile": "?0" ,
  "sec-ch-ua-platform": "^\^'Windows^\^'^",
}

r = requests.get(last_10_matches, headers=headers,verify=False)
data = r.json()
df = pd.json_normalize(data['events']).transpose()

# %%
for i in range(10):
    print(f"{(i+1):02d}: {date.fromtimestamp(df[i]['startTimestamp']).strftime("%d/%m/%Y")} - {df[i]['season.name']} | {df[i]['homeTeam.name']} {df[i]['homeScore.current']}x{df[i]['awayScore.current']} {df[i]['awayTeam.name']}")

# %%
def request_to_df(url: str,section: str,sub_section1="",sub_section2="",sub_section3="",sub_section4="",sub_section5=""):
    '''
    Receives the url and return as a Pandas DF
    '''
    a = requests.get(url, headers=headers,verify=False).json()
    if sub_section5 != "":
        df = pd.json_normalize(a[section][sub_section1][sub_section2][sub_section3][sub_section4][sub_section5])
    elif sub_section4 != "":
        df = pd.json_normalize(a[section][sub_section1][sub_section2][sub_section3][sub_section4])
    elif sub_section3 != "":
        df = pd.json_normalize(a[section][sub_section1][sub_section2][sub_section3])
    elif sub_section2 != "":
        df = pd.json_normalize(a[section][sub_section1][sub_section2])
    elif sub_section1 != "":
        df = pd.json_normalize(a[section][sub_section1])
    else:
        df = pd.json_normalize(a[section])
    return df
# %%
def request_keys(url: str,section="",sub_section=""):
    '''
    Receives the url and return the json keys
    '''
    a = requests.get(url, headers=headers,verify=False).json()
    if section != "":
        if sub_section!="":
            if type(a[section][sub_section])!=list:
                a = a[section][sub_section]
            else:
                print("This is already JSON's last level")
                return 
        if a[section].keys()==list:
            print("This is already JSON's last level1")
        else:
            a = a[section]
    for key in a.keys():
        print(key)
    return a
# %%
last_match_url = "https://www.sofascore.com/api/v1/event/" + str(df[9]['id'])

statistics_url = last_match_url + "/statistics"
lineups_url = last_match_url + "/lineups"
managers_url = last_match_url + "/managers"
avg_positions_url = last_match_url + "/average-positions"
shotmap_url = last_match_url + "/shotmap"
graph_url = last_match_url + "/graph"
next_event_url = "https://www.sofascore.com/api/v1/team/"+str(team_id)+"/events/next/0"
last_event_url = "https://www.sofascore.com/api/v1/team/"+str(team_id)+"/events/last/0"
win_probability_url = last_match_url + "/provider/1/winning-odds"
team_streaks_url = last_match_url + "/team-streaks"
pre_game_form_url = last_match_url + "/pregame-form"
best_players_url = last_match_url + "/best-players/summary"
incidents_url = last_match_url + "/incidents"
# %%
statistics_df = pd.DataFrame()
statistics_requests = requests.get(statistics_url, headers=headers,verify=False).json()
for i in range(len(statistics_requests['statistics'][0]['groups'])):
    statistics_df = pd.concat([df,(request_to_df(statistics_url,'statistics',0,"groups",i,"statisticsItems",0))],ignore_index=True)
# %%
r = requests.get(avg_positions_url, headers=headers,verify=False).json()
r1 = requests.get(lineups_url, headers=headers,verify=False).json()

# %%
home_avg_positions_df = pd.json_normalize(r['home'])
home_lineup_df = pd.json_normalize(r1['home']['players'])
home_starting_lineup_df = home_lineup_df[home_lineup_df['substitute']==False]
home_starting11_avg_positions_df = home_avg_positions_df[home_avg_positions_df['player.id'].isin(home_starting_lineup_df['player.id'])]
away_avg_positions_df = pd.json_normalize(r['away'])

# %%

df_test = home_starting11_avg_positions_df.copy().reset_index()
df_test['averageX'] = df_test['averageX']*105/100
df_test['averageY'] = df_test['averageY']*68/100
pitch2 = Pitch(pitch_type='custom',pitch_color='grass',pitch_length=105, pitch_width=68,goal_type='box',line_color='white',stripe=True)
fig, ax = pitch2.draw()
ax_text = pitch2.scatter(df_test['averageX'],df_test['averageY'],ax=ax,s=500,c='#ffffff', ec='#000000',linewidth=3)
# plot the jersey numbers
for i, label in enumerate(df_test['player.jerseyNumber']):
    pitch2.annotate(label, (df_test['averageX'][i],df_test['averageY'][i]),
                   va='center', ha='center', color='black', fontsize=12, ax=ax)
# %%

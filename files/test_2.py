# %%
import requests
import json
import pandas as pd
from datetime import date
from PIL import Image

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

urls = [statistics_url,lineups_url,managers_url,avg_positions_url,shotmap_url,graph_url,next_event_url,last_event_url,win_probability_url,team_streaks_url,pre_game_form_url,best_players_url,incidents_url]

r = {}
for i in range(len(urls)):
    r[i] = requests.get(urls[i], headers=headers,verify=False).json()
for i in range(len(r)):
    print(r[i])

r[0]['statistics'][0]['groups'][0]
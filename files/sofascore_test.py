# %%
import requests
import json
import pandas as pd
from datetime import date
# %%
today = date.today()
#sofascore_link = "https://www.sofascore.com/avai-santos/tOspWc#id:12146215"
sofascore_match_link = "https://www.sofascore.com/paysandu-santos/tOsXO#id:12146204"
sofascore_api_link = "https://api.sofascore.app/api/v1/"
matchId = sofascore_match_link.split('#id:')[1]
referer = sofascore_match_link.split('#')[0]
match_name = sofascore_match_link.split('/')[3]

# %%
#url = (f"https://www.sofascore.com/api/v1/event/12146215")
general_info = "https://www.sofascore.com/api/v1/event/" + matchId
#url3= (f"{url3}")
payload = {}
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

statistics_url = general_info + "/statistics"
lineups_url = general_info + "/lineups"
managers_url = general_info + "/managers"
avg_positions_url = general_info + "/average-positions"
shotmap_url = general_info + "/shotmap"
graph_url = general_info + "/graph"
next_event_url = "https://www.sofascore.com/api/v1/team/1968/events/next/0"
last_event_url = "https://www.sofascore.com/api/v1/team/1968/events/last/0"
win_probability_url = general_info + "/win-probability"
team_streaks_url = general_info + "/team-streaks"
pre_game_form_url = general_info + "/pregame-form"
best_players_url = general_info + "best-players/summary"
incidents_url = general_info + "/incidents"
graph_win_probability = general_info + "/graph/win-probability"
comments_url = general_info + "/comments"


# %%
r = requests.get(general_info, headers=headers,verify=False)
r2 = requests.get(statistics_url, headers=headers,verify=False)
# %%
data = r.json()
data2 = r2.json()
# %%
tournament_name = data['event']['tournament']
home_team_name = data['event']['homeTeam']['name']
home_team_id = data['event']['homeTeam']['id']
away_team_name = data['event']['awayTeam']['name']

# %% Images
manager_image_url = "https://api.sofascore.app/api/v1/manager/784883/image"
away_player_jersey_image_url = "https://api.sofascore.app/api/v1/event/12146204/jersey/away/player/fancy"
away_gk_jersey_image_url = "https://api.sofascore.app/api/v1/event/12146204/jersey/away/goalkeeper/fancy" 
home_player_jersey_image = "https://api.sofascore.app/api/v1/event/12146204/jersey/home/player/fancy"
player_image_url = "https://api.sofascore.app/api/v1/player/795177/image"
team_image_url = sofascore_api_link + f"/team/{home_team_id}/image"
# %%
df = pd.json_normalize(data['event']).transpose()
# %%
df.to_csv(f'../export/sofascore_{match_name}.csv', index=True,encoding="utf-8-sig")
'''
curl "https://www.sofascore.com/api/v1/team/1968/performance" ^
  -H "Accept: */*" ^
  -H "Accept-Language: en-US,en;q=0.9,pt;q=0.8,fr;q=0.7,pt-BR;q=0.6,pt-PT;q=0.5" ^
  -H "Cache-Control: max-age=0" ^
  -H "Connection: keep-alive" ^
  -H "Cookie: _scid=a2c64644-8845-4c87-a02d-10300efe6317; _ga=GA1.1.1480352166.1694613292; _uc_referrer=https://www.sofascore.com/pt/; _tt_enable_cookie=1; _ttp=UKKbqjh7Fg57k9kijgFu-n1uvDt; _scid_r=a2c64644-8845-4c87-a02d-10300efe6317; _gcl_au=1.1.1302485585.1714668818; _ga_HNQ9P9MGZR=GS1.1.1714992194.5.1.1714992223.31.0.0; _ga_3KF4XTPHC4=GS1.1.1714992194.4.1.1714992226.28.0.0; _ga_QH2YGS7BB4=GS1.1.1714992194.5.1.1714992226.0.0.0" ^
  -H "DNT: 1" ^
  -H ^"If-None-Match: W/^\^"a0b5334fb1^\^"^" ^
  -H "Referer: https://www.sofascore.com/team/football/santos/1968" ^
  -H "Sec-Fetch-Dest: empty" ^
  -H "Sec-Fetch-Mode: cors" ^
  -H "Sec-Fetch-Site: same-origin" ^
  -H "User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36 Edg/124.0.0.0" ^
  -H "X-Requested-With: 45e338" ^
  -H ^"sec-ch-ua: ^\^"Chromium^\^";v=^\^"124^\^", ^\^"Microsoft Edge^\^";v=^\^"124^\^", ^\^"Not-A.Brand^\^";v=^\^"99^\^"^" ^
  -H "sec-ch-ua-mobile: ?0" ^
  -H ^"sec-ch-ua-platform: ^\^"Windows^\^"^"
'''
'''
curl "https://api.sofascore.app/api/v1/team/1968/image" ^
  -H "Accept: image/avif,image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8" ^
  -H "Accept-Language: en-US,en;q=0.9,pt;q=0.8,fr;q=0.7,pt-BR;q=0.6,pt-PT;q=0.5" ^
  -H "Connection: keep-alive" ^
  -H "DNT: 1" ^
  -H "Referer: https://www.sofascore.com/" ^
  -H "Sec-Fetch-Dest: image" ^
  -H "Sec-Fetch-Mode: no-cors" ^
  -H "Sec-Fetch-Site: cross-site" ^
  -H "User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36 Edg/124.0.0.0" ^
  -H ^"sec-ch-ua: ^\^"Chromium^\^";v=^\^"124^\^", ^\^"Microsoft Edge^\^";v=^\^"124^\^", ^\^"Not-A.Brand^\^";v=^\^"99^\^"^" ^
  -H "sec-ch-ua-mobile: ?0" ^
  -H ^"sec-ch-ua-platform: ^\^"Windows^\^"^" &

curl "https://www.sofascore.com/api/v1/event/12146204/statistics" ^
  -X "HEAD" ^
  -H "Accept: */*" ^
  -H "Accept-Language: en-US,en;q=0.9,pt;q=0.8,fr;q=0.7,pt-BR;q=0.6,pt-PT;q=0.5" ^
  -H "Connection: keep-alive" ^
  -H "Cookie: _scid=a2c64644-8845-4c87-a02d-10300efe6317; _ga=GA1.1.1480352166.1694613292; _uc_referrer=https://www.sofascore.com/pt/; _tt_enable_cookie=1; _ttp=UKKbqjh7Fg57k9kijgFu-n1uvDt; _scid_r=a2c64644-8845-4c87-a02d-10300efe6317; _gcl_au=1.1.1302485585.1714668818; _ga_HNQ9P9MGZR=GS1.1.1714676694.4.1.1714678743.29.0.0; _ga_QH2YGS7BB4=GS1.1.1714676691.4.1.1714678743.0.0.0; _ga_3KF4XTPHC4=GS1.1.1714676691.3.1.1714678743.29.0.0" ^
  -H "DNT: 1" ^
  -H ^"If-None-Match: W/^\^"31a4ab4496^\^"^" ^
  -H "Referer: https://www.sofascore.com/paysandu-santos/tOsXO" ^
  -H "Sec-Fetch-Dest: empty" ^
  -H "Sec-Fetch-Mode: cors" ^
  -H "Sec-Fetch-Site: same-origin" ^
  -H "User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36 Edg/124.0.0.0" ^
  -H ^"sec-ch-ua: ^\^"Chromium^\^";v=^\^"124^\^", ^\^"Microsoft Edge^\^";v=^\^"124^\^", ^\^"Not-A.Brand^\^";v=^\^"99^\^"^" ^
  -H "sec-ch-ua-mobile: ?0" ^
  -H ^"sec-ch-ua-platform: ^\^"Windows^\^"^" &

curl "https://www.sofascore.com/api/v1/event/12146204/lineups" ^
  -X "HEAD" ^
  -H "Accept: */*" ^
  -H "Accept-Language: en-US,en;q=0.9,pt;q=0.8,fr;q=0.7,pt-BR;q=0.6,pt-PT;q=0.5" ^
  -H "Connection: keep-alive" ^
  -H "Cookie: _scid=a2c64644-8845-4c87-a02d-10300efe6317; _ga=GA1.1.1480352166.1694613292; _uc_referrer=https://www.sofascore.com/pt/; _tt_enable_cookie=1; _ttp=UKKbqjh7Fg57k9kijgFu-n1uvDt; _scid_r=a2c64644-8845-4c87-a02d-10300efe6317; _gcl_au=1.1.1302485585.1714668818; _ga_HNQ9P9MGZR=GS1.1.1714676694.4.1.1714678743.29.0.0; _ga_QH2YGS7BB4=GS1.1.1714676691.4.1.1714678743.0.0.0; _ga_3KF4XTPHC4=GS1.1.1714676691.3.1.1714678743.29.0.0" ^
  -H "DNT: 1" ^
  -H ^"If-None-Match: W/^\^"6ad9200976^\^"^" ^
  -H "Referer: https://www.sofascore.com/paysandu-santos/tOsXO" ^
  -H "Sec-Fetch-Dest: empty" ^
  -H "Sec-Fetch-Mode: cors" ^
  -H "Sec-Fetch-Site: same-origin" ^
  -H "User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36 Edg/124.0.0.0" ^
  -H ^"sec-ch-ua: ^\^"Chromium^\^";v=^\^"124^\^", ^\^"Microsoft Edge^\^";v=^\^"124^\^", ^\^"Not-A.Brand^\^";v=^\^"99^\^"^" ^
  -H "sec-ch-ua-mobile: ?0" ^
  -H ^"sec-ch-ua-platform: ^\^"Windows^\^"^" &

curl "https://www.sofascore.com/api/v1/event/12146204/comments" ^
  -X "HEAD" ^
  -H "Accept: */*" ^
  -H "Accept-Language: en-US,en;q=0.9,pt;q=0.8,fr;q=0.7,pt-BR;q=0.6,pt-PT;q=0.5" ^
  -H "Connection: keep-alive" ^
  -H "Cookie: _scid=a2c64644-8845-4c87-a02d-10300efe6317; _ga=GA1.1.1480352166.1694613292; _uc_referrer=https://www.sofascore.com/pt/; _tt_enable_cookie=1; _ttp=UKKbqjh7Fg57k9kijgFu-n1uvDt; _scid_r=a2c64644-8845-4c87-a02d-10300efe6317; _gcl_au=1.1.1302485585.1714668818; _ga_HNQ9P9MGZR=GS1.1.1714676694.4.1.1714678743.29.0.0; _ga_QH2YGS7BB4=GS1.1.1714676691.4.1.1714678743.0.0.0; _ga_3KF4XTPHC4=GS1.1.1714676691.3.1.1714678743.29.0.0" ^
  -H "DNT: 1" ^
  -H "Referer: https://www.sofascore.com/paysandu-santos/tOsXO" ^
  -H "Sec-Fetch-Dest: empty" ^
  -H "Sec-Fetch-Mode: cors" ^
  -H "Sec-Fetch-Site: same-origin" ^
  -H "User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36 Edg/124.0.0.0" ^
  -H ^"sec-ch-ua: ^\^"Chromium^\^";v=^\^"124^\^", ^\^"Microsoft Edge^\^";v=^\^"124^\^", ^\^"Not-A.Brand^\^";v=^\^"99^\^"^" ^
  -H "sec-ch-ua-mobile: ?0" ^
  -H ^"sec-ch-ua-platform: ^\^"Windows^\^"^" &

curl "https://www.sofascore.com/api/v1/event/12146204/graph/win-probability" ^
  -X "HEAD" ^
  -H "Accept: */*" ^
  -H "Accept-Language: en-US,en;q=0.9,pt;q=0.8,fr;q=0.7,pt-BR;q=0.6,pt-PT;q=0.5" ^
  -H "Connection: keep-alive" ^
  -H "Cookie: _scid=a2c64644-8845-4c87-a02d-10300efe6317; _ga=GA1.1.1480352166.1694613292; _uc_referrer=https://www.sofascore.com/pt/; _tt_enable_cookie=1; _ttp=UKKbqjh7Fg57k9kijgFu-n1uvDt; _scid_r=a2c64644-8845-4c87-a02d-10300efe6317; _gcl_au=1.1.1302485585.1714668818; _ga_HNQ9P9MGZR=GS1.1.1714676694.4.1.1714678743.29.0.0; _ga_QH2YGS7BB4=GS1.1.1714676691.4.1.1714678743.0.0.0; _ga_3KF4XTPHC4=GS1.1.1714676691.3.1.1714678743.29.0.0" ^
  -H "DNT: 1" ^
  -H "Referer: https://www.sofascore.com/paysandu-santos/tOsXO" ^
  -H "Sec-Fetch-Dest: empty" ^
  -H "Sec-Fetch-Mode: cors" ^
  -H "Sec-Fetch-Site: same-origin" ^
  -H "User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36 Edg/124.0.0.0" ^
  -H ^"sec-ch-ua: ^\^"Chromium^\^";v=^\^"124^\^", ^\^"Microsoft Edge^\^";v=^\^"124^\^", ^\^"Not-A.Brand^\^";v=^\^"99^\^"^" ^
  -H "sec-ch-ua-mobile: ?0" ^
  -H ^"sec-ch-ua-platform: ^\^"Windows^\^"^" &

curl "https://www.sofascore.com/api/v1/event/12146204/incidents" ^
  -H "Accept: */*" ^
  -H "Accept-Language: en-US,en;q=0.9,pt;q=0.8,fr;q=0.7,pt-BR;q=0.6,pt-PT;q=0.5" ^
  -H "Cache-Control: max-age=0" ^
  -H "Connection: keep-alive" ^
  -H "Cookie: _scid=a2c64644-8845-4c87-a02d-10300efe6317; _ga=GA1.1.1480352166.1694613292; _uc_referrer=https://www.sofascore.com/pt/; _tt_enable_cookie=1; _ttp=UKKbqjh7Fg57k9kijgFu-n1uvDt; _scid_r=a2c64644-8845-4c87-a02d-10300efe6317; _gcl_au=1.1.1302485585.1714668818; _ga_HNQ9P9MGZR=GS1.1.1714676694.4.1.1714678743.29.0.0; _ga_QH2YGS7BB4=GS1.1.1714676691.4.1.1714678743.0.0.0; _ga_3KF4XTPHC4=GS1.1.1714676691.3.1.1714678743.29.0.0" ^
  -H "DNT: 1" ^
  -H ^"If-None-Match: W/^\^"998dabc86a^\^"^" ^
  -H "Referer: https://www.sofascore.com/paysandu-santos/tOsXO" ^
  -H "Sec-Fetch-Dest: empty" ^
  -H "Sec-Fetch-Mode: cors" ^
  -H "Sec-Fetch-Site: same-origin" ^
  -H "User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36 Edg/124.0.0.0" ^
  -H "X-Requested-With: 707da2" ^
  -H ^"sec-ch-ua: ^\^"Chromium^\^";v=^\^"124^\^", ^\^"Microsoft Edge^\^";v=^\^"124^\^", ^\^"Not-A.Brand^\^";v=^\^"99^\^"^" ^
  -H "sec-ch-ua-mobile: ?0" ^
  -H ^"sec-ch-ua-platform: ^\^"Windows^\^"^" &
curl "https://www.sofascore.com/api/v1/event/12146204/best-players/summary" ^
  -H "Accept: */*" ^
  -H "Accept-Language: en-US,en;q=0.9,pt;q=0.8,fr;q=0.7,pt-BR;q=0.6,pt-PT;q=0.5" ^
  -H "Cache-Control: max-age=0" ^
  -H "Connection: keep-alive" ^
  -H "Cookie: _scid=a2c64644-8845-4c87-a02d-10300efe6317; _ga=GA1.1.1480352166.1694613292; _uc_referrer=https://www.sofascore.com/pt/; _tt_enable_cookie=1; _ttp=UKKbqjh7Fg57k9kijgFu-n1uvDt; _scid_r=a2c64644-8845-4c87-a02d-10300efe6317; _gcl_au=1.1.1302485585.1714668818; _ga_HNQ9P9MGZR=GS1.1.1714676694.4.1.1714678743.29.0.0; _ga_QH2YGS7BB4=GS1.1.1714676691.4.1.1714678743.0.0.0; _ga_3KF4XTPHC4=GS1.1.1714676691.3.1.1714678743.29.0.0" ^
  -H "DNT: 1" ^
  -H ^"If-None-Match: W/^\^"a848a5f15f^\^"^" ^
  -H "Referer: https://www.sofascore.com/paysandu-santos/tOsXO" ^
  -H "Sec-Fetch-Dest: empty" ^
  -H "Sec-Fetch-Mode: cors" ^
  -H "Sec-Fetch-Site: same-origin" ^
  -H "User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36 Edg/124.0.0.0" ^
  -H "X-Requested-With: 707da2" ^
  -H ^"sec-ch-ua: ^\^"Chromium^\^";v=^\^"124^\^", ^\^"Microsoft Edge^\^";v=^\^"124^\^", ^\^"Not-A.Brand^\^";v=^\^"99^\^"^" ^
  -H "sec-ch-ua-mobile: ?0" ^
  -H ^"sec-ch-ua-platform: ^\^"Windows^\^"^" &
curl "https://www.sofascore.com/api/v1/event/12146204/pregame-form" ^
  -H "Accept: */*" ^
  -H "Accept-Language: en-US,en;q=0.9,pt;q=0.8,fr;q=0.7,pt-BR;q=0.6,pt-PT;q=0.5" ^
  -H "Cache-Control: max-age=0" ^
  -H "Connection: keep-alive" ^
  -H "Cookie: _scid=a2c64644-8845-4c87-a02d-10300efe6317; _ga=GA1.1.1480352166.1694613292; _uc_referrer=https://www.sofascore.com/pt/; _tt_enable_cookie=1; _ttp=UKKbqjh7Fg57k9kijgFu-n1uvDt; _scid_r=a2c64644-8845-4c87-a02d-10300efe6317; _gcl_au=1.1.1302485585.1714668818; _ga_HNQ9P9MGZR=GS1.1.1714676694.4.1.1714678743.29.0.0; _ga_QH2YGS7BB4=GS1.1.1714676691.4.1.1714678743.0.0.0; _ga_3KF4XTPHC4=GS1.1.1714676691.3.1.1714678743.29.0.0" ^
  -H "DNT: 1" ^
  -H "Referer: https://www.sofascore.com/paysandu-santos/tOsXO" ^
  -H "Sec-Fetch-Dest: empty" ^
  -H "Sec-Fetch-Mode: cors" ^
  -H "Sec-Fetch-Site: same-origin" ^
  -H "User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36 Edg/124.0.0.0" ^
  -H "X-Requested-With: 707da2" ^
  -H ^"sec-ch-ua: ^\^"Chromium^\^";v=^\^"124^\^", ^\^"Microsoft Edge^\^";v=^\^"124^\^", ^\^"Not-A.Brand^\^";v=^\^"99^\^"^" ^
  -H "sec-ch-ua-mobile: ?0" ^
  -H ^"sec-ch-ua-platform: ^\^"Windows^\^"^" &

curl "https://www.sofascore.com/api/v1/event/12146204/odds/1/featured" ^
  -H "Accept: */*" ^
  -H "Accept-Language: en-US,en;q=0.9,pt;q=0.8,fr;q=0.7,pt-BR;q=0.6,pt-PT;q=0.5" ^
  -H "Cache-Control: max-age=0" ^
  -H "Connection: keep-alive" ^
  -H "Cookie: _scid=a2c64644-8845-4c87-a02d-10300efe6317; _ga=GA1.1.1480352166.1694613292; _uc_referrer=https://www.sofascore.com/pt/; _tt_enable_cookie=1; _ttp=UKKbqjh7Fg57k9kijgFu-n1uvDt; _scid_r=a2c64644-8845-4c87-a02d-10300efe6317; _gcl_au=1.1.1302485585.1714668818; _ga_HNQ9P9MGZR=GS1.1.1714676694.4.1.1714678743.29.0.0; _ga_QH2YGS7BB4=GS1.1.1714676691.4.1.1714678743.0.0.0; _ga_3KF4XTPHC4=GS1.1.1714676691.3.1.1714678743.29.0.0" ^
  -H "DNT: 1" ^
  -H ^"If-None-Match: W/^\^"e8a5174920^\^"^" ^
  -H "Referer: https://www.sofascore.com/paysandu-santos/tOsXO" ^
  -H "Sec-Fetch-Dest: empty" ^
  -H "Sec-Fetch-Mode: cors" ^
  -H "Sec-Fetch-Site: same-origin" ^
  -H "User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36 Edg/124.0.0.0" ^
  -H "X-Requested-With: 707da2" ^
  -H ^"sec-ch-ua: ^\^"Chromium^\^";v=^\^"124^\^", ^\^"Microsoft Edge^\^";v=^\^"124^\^", ^\^"Not-A.Brand^\^";v=^\^"99^\^"^" ^
  -H "sec-ch-ua-mobile: ?0" ^
  -H ^"sec-ch-ua-platform: ^\^"Windows^\^"^" &

curl "https://www.sofascore.com/api/v1/event/12146204/highlights" ^
  -H "Accept: */*" ^
  -H "Accept-Language: en-US,en;q=0.9,pt;q=0.8,fr;q=0.7,pt-BR;q=0.6,pt-PT;q=0.5" ^
  -H "Cache-Control: max-age=0" ^
  -H "Connection: keep-alive" ^
  -H "Cookie: _scid=a2c64644-8845-4c87-a02d-10300efe6317; _ga=GA1.1.1480352166.1694613292; _uc_referrer=https://www.sofascore.com/pt/; _tt_enable_cookie=1; _ttp=UKKbqjh7Fg57k9kijgFu-n1uvDt; _scid_r=a2c64644-8845-4c87-a02d-10300efe6317; _gcl_au=1.1.1302485585.1714668818; _ga_HNQ9P9MGZR=GS1.1.1714676694.4.1.1714678743.29.0.0; _ga_QH2YGS7BB4=GS1.1.1714676691.4.1.1714678743.0.0.0; _ga_3KF4XTPHC4=GS1.1.1714676691.3.1.1714678743.29.0.0" ^
  -H "DNT: 1" ^
  -H ^"If-None-Match: W/^\^"e93efccc30^\^"^" ^
  -H "Referer: https://www.sofascore.com/paysandu-santos/tOsXO" ^
  -H "Sec-Fetch-Dest: empty" ^
  -H "Sec-Fetch-Mode: cors" ^
  -H "Sec-Fetch-Site: same-origin" ^
  -H "User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36 Edg/124.0.0.0" ^
  -H "X-Requested-With: 707da2" ^
  -H ^"sec-ch-ua: ^\^"Chromium^\^";v=^\^"124^\^", ^\^"Microsoft Edge^\^";v=^\^"124^\^", ^\^"Not-A.Brand^\^";v=^\^"99^\^"^" ^
  -H "sec-ch-ua-mobile: ?0" ^
  -H ^"sec-ch-ua-platform: ^\^"Windows^\^"^" &


curl "https://www.sofascore.com/api/v1/event/12146204/team-streaks" ^
  -H "Accept: */*" ^
  -H "Accept-Language: en-US,en;q=0.9,pt;q=0.8,fr;q=0.7,pt-BR;q=0.6,pt-PT;q=0.5" ^
  -H "Cache-Control: max-age=0" ^
  -H "Connection: keep-alive" ^
  -H "Cookie: _scid=a2c64644-8845-4c87-a02d-10300efe6317; _ga=GA1.1.1480352166.1694613292; _uc_referrer=https://www.sofascore.com/pt/; _tt_enable_cookie=1; _ttp=UKKbqjh7Fg57k9kijgFu-n1uvDt; _scid_r=a2c64644-8845-4c87-a02d-10300efe6317; _gcl_au=1.1.1302485585.1714668818; _ga_HNQ9P9MGZR=GS1.1.1714676694.4.1.1714678743.29.0.0; _ga_QH2YGS7BB4=GS1.1.1714676691.4.1.1714678743.0.0.0; _ga_3KF4XTPHC4=GS1.1.1714676691.3.1.1714678743.29.0.0" ^
  -H "DNT: 1" ^
  -H ^"If-None-Match: W/^\^"e65a68d1e8^\^"^" ^
  -H "Referer: https://www.sofascore.com/paysandu-santos/tOsXO" ^
  -H "Sec-Fetch-Dest: empty" ^
  -H "Sec-Fetch-Mode: cors" ^
  -H "Sec-Fetch-Site: same-origin" ^
  -H "User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36 Edg/124.0.0.0" ^
  -H "X-Requested-With: 707da2" ^
  -H ^"sec-ch-ua: ^\^"Chromium^\^";v=^\^"124^\^", ^\^"Microsoft Edge^\^";v=^\^"124^\^", ^\^"Not-A.Brand^\^";v=^\^"99^\^"^" ^
  -H "sec-ch-ua-mobile: ?0" ^
  -H ^"sec-ch-ua-platform: ^\^"Windows^\^"^" &

curl "https://www.sofascore.com/api/v1/event/12146204/team-streaks/betting-odds/1" ^
  -H "Accept: */*" ^
  -H "Accept-Language: en-US,en;q=0.9,pt;q=0.8,fr;q=0.7,pt-BR;q=0.6,pt-PT;q=0.5" ^
  -H "Cache-Control: max-age=0" ^
  -H "Connection: keep-alive" ^
  -H "Cookie: _scid=a2c64644-8845-4c87-a02d-10300efe6317; _ga=GA1.1.1480352166.1694613292; _uc_referrer=https://www.sofascore.com/pt/; _tt_enable_cookie=1; _ttp=UKKbqjh7Fg57k9kijgFu-n1uvDt; _scid_r=a2c64644-8845-4c87-a02d-10300efe6317; _gcl_au=1.1.1302485585.1714668818; _ga_HNQ9P9MGZR=GS1.1.1714676694.4.1.1714678743.29.0.0; _ga_QH2YGS7BB4=GS1.1.1714676691.4.1.1714678743.0.0.0; _ga_3KF4XTPHC4=GS1.1.1714676691.3.1.1714678743.29.0.0" ^
  -H "DNT: 1" ^
  -H ^"If-None-Match: W/^\^"6455d9ba14^\^"^" ^
  -H "Referer: https://www.sofascore.com/paysandu-santos/tOsXO" ^
  -H "Sec-Fetch-Dest: empty" ^
  -H "Sec-Fetch-Mode: cors" ^
  -H "Sec-Fetch-Site: same-origin" ^
  -H "User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36 Edg/124.0.0.0" ^
  -H "X-Requested-With: 707da2" ^
  -H ^"sec-ch-ua: ^\^"Chromium^\^";v=^\^"124^\^", ^\^"Microsoft Edge^\^";v=^\^"124^\^", ^\^"Not-A.Brand^\^";v=^\^"99^\^"^" ^
  -H "sec-ch-ua-mobile: ?0" ^
  -H ^"sec-ch-ua-platform: ^\^"Windows^\^"^" &

curl "https://www.sofascore.com/api/v1/event/12146204/win-probability" ^
  -X "HEAD" ^
  -H "Accept: */*" ^
  -H "Accept-Language: en-US,en;q=0.9,pt;q=0.8,fr;q=0.7,pt-BR;q=0.6,pt-PT;q=0.5" ^
  -H "Connection: keep-alive" ^
  -H "Cookie: _scid=a2c64644-8845-4c87-a02d-10300efe6317; _ga=GA1.1.1480352166.1694613292; _uc_referrer=https://www.sofascore.com/pt/; _tt_enable_cookie=1; _ttp=UKKbqjh7Fg57k9kijgFu-n1uvDt; _scid_r=a2c64644-8845-4c87-a02d-10300efe6317; _gcl_au=1.1.1302485585.1714668818; _ga_HNQ9P9MGZR=GS1.1.1714676694.4.1.1714678743.29.0.0; _ga_QH2YGS7BB4=GS1.1.1714676691.4.1.1714678743.0.0.0; _ga_3KF4XTPHC4=GS1.1.1714676691.3.1.1714678743.29.0.0" ^
  -H "DNT: 1" ^
  -H "Referer: https://www.sofascore.com/paysandu-santos/tOsXO" ^
  -H "Sec-Fetch-Dest: empty" ^
  -H "Sec-Fetch-Mode: cors" ^
  -H "Sec-Fetch-Site: same-origin" ^
  -H "User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36 Edg/124.0.0.0" ^
  -H ^"sec-ch-ua: ^\^"Chromium^\^";v=^\^"124^\^", ^\^"Microsoft Edge^\^";v=^\^"124^\^", ^\^"Not-A.Brand^\^";v=^\^"99^\^"^" ^
  -H "sec-ch-ua-mobile: ?0" ^
  -H ^"sec-ch-ua-platform: ^\^"Windows^\^"^" &

curl "https://www.sofascore.com/api/v1/team/1968/events/last/0" ^
  -H "Accept: */*" ^
  -H "Accept-Language: en-US,en;q=0.9,pt;q=0.8,fr;q=0.7,pt-BR;q=0.6,pt-PT;q=0.5" ^
  -H "Cache-Control: max-age=0" ^
  -H "Connection: keep-alive" ^
  -H "Cookie: _scid=a2c64644-8845-4c87-a02d-10300efe6317; _ga=GA1.1.1480352166.1694613292; _uc_referrer=https://www.sofascore.com/pt/; _tt_enable_cookie=1; _ttp=UKKbqjh7Fg57k9kijgFu-n1uvDt; _scid_r=a2c64644-8845-4c87-a02d-10300efe6317; _gcl_au=1.1.1302485585.1714668818; _ga_HNQ9P9MGZR=GS1.1.1714676694.4.1.1714678743.29.0.0; _ga_QH2YGS7BB4=GS1.1.1714676691.4.1.1714678743.0.0.0; _ga_3KF4XTPHC4=GS1.1.1714676691.3.1.1714678743.29.0.0" ^
  -H "DNT: 1" ^
  -H ^"If-None-Match: W/^\^"5306dd2a66^\^"^" ^
  -H "Referer: https://www.sofascore.com/paysandu-santos/tOsXO" ^
  -H "Sec-Fetch-Dest: empty" ^
  -H "Sec-Fetch-Mode: cors" ^
  -H "Sec-Fetch-Site: same-origin" ^
  -H "User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36 Edg/124.0.0.0" ^
  -H "X-Requested-With: 707da2" ^
  -H ^"sec-ch-ua: ^\^"Chromium^\^";v=^\^"124^\^", ^\^"Microsoft Edge^\^";v=^\^"124^\^", ^\^"Not-A.Brand^\^";v=^\^"99^\^"^" ^
  -H "sec-ch-ua-mobile: ?0" ^
  -H ^"sec-ch-ua-platform: ^\^"Windows^\^"^" &
curl "https://www.sofascore.com/api/v1/team/1968/events/next/0" ^
  -H "Accept: */*" ^
  -H "Accept-Language: en-US,en;q=0.9,pt;q=0.8,fr;q=0.7,pt-BR;q=0.6,pt-PT;q=0.5" ^
  -H "Cache-Control: max-age=0" ^
  -H "Connection: keep-alive" ^
  -H "Cookie: _scid=a2c64644-8845-4c87-a02d-10300efe6317; _ga=GA1.1.1480352166.1694613292; _uc_referrer=https://www.sofascore.com/pt/; _tt_enable_cookie=1; _ttp=UKKbqjh7Fg57k9kijgFu-n1uvDt; _scid_r=a2c64644-8845-4c87-a02d-10300efe6317; _gcl_au=1.1.1302485585.1714668818; _ga_HNQ9P9MGZR=GS1.1.1714676694.4.1.1714678743.29.0.0; _ga_QH2YGS7BB4=GS1.1.1714676691.4.1.1714678743.0.0.0; _ga_3KF4XTPHC4=GS1.1.1714676691.3.1.1714678743.29.0.0" ^
  -H "DNT: 1" ^
  -H ^"If-None-Match: W/^\^"ef1cf01585^\^"^" ^
  -H "Referer: https://www.sofascore.com/paysandu-santos/tOsXO" ^
  -H "Sec-Fetch-Dest: empty" ^
  -H "Sec-Fetch-Mode: cors" ^
  -H "Sec-Fetch-Site: same-origin" ^
  -H "User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36 Edg/124.0.0.0" ^
  -H "X-Requested-With: 707da2" ^
  -H ^"sec-ch-ua: ^\^"Chromium^\^";v=^\^"124^\^", ^\^"Microsoft Edge^\^";v=^\^"124^\^", ^\^"Not-A.Brand^\^";v=^\^"99^\^"^" ^
  -H "sec-ch-ua-mobile: ?0" ^
  -H ^"sec-ch-ua-platform: ^\^"Windows^\^"^" &

curl "https://www.sofascore.com/api/v1/event/12146204/statistics" ^
  -H "Accept: */*" ^
  -H "Accept-Language: en-US,en;q=0.9,pt;q=0.8,fr;q=0.7,pt-BR;q=0.6,pt-PT;q=0.5" ^
  -H "Cache-Control: max-age=0" ^
  -H "Connection: keep-alive" ^
  -H "Cookie: _scid=a2c64644-8845-4c87-a02d-10300efe6317; _ga=GA1.1.1480352166.1694613292; _uc_referrer=https://www.sofascore.com/pt/; _tt_enable_cookie=1; _ttp=UKKbqjh7Fg57k9kijgFu-n1uvDt; _scid_r=a2c64644-8845-4c87-a02d-10300efe6317; _gcl_au=1.1.1302485585.1714668818; _ga_HNQ9P9MGZR=GS1.1.1714676694.4.1.1714678743.29.0.0; _ga_QH2YGS7BB4=GS1.1.1714676691.4.1.1714678743.0.0.0; _ga_3KF4XTPHC4=GS1.1.1714676691.3.1.1714678743.29.0.0" ^
  -H "DNT: 1" ^
  -H ^"If-None-Match: W/^\^"31a4ab4496^\^"^" ^
  -H "Referer: https://www.sofascore.com/paysandu-santos/tOsXO" ^
  -H "Sec-Fetch-Dest: empty" ^
  -H "Sec-Fetch-Mode: cors" ^
  -H "Sec-Fetch-Site: same-origin" ^
  -H "User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36 Edg/124.0.0.0" ^
  -H "X-Requested-With: 707da2" ^
  -H ^"sec-ch-ua: ^\^"Chromium^\^";v=^\^"124^\^", ^\^"Microsoft Edge^\^";v=^\^"124^\^", ^\^"Not-A.Brand^\^";v=^\^"99^\^"^" ^
  -H "sec-ch-ua-mobile: ?0" ^
  -H ^"sec-ch-ua-platform: ^\^"Windows^\^"^" &

curl "https://api.sofascore.app/api/v1/player/795177/image" ^
  -H "Accept: image/avif,image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8" ^
  -H "Accept-Language: en-US,en;q=0.9,pt;q=0.8,fr;q=0.7,pt-BR;q=0.6,pt-PT;q=0.5" ^
  -H "Connection: keep-alive" ^
  -H "DNT: 1" ^
  -H "Referer: https://www.sofascore.com/" ^
  -H "Sec-Fetch-Dest: image" ^
  -H "Sec-Fetch-Mode: no-cors" ^
  -H "Sec-Fetch-Site: cross-site" ^
  -H "User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36 Edg/124.0.0.0" ^
  -H ^"sec-ch-ua: ^\^"Chromium^\^";v=^\^"124^\^", ^\^"Microsoft Edge^\^";v=^\^"124^\^", ^\^"Not-A.Brand^\^";v=^\^"99^\^"^" ^
  -H "sec-ch-ua-mobile: ?0" ^
  -H ^"sec-ch-ua-platform: ^\^"Windows^\^"^" &

curl "https://www.sofascore.com/api/v1/event/12146204/graph" ^
  -H "Accept: */*" ^
  -H "Accept-Language: en-US,en;q=0.9,pt;q=0.8,fr;q=0.7,pt-BR;q=0.6,pt-PT;q=0.5" ^
  -H "Cache-Control: max-age=0" ^
  -H "Connection: keep-alive" ^
  -H "Cookie: _scid=a2c64644-8845-4c87-a02d-10300efe6317; _ga=GA1.1.1480352166.1694613292; _uc_referrer=https://www.sofascore.com/pt/; _tt_enable_cookie=1; _ttp=UKKbqjh7Fg57k9kijgFu-n1uvDt; _scid_r=a2c64644-8845-4c87-a02d-10300efe6317; _gcl_au=1.1.1302485585.1714668818; _ga_HNQ9P9MGZR=GS1.1.1714676694.4.1.1714678743.29.0.0; _ga_QH2YGS7BB4=GS1.1.1714676691.4.1.1714678746.0.0.0; _ga_3KF4XTPHC4=GS1.1.1714676691.3.1.1714678746.26.0.0" ^
  -H "DNT: 1" ^
  -H ^"If-None-Match: W/^\^"2201e9a12e^\^"^" ^
  -H "Referer: https://www.sofascore.com/paysandu-santos/tOsXO" ^
  -H "Sec-Fetch-Dest: empty" ^
  -H "Sec-Fetch-Mode: cors" ^
  -H "Sec-Fetch-Site: same-origin" ^
  -H "User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36 Edg/124.0.0.0" ^
  -H "X-Requested-With: 707da2" ^
  -H ^"sec-ch-ua: ^\^"Chromium^\^";v=^\^"124^\^", ^\^"Microsoft Edge^\^";v=^\^"124^\^", ^\^"Not-A.Brand^\^";v=^\^"99^\^"^" ^
  -H "sec-ch-ua-mobile: ?0" ^
  -H ^"sec-ch-ua-platform: ^\^"Windows^\^"^" &

curl "https://www.sofascore.com/api/v1/event/12146204/managers" ^
  -H "Accept: */*" ^
  -H "Accept-Language: en-US,en;q=0.9,pt;q=0.8,fr;q=0.7,pt-BR;q=0.6,pt-PT;q=0.5" ^
  -H "Cache-Control: max-age=0" ^
  -H "Connection: keep-alive" ^
  -H "Cookie: _scid=a2c64644-8845-4c87-a02d-10300efe6317; _ga=GA1.1.1480352166.1694613292; _uc_referrer=https://www.sofascore.com/pt/; _tt_enable_cookie=1; _ttp=UKKbqjh7Fg57k9kijgFu-n1uvDt; _scid_r=a2c64644-8845-4c87-a02d-10300efe6317; _gcl_au=1.1.1302485585.1714668818; _ga_HNQ9P9MGZR=GS1.1.1714676694.4.1.1714678743.29.0.0; _ga_QH2YGS7BB4=GS1.1.1714676691.4.1.1714678746.0.0.0; _ga_3KF4XTPHC4=GS1.1.1714676691.3.1.1714678746.26.0.0" ^
  -H "DNT: 1" ^
  -H ^"If-None-Match: W/^\^"fece0b7924^\^"^" ^
  -H "Referer: https://www.sofascore.com/paysandu-santos/tOsXO" ^
  -H "Sec-Fetch-Dest: empty" ^
  -H "Sec-Fetch-Mode: cors" ^
  -H "Sec-Fetch-Site: same-origin" ^
  -H "User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36 Edg/124.0.0.0" ^
  -H "X-Requested-With: 707da2" ^
  -H ^"sec-ch-ua: ^\^"Chromium^\^";v=^\^"124^\^", ^\^"Microsoft Edge^\^";v=^\^"124^\^", ^\^"Not-A.Brand^\^";v=^\^"99^\^"^" ^
  -H "sec-ch-ua-mobile: ?0" ^
  -H ^"sec-ch-ua-platform: ^\^"Windows^\^"^" &

curl "https://www.sofascore.com/api/v1/event/12146204/lineups" ^
  -H "Accept: */*" ^
  -H "Accept-Language: en-US,en;q=0.9,pt;q=0.8,fr;q=0.7,pt-BR;q=0.6,pt-PT;q=0.5" ^
  -H "Cache-Control: max-age=0" ^
  -H "Connection: keep-alive" ^
  -H "Cookie: _scid=a2c64644-8845-4c87-a02d-10300efe6317; _ga=GA1.1.1480352166.1694613292; _uc_referrer=https://www.sofascore.com/pt/; _tt_enable_cookie=1; _ttp=UKKbqjh7Fg57k9kijgFu-n1uvDt; _scid_r=a2c64644-8845-4c87-a02d-10300efe6317; _gcl_au=1.1.1302485585.1714668818; _ga_HNQ9P9MGZR=GS1.1.1714676694.4.1.1714678743.29.0.0; _ga_QH2YGS7BB4=GS1.1.1714676691.4.1.1714678746.0.0.0; _ga_3KF4XTPHC4=GS1.1.1714676691.3.1.1714678746.26.0.0" ^
  -H "DNT: 1" ^
  -H ^"If-None-Match: W/^\^"6ad9200976^\^"^" ^
  -H "Referer: https://www.sofascore.com/paysandu-santos/tOsXO" ^
  -H "Sec-Fetch-Dest: empty" ^
  -H "Sec-Fetch-Mode: cors" ^
  -H "Sec-Fetch-Site: same-origin" ^
  -H "User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36 Edg/124.0.0.0" ^
  -H "X-Requested-With: 707da2" ^
  -H ^"sec-ch-ua: ^\^"Chromium^\^";v=^\^"124^\^", ^\^"Microsoft Edge^\^";v=^\^"124^\^", ^\^"Not-A.Brand^\^";v=^\^"99^\^"^" ^
  -H "sec-ch-ua-mobile: ?0" ^
  -H ^"sec-ch-ua-platform: ^\^"Windows^\^"^" &

curl "https://www.sofascore.com/api/v1/event/12146204/average-positions" ^
  -X "HEAD" ^
  -H "Accept: */*" ^
  -H "Accept-Language: en-US,en;q=0.9,pt;q=0.8,fr;q=0.7,pt-BR;q=0.6,pt-PT;q=0.5" ^
  -H "Connection: keep-alive" ^
  -H "Cookie: _scid=a2c64644-8845-4c87-a02d-10300efe6317; _ga=GA1.1.1480352166.1694613292; _uc_referrer=https://www.sofascore.com/pt/; _tt_enable_cookie=1; _ttp=UKKbqjh7Fg57k9kijgFu-n1uvDt; _scid_r=a2c64644-8845-4c87-a02d-10300efe6317; _gcl_au=1.1.1302485585.1714668818; _ga_HNQ9P9MGZR=GS1.1.1714676694.4.1.1714678743.29.0.0; _ga_QH2YGS7BB4=GS1.1.1714676691.4.1.1714678746.0.0.0; _ga_3KF4XTPHC4=GS1.1.1714676691.3.1.1714678746.26.0.0" ^
  -H "DNT: 1" ^
  -H "Referer: https://www.sofascore.com/paysandu-santos/tOsXO" ^
  -H "Sec-Fetch-Dest: empty" ^
  -H "Sec-Fetch-Mode: cors" ^
  -H "Sec-Fetch-Site: same-origin" ^
  -H "User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36 Edg/124.0.0.0" ^
  -H ^"sec-ch-ua: ^\^"Chromium^\^";v=^\^"124^\^", ^\^"Microsoft Edge^\^";v=^\^"124^\^", ^\^"Not-A.Brand^\^";v=^\^"99^\^"^" ^
  -H "sec-ch-ua-mobile: ?0" ^
  -H ^"sec-ch-ua-platform: ^\^"Windows^\^"^" &

curl "https://api.sofascore.app/api/v1/event/12146204/jersey/home/player/fancy" ^
  -H "Accept: image/avif,image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8" ^
  -H "Accept-Language: en-US,en;q=0.9,pt;q=0.8,fr;q=0.7,pt-BR;q=0.6,pt-PT;q=0.5" ^
  -H "Connection: keep-alive" ^
  -H "DNT: 1" ^
  -H "Referer: https://www.sofascore.com/" ^
  -H "Sec-Fetch-Dest: image" ^
  -H "Sec-Fetch-Mode: no-cors" ^
  -H "Sec-Fetch-Site: cross-site" ^
  -H "User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36 Edg/124.0.0.0" ^
  -H ^"sec-ch-ua: ^\^"Chromium^\^";v=^\^"124^\^", ^\^"Microsoft Edge^\^";v=^\^"124^\^", ^\^"Not-A.Brand^\^";v=^\^"99^\^"^" ^
  -H "sec-ch-ua-mobile: ?0" ^
  -H ^"sec-ch-ua-platform: ^\^"Windows^\^"^" &
curl "https://api.sofascore.app/api/v1/event/12146204/jersey/away/goalkeeper/fancy" ^
  -H "Accept: image/avif,image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8" ^
  -H "Accept-Language: en-US,en;q=0.9,pt;q=0.8,fr;q=0.7,pt-BR;q=0.6,pt-PT;q=0.5" ^
  -H "Connection: keep-alive" ^
  -H "DNT: 1" ^
  -H "Referer: https://www.sofascore.com/" ^
  -H "Sec-Fetch-Dest: image" ^
  -H "Sec-Fetch-Mode: no-cors" ^
  -H "Sec-Fetch-Site: cross-site" ^
  -H "User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36 Edg/124.0.0.0" ^
  -H ^"sec-ch-ua: ^\^"Chromium^\^";v=^\^"124^\^", ^\^"Microsoft Edge^\^";v=^\^"124^\^", ^\^"Not-A.Brand^\^";v=^\^"99^\^"^" ^
  -H "sec-ch-ua-mobile: ?0" ^
  -H ^"sec-ch-ua-platform: ^\^"Windows^\^"^" &
curl "https://api.sofascore.app/api/v1/event/12146204/jersey/away/player/fancy" ^
  -H "Accept: image/avif,image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8" ^
  -H "Accept-Language: en-US,en;q=0.9,pt;q=0.8,fr;q=0.7,pt-BR;q=0.6,pt-PT;q=0.5" ^
  -H "Connection: keep-alive" ^
  -H "DNT: 1" ^
  -H "Referer: https://www.sofascore.com/" ^
  -H "Sec-Fetch-Dest: image" ^
  -H "Sec-Fetch-Mode: no-cors" ^
  -H "Sec-Fetch-Site: cross-site" ^
  -H "User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36 Edg/124.0.0.0" ^
  -H ^"sec-ch-ua: ^\^"Chromium^\^";v=^\^"124^\^", ^\^"Microsoft Edge^\^";v=^\^"124^\^", ^\^"Not-A.Brand^\^";v=^\^"99^\^"^" ^
  -H "sec-ch-ua-mobile: ?0" ^
  -H ^"sec-ch-ua-platform: ^\^"Windows^\^"^" &

curl "https://api.sofascore.app/api/v1/manager/784883/image" ^
  -H "Accept: image/avif,image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8" ^
  -H "Accept-Language: en-US,en;q=0.9,pt;q=0.8,fr;q=0.7,pt-BR;q=0.6,pt-PT;q=0.5" ^
  -H "Connection: keep-alive" ^
  -H "DNT: 1" ^
  -H "Referer: https://www.sofascore.com/" ^
  -H "Sec-Fetch-Dest: image" ^
  -H "Sec-Fetch-Mode: no-cors" ^
  -H "Sec-Fetch-Site: cross-site" ^
  -H "User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36 Edg/124.0.0.0" ^
  -H ^"sec-ch-ua: ^\^"Chromium^\^";v=^\^"124^\^", ^\^"Microsoft Edge^\^";v=^\^"124^\^", ^\^"Not-A.Brand^\^";v=^\^"99^\^"^" ^
  -H "sec-ch-ua-mobile: ?0" ^
  -H ^"sec-ch-ua-platform: ^\^"Windows^\^"^" &

curl "https://www.sofascore.com/api/v1/event/12146204/shotmap" ^
  -H "Accept: */*" ^
  -H "Accept-Language: en-US,en;q=0.9,pt;q=0.8,fr;q=0.7,pt-BR;q=0.6,pt-PT;q=0.5" ^
  -H "Cache-Control: max-age=0" ^
  -H "Connection: keep-alive" ^
  -H "Cookie: _scid=a2c64644-8845-4c87-a02d-10300efe6317; _ga=GA1.1.1480352166.1694613292; _uc_referrer=https://www.sofascore.com/pt/; _tt_enable_cookie=1; _ttp=UKKbqjh7Fg57k9kijgFu-n1uvDt; _scid_r=a2c64644-8845-4c87-a02d-10300efe6317; _gcl_au=1.1.1302485585.1714668818; _ga_HNQ9P9MGZR=GS1.1.1714676694.4.1.1714678743.29.0.0; _ga_QH2YGS7BB4=GS1.1.1714676691.4.1.1714678746.0.0.0; _ga_3KF4XTPHC4=GS1.1.1714676691.3.1.1714678746.26.0.0" ^
  -H "DNT: 1" ^
  -H ^"If-None-Match: W/^\^"203ecd3b30^\^"^" ^
  -H "Referer: https://www.sofascore.com/paysandu-santos/tOsXO" ^
  -H "Sec-Fetch-Dest: empty" ^
  -H "Sec-Fetch-Mode: cors" ^
  -H "Sec-Fetch-Site: same-origin" ^
  -H "User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36 Edg/124.0.0.0" ^
  -H "X-Requested-With: 707da2" ^
  -H ^"sec-ch-ua: ^\^"Chromium^\^";v=^\^"124^\^", ^\^"Microsoft Edge^\^";v=^\^"124^\^", ^\^"Not-A.Brand^\^";v=^\^"99^\^"^" ^
  -H "sec-ch-ua-mobile: ?0" ^
  -H ^"sec-ch-ua-platform: ^\^"Windows^\^"^" &



'''
# %%

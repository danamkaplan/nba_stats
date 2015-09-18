import requests  
import json  
import pandas as pd

players = []  
player_stats = {'name':None,'avg_dribbles':None,'avg_touch_time':None,'avg_shot_distance':None,'avg_defender_distance':None}

def find_stats(name,player_id):  
    #NBA Stats API using selected player ID
    url = 'http://stats.nba.com/stats/playerdashptshotlog?'+ \
    'DateFrom=&DateTo=&GameSegment=&LastNGames=0&LeagueID=00&'+ \
    'Location=&Month=0&OpponentTeamID=0&Outcome=&Period=0&'+ \
    'PlayerID='+player_id+'&Season=2014-15&SeasonSegment=&'+ \
    'SeasonType=Regular+Season&TeamID=0&VsConference=&VsDivision='

    #Create Dict based on JSON response
    response = requests.get(url)
    shots = response.json()['resultSets'][0]['rowSet']
    data = json.loads(response.text)

    #Create df from data and find averages 
    headers = data['resultSets'][0]['headers']
    shot_data = data['resultSets'][0]['rowSet']
    df = pd.DataFrame(shot_data,columns=headers) 
    avg_def = df['CLOSE_DEF_DIST'].mean(axis=1)
    avg_dribbles = df['DRIBBLES'].mean(axis=1)
    avg_shot_distance = df['SHOT_DIST'].mean(axis=1)
    avg_touch_time = df['TOUCH_TIME'].mean(axis=1)

    #add Averages to dictionary then to list
    player_stats['name'] = name
    player_stats['avg_defender_distance'] = avg_def
    player_stats['avg_shot_distance'] = avg_shot_distance
    player_stats['avg_touch_time'] = avg_touch_time
    player_stats['avg_dribbles'] = avg_dribbles
    players.append(player_stats.copy())

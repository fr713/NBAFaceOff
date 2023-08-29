import requests
from nba_api.stats.endpoints import playercareerstats
from nba_api.stats.endpoints import commonplayerinfo
from nba_api.stats.static import players
from nba_api.stats.endpoints import boxscoreadvancedv2
from nba_api.stats.endpoints import playerawards
import pandas as pd
from pandas import *
from advancedScraper import get_advanced_stats
from advancedScraper import get_championships
import pprint
import csv


#WORKS FOR PLAYERS DRAFTED 2001 AND AFTER
header = ['player','POSITION','GP','FG_PCT','FT_PCT','3PT_PCT','points_avg','assists_avg','rebounds_avg','steals_avg','blocks_avg']
with open('awsdata.csv','w',encoding='UTF8') as f:
    writer = csv.writer(f)
    writer.writerow(header)

def get_player_data(player_name):
    _player_id = players.find_players_by_full_name(player_name)[0]['id']
    print(_player_id)
    career = playercareerstats.PlayerCareerStats(player_id = _player_id) 
    player_profile =  commonplayerinfo.CommonPlayerInfo(player_id = _player_id)
    player_advanced = boxscoreadvancedv2.BoxScoreAdvancedV2(game_id = '0022200056')
    player_awards = playerawards.PlayerAwards(player_id = _player_id)

    player_adv_stat = player_advanced.get_data_frames()[0]
    player_adv_stat.to_csv('file3.csv')
    infor = read_csv('file3.csv')

    player_df = player_profile.get_data_frames()[0]
    player_df.to_csv('file2.csv')
    info = read_csv("file2.csv")

    player_a = player_awards.get_data_frames()[0]
    player_a.to_csv('file4.csv')
    inform = read_csv('file4.csv')

    career_df = career.get_data_frames()[0]
    career_df.to_csv('file1.csv')
    data = read_csv("file1.csv")


    award_list = inform['DESCRIPTION']
    position = info['POSITION'].tolist()[0]
    print(position)
    games_played = data['GP'].tolist()
    field_goal_pct = data['FG_PCT'].tolist()
    three_point_pct = data['FG3_PCT'].tolist()
    free_throw_pct = data['FT_PCT'].tolist()
    rebounds = data['REB'].tolist()
    assists = data['AST'].tolist()
    steals = data['STL'].tolist()
    blocks = data['BLK'].tolist()
    turnovers = data['TOV'].tolist()
    fouls = data['PF'].tolist()
    points = data['PTS'].tolist()
    fgm = data['FGM'].tolist()
    fga = data['FGA'].tolist()
    ftm = data['FTM'].tolist()
    fta = data['FTA'].tolist()
    fgm3 = data['FG3M'].tolist()
    fga3 = data['FG3A'].tolist()

    turnovers_sum = sum(turnovers)
    points_sum = sum(points)
    assists_sum = sum(assists)
    rebounds_sum = sum(rebounds)
    steals_sum = sum(steals)
    blocks_sum = sum(blocks)
    gp_sum = sum(games_played)
    fgm_sum = sum(fgm)
    fga_sum = sum(fga)
    ftm_sum = sum(ftm)
    fta_sum = sum(fta)
    fmg3_sum = sum(fgm3)
    fga3_sum = sum(fga3)

    turnovers_avg = round(turnovers_sum/gp_sum,1)
    points_avg = round(points_sum/gp_sum,1)
    assists_avg = round(assists_sum/gp_sum,1)
    rebounds_avg = round(rebounds_sum/gp_sum,1)
    steals_avg = round(steals_sum/gp_sum,1)
    blocks_avg = round(blocks_sum/gp_sum,1)
    field_goal_pct_final = round(fgm_sum/fga_sum,3)
    free_throw_pct_final = round(ftm_sum/fta_sum,3)
    three_point_pct_final = round(fmg3_sum/fga3_sum,3)
    assist_turn_ratio = assists_avg/turnovers_avg

    awards = []
    for i in award_list:
        if i == 'NBA Most Valuable Player' or i == 'NBA Defensive Player of the Year' or i == 'NBA Finals Most Valuable Player':
            awards.append(i)
        if i == 'All-Defensive Team' or i == 'All-NBA':
            awards.append(i)
    chips = get_championships(player_name)
    awards.append(chips[0])
    data = [[player_name,position,gp_sum,field_goal_pct_final,free_throw_pct_final,three_point_pct_final,points_avg,assists_avg
    ,rebounds_avg,steals_avg,blocks_avg, turnovers_avg, assist_turn_ratio]]
    
    data.append(awards)
    with open('awsdata.csv','a') as f:
        writer = csv.writer(f)
        writer.writerow(data)

    # json 
    career.get_json()
    
    # dictionary
    career_dic = career.get_dict()
    adv_stats = get_advanced_stats(_player_id)
    data.append(adv_stats)
    return data
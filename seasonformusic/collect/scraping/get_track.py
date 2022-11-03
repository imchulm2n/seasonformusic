# -*- coding: utf-8 -*-

import pandas as pd 
import json
import requests
import base64
from get_api import getAccessToken, gettrackAudioFeatures_winter,gettrackAudioFeatures_autumn,gettrackAudioFeatures_summer,gettrackAudioFeatures_spring,gettrackData_winter1,gettrackData_winter2,gettrackData_autumn1,gettrackData_autumn2,gettrackData_summer1,gettrackData_summer2,gettrackData_spring1,gettrackData_spring2

clientID = "dae6ff949ffc4a95aa522c7f148f90f9"
clientSecret = "91f1dc8769ac4e0f995f4224b73ad87d"


tracks_features = {}
token = getAccessToken(clientID, clientSecret)

seasons = ['winter','autumn','summer','spring']

track_name = []
track_popularity = []
track_id = []
track_number = []
track_season = []



trackdata_winter1 = gettrackData_winter1(token)
for i in range(0,len(trackdata_winter1['tracks'])):
    track_name.append(trackdata_winter1['tracks'][i]['name'])
    track_id.append(trackdata_winter1['tracks'][i]['id'])
    track_popularity.append(trackdata_winter1['tracks'][i]['popularity'])
    track_number.append(trackdata_winter1['tracks'][i]['track_number'])
    track_season.append('winter')


trackdata_winter2 = gettrackData_winter2(token)
for i in range(0,len(trackdata_winter2['tracks'])):
    track_name.append(trackdata_winter2['tracks'][i]['name'])
    track_id.append(trackdata_winter2['tracks'][i]['id'])
    track_popularity.append(trackdata_winter2['tracks'][i]['popularity'])
    track_number.append(trackdata_winter2['tracks'][i]['track_number'])
    track_season.append('winter')

trackdata_autumn1 = gettrackData_autumn1(token)
for i in range(0,len(trackdata_autumn1['tracks'])):
    track_name.append(trackdata_autumn1['tracks'][i]['name'])
    track_id.append(trackdata_autumn1['tracks'][i]['id'])
    track_popularity.append(trackdata_autumn1['tracks'][i]['popularity'])
    track_number.append(trackdata_autumn1['tracks'][i]['track_number'])
    track_season.append('autumn')

trackdata_autumn2 = gettrackData_autumn2(token)
for i in range(0,len(trackdata_autumn2['tracks'])):
    track_name.append(trackdata_autumn2['tracks'][i]['name'])
    track_id.append(trackdata_autumn2['tracks'][i]['id'])
    track_popularity.append(trackdata_autumn2['tracks'][i]['popularity'])
    track_number.append(trackdata_autumn2['tracks'][i]['track_number'])
    track_season.append('autumn')

trackdata_summer1 = gettrackData_summer1(token)
for i in range(0,len(trackdata_summer1['tracks'])):
    track_name.append(trackdata_summer1['tracks'][i]['name'])
    track_id.append(trackdata_summer1['tracks'][i]['id'])
    track_popularity.append(trackdata_summer1['tracks'][i]['popularity'])
    track_number.append(trackdata_summer1['tracks'][i]['track_number'])
    track_season.append('summer')

trackdata_summer2 = gettrackData_summer2(token)
for i in range(0,len(trackdata_summer2['tracks'])):
    track_name.append(trackdata_summer2['tracks'][i]['name'])
    track_id.append(trackdata_summer2['tracks'][i]['id'])
    track_popularity.append(trackdata_summer2['tracks'][i]['popularity'])
    track_number.append(trackdata_summer2['tracks'][i]['track_number'])
    track_season.append('summer')

trackdata_spring1 = gettrackData_spring1(token)
for i in range(0,len(trackdata_spring1['tracks'])):
    track_name.append(trackdata_spring1['tracks'][i]['name'])
    track_id.append(trackdata_spring1['tracks'][i]['id'])
    track_popularity.append(trackdata_spring1['tracks'][i]['popularity'])
    track_number.append(trackdata_spring1['tracks'][i]['track_number'])
    track_season.append('spring')

trackdata_spring2 = gettrackData_spring2(token)
for i in range(0,len(trackdata_spring2['tracks'])):
    track_name.append(trackdata_spring2['tracks'][i]['name'])
    track_id.append(trackdata_spring2['tracks'][i]['id'])
    track_popularity.append(trackdata_spring2['tracks'][i]['popularity'])
    track_number.append(trackdata_spring2['tracks'][i]['track_number'])
    track_season.append('spring')

track_df = pd.DataFrame({'track_name' : track_name, 'track_id' : track_id, 'track_popularity' : track_popularity, 'track_number' : track_number, 'track_season' : track_season})
track_df.to_csv("track_df.csv", mode='w')

for season in seasons:
    with open(f'./json_data/season_track/{season}.json', encoding='UTF-8') as f :
        tracks = json.load(f)
    tracks_features['winter'] = gettrackAudioFeatures_winter(token)
    tracks_features['autumn'] = gettrackAudioFeatures_autumn(token)
    tracks_features['summer'] = gettrackAudioFeatures_summer(token)
    tracks_features['spring'] = gettrackAudioFeatures_spring(token)

       
with open(f'./json_data/tracks_features.json','w', encoding='UTF-8') as f:
   json.dump(tracks_features, f)


with open('./json_data/tracks_features.json') as f :
    info = json.load(f)

for season in info:
    for i in info[f'{season}']['audio_features']:
        i['type'] = f'{season}'

with open(f'./json_data/tracks_features2.json','w', encoding='UTF-8') as j:
    json.dump(info, j)

with open('./json_data/tracks_features2.json','r') as k:
    js = json.loads(k.read())

df_audio_features_winter = pd.DataFrame(js['winter']['audio_features'])
df_audio_features_autumn = pd.DataFrame(js['autumn']['audio_features'])
df_audio_features_summer = pd.DataFrame(js['summer']['audio_features'])
df_audio_features_spring = pd.DataFrame(js['spring']['audio_features'])

df_audio_features = pd.concat([df_audio_features_winter,df_audio_features_autumn,df_audio_features_summer,df_audio_features_spring]).reset_index()
df_audio_features = df_audio_features.drop(['index', 'type','uri','track_href','analysis_url','duration_ms','time_signature'], axis = 1)
df_audio_features.to_csv("df_audio_features.csv", mode='w')

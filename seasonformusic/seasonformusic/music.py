# -*- coding: utf-8 -*-

"""
Model 적용을 위한 code
link -> data
"""
# data = "https://open.spotify.com/track/2bgTY4UwhfBYhGT4HUYStN?si=c4c4b7d47406465c"

import json
import requests
import base64
import pandas as pd

from requests.api import head # secret.py에서 클라이언트 정보 가져오기

authUrl = "https://accounts.spotify.com/api/token"
authHeader = {}
authData = {}

clientID = "dae6ff949ffc4a95aa522c7f148f90f9"
clientSecret = "91f1dc8769ac4e0f995f4224b73ad87d"


authUrl = "https://accounts.spotify.com/api/token"
authHeader = {}
authData = {}

def getAccessToken(clientID, clientSecret):
    """
    ## 토큰을 가져오는 함수
    """
    cred = f"{clientID}:{clientSecret}" # secret.py에 사용자 정보 불러오기
    base64_cred = base64.b64encode(cred.encode('ascii')).decode('ascii')

    authHeader['Authorization'] = "Basic " + base64_cred
    authData['grant_type'] = "client_credentials"

    res = requests.post(authUrl, headers=authHeader, data=authData)

    print(res) # <Response [200]> 

    responseObject = res.json() # json 파일화 시키기

    accessToken = responseObject['access_token']

    return accessToken

token = getAccessToken(clientID, clientSecret)


# Playlist의 Tracks를 가져오는 함수를 지정하였습니다.
def getTrackFeatures(token, data):

    # 음악 쿼리를 링크로 변환하는 API (Search)
    endpoint = f"	https://api.spotify.com/v1/search?q={data}&type=track&market=KR&limit=1"

    getHeader = {
        "Authorization" : "Bearer " + token
    }

    res_q = requests.get(endpoint, headers=getHeader)
    track = res_q.json()
    id2 = track['tracks']['items'][0]['id']
    
    endpoint_f = f"	https://api.spotify.com/v1/audio-features/{id2}"
    endpoint_i = f"	https://api.spotify.com/v1/tracks/{id2}"


    res_f = requests.get(endpoint_f, headers=getHeader)
    res_i = requests.get(endpoint_i, headers=getHeader)

    dict_data = {}
    dict_info = {}
    track_features = res_f.json()
    track_info = res_i.json()

    dict_data['danceability'] = track_features['danceability']
    dict_data['acousticness'] = track_features['acousticness']
    dict_data['energy'] = track_features['energy']
    dict_data['key'] = track_features['key']
    dict_data['liveness'] = track_features['liveness']
    dict_data['loudness'] = track_features['loudness']
    dict_data['mode'] = track_features['mode']
    dict_data['speechiness'] = track_features['speechiness']
    dict_data['tempo'] = track_features['tempo']
    dict_data['valence'] = track_features['valence']
    dict_data['popularity'] = track_info['popularity']
    df_data = pd.DataFrame([dict_data])

    dict_info = track_info['name']

    return dict_info, df_data
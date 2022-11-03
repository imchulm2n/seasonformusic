# -*- coding: utf-8 -*-

import json
from re import A
import requests
import base64

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


user_id = "31n4n3dud3olgmkmoxym7ldpicme"

# User의 Playlist 불러오는 API 함수
def getUserPlaylist(token, user_id): 
    """
    ## 플레이리스트를 가져오는 함수
    1. MBTI Playlist를 정리해놓은 사용자의 플레이리스트를 API를 활용해서 불러온다.
    2. `{Title : ID}` 형식으로 `plist_dict`을 리턴한다.
    3. API를 활용한 원본 json 형식을 `users_plists`으로 리턴한다.

    """
    endpoint = f"https://api.spotify.com/v1/users/{user_id}/playlists"
    getHeader = {
      "Authorization" : "Bearer " + token
       }
    
    res_users = requests.get(endpoint, headers=getHeader)
    users_plists = res_users.json()
    

    plist_titles = []
    for i in range(0, len(users_plists['items'])) : 
        plist_titles.append(users_plists['items'][i]["name"])


    plist_dict = {}
    for i in range(0, len(plist_titles)) :
        plist_dict[f'{plist_titles[i]}'] = users_plists['items'][i]["id"]

    return plist_dict, users_plists

plist_dicts, users_plists  = getUserPlaylist(token, user_id)

with open(f'./json_data/season_plist.json','w') as f:
    json.dump(plist_dicts, f)

def getPlaylistTracks(token, playlist_id):

    endpoint = f"https://api.spotify.com/v1/playlists/{playlist_id}/tracks"

    getHeader = {
        "Authorization" : "Bearer " + token
    }

    res = requests.get(endpoint, headers=getHeader)
    playlist_track = res.json()

    return playlist_track

winter_track_dic={}
autumn_track_dic={}
summer_track_dic={}
spring_track_dic={}
pli_track={}

seasons = ['winter','autumn','summer','spring']

#Playlist의 track id
winter_tracks = getPlaylistTracks(token,list(plist_dicts.values())[0])
for i in range(0, len(winter_tracks['items'])):
    winter_track_dic[f'{i}'] = winter_tracks['items'][i]['track']['id']
    
with open(f'./json_data/season_track/winter.json','w') as f:
    json.dump(winter_track_dic, f)

autumn_tracks = getPlaylistTracks(token,list(plist_dicts.values())[1])
for i in range(0, len(autumn_tracks['items'])):
    autumn_track_dic[f'{i}'] = autumn_tracks['items'][i]['track']['id']

with open(f'./json_data/season_track/autumn.json','w') as f:
    json.dump(autumn_track_dic, f)

summer_tracks = getPlaylistTracks(token,list(plist_dicts.values())[2])
for i in range(0, len(summer_tracks['items'])):
    summer_track_dic[f'{i}'] = summer_tracks['items'][i]['track']['id']
    
with open(f'./json_data/season_track/summer.json','w') as f:
    json.dump(summer_track_dic, f)

spring_tracks = getPlaylistTracks(token,list(plist_dicts.values())[3])
for i in range(0, len(spring_tracks['items'])):
    spring_track_dic[f'{i}'] = spring_tracks['items'][i]['track']['id']
    
with open(f'./json_data/season_track/spring.json','w') as f:
    json.dump(spring_track_dic, f)


# track_data 수집
def gettrackData_winter1(token):
    
    endpoint = "https://api.spotify.com/v1/tracks?ids=78bSWIqoNPdJB8QpCVkv0K,2VNpT9fRk1kyksT0S4coZR,4dYODiAYvJHWQJtNganYCY,0wk4GYAryLcXEMvfhzU1bv,2KhNgn4w8LHxn3ybLoofh4,30NvzcboJe3GQRIDkJM0k3,5lEvC4905fBtL9GjJKionT,7rxnGhTlqU3FRUzd8F4R3d,5RLYcoMDw5y0ULlCUvMzsQ,7tIFeLQFS7A6DLcZ12Mv3U,1k555u88NiaBJH6AWlf5rA,48ssDYE9KA7gt7bx01RrT7,24XLVxCLOhNEsjGBUrECsc,1TUkEXQrskATO9SoB4QMUN,3JBnDOUd18QKjDqSYuOfpm,4QqROKO0RtV5CvxE7g90uw,3uA8SjMyDtwtt0jLPMQbVD,63oTx2gvxdNv9qGYQCA005,0c0Gf3FpG1NKKThB434Qbl,7LN1f9jAIu7yxBzsLMN7RB,55tdBGmnhA3pPqn9Ih4vzb,0PkpRtJqrwuXhbdtJuQm7E,6z1kLsntE7FuzKZHZWrXYN,0WSTInLqMrT9po0LAHpZCJ,1mMI14irOrynB5yvQY1Taz,61limJA2zOeHiYkKJHOFtB,1KMc5CXwEkjklwSqPMQjB1,4RUF7vLA3KutJHfQ1eGWuA,3UNXEhxZ1bXQ87osUTfxQl,5f3TJj7s2R0CmffNXTneF7,1oWe4At8PLglBRAeQVcglM,2gN7FWVu7rq1MxJ7DGjhtb,25tkPPlBrYCXkSIAASibtL,3m1LYtflSvSFz4Hu7O4GIF,5xDrO9DEDJGUQGfyoHvgDJ,7z4TxEA4mXG1ChgxXp7Mj3,6RS6rcjnWrdfVuu2U2W2dj,4T2cOfemKB0owJS2JOu7dF,2M7xLL49EPNaX5u6GOj5ue,77jnpzZS9oIGquIGNaKBk6,4rhiJhZyEwEm1tzG4y3vl7,5NHX9nf376Qlt5fsU84SQb,6uYBDTTolezL3ne2HsXDm0,1bUacg9mWo407qZvsknlFd,3Pqp7yCHo6hbxMS0ZGc93N,1eyek0KJEh2v5HQ9uQSybb,0a6dOdshuoE6H5nRErl5Yb,4blIJNUxmJGvvQJJZxXB8S,3kSANhW7k6lMMhYgGH33rK,6TBJkXHPhu3EsMk1bshwuI"
    getHeader = {
        "Authorization" : "Bearer " + token
    }

    res = requests.get(endpoint, headers=getHeader)
    track_data_winter1 = res.json()
    
    return track_data_winter1


def gettrackData_winter2(token):
    
    endpoint = "https://api.spotify.com/v1/tracks?ids=0JL7DoEqAUcOntWmBuOSdh,4YTvuLSqKshDOJvwyDmAYS,10PzmnIzAwd4vRRDUamEwr,1qOla2w5bk6jb5C4RCDZyE,3MEcq4JRbQImU04hBtyM0w,6MPAgclYe1F9LSYXxOuoBC,1E8Cztx0OIj4zm1IZh2XXj,1lhm29o3syw122xynSKaAK,2TkHnzYwHEoTVgoyqf6UJ2,72cq3rZCIEYaq1TM8y5LBQ,6GS3lnAVy5w6AHWEKYzYeS,5rZkRaL4AjykFgw49KULyo,6pm3SR1vvrV54AOJWsN7y7,2TfsNTyC4uuamXBZJnU0ga,6bXqLHhpWoGzPXjm8e9uBY,3SiTPm2IOaCz1cWFv6LSjn,4lLtcSEIGqO7pvXCUvDtIU,48BG1jM0IvYCXcB0rGkUU2,4ilsJT4GNG9dYidf5qcBVb,3CYH422oy1cZNoo0GTG1TK,7Gj8f0zhVvSveNuXRkUGhN,6ZzYETKetIfNUsZUb23jgG,6A1GBCMwbfhkB9e1thR8a8,7i1pavASRUZk62ejaUIESa,1sYSP7gKa5kdKIfhANfori,6SLMyJPRTh2zCX9SJJHTZQ,3JISGU3qHjPaBdWSh6ZJdq,1Cit71poDuP2mxqH35oW9W,45taTTB4hvmb6AnRla8aoF,0l9LpCsYufB1e5PJSvOXbU,6HG6B14eXGGvral4v8JTfG,38uLSU8bZ4g1vrBl1KHHpg,2bU2EvhMM4Z1M1CLJlnZH1,3WGd1zqLLAWUqPCEVTskT3,3DO8WRX72c1Z5hduVL1Nd5,0GPJSHYaXh8rZSSJoUMgyl,18uwL0vNUanqZH0ro2QcOP,75ls0gurX68lUmMjE7QcsE,0rbKrBvZUYY9GN9l057BuY,4SjXHwsZevaRo1M2EQgHf6,1JJUsWVriEtXr8lHSQXTIy,7kZnkHvbHwWWmXMR0vtbVh,3afkJSKX0EAMsJXTZnDXXJ,3K8tRD2Prik7FXbD8lZ6DC,16LATbHXLu0gh8MCw1hUGl,0zd2SSzszSuHCMpzokkKUo,6yTZXMiGHX8bwAQHZvQxkf,1S80okWdnarCmC0KhJPxgK,2bNTtfRuUYgt32fe1X2zaD,36UcoqH2P24RtSGbLKLK3w"
    getHeader = {
        "Authorization" : "Bearer " + token
    }

    res = requests.get(endpoint, headers=getHeader)
    track_data_winter2 = res.json()
    
    return track_data_winter2


def gettrackData_autumn1(token):
    
    endpoint = "https://api.spotify.com/v1/tracks?ids=5mwZ597mJSZ4MtO0EtxWBE,31ZAhjSUqcNutSdVcd93a9,1KkMPNfvkmqHefdD4zWcNG,0lN2KeotmSpAoBMRcSXTX6,6Vu5jrlveGRcQ7FqUujsut,7hSxOrxogaR7YGpg4l8wmd,5kPpA4aMFeAQnahSnTIOi4,3rxJpoEe435WLkaqJK5dnO,3QRUPaizh0X42xNQMr8aPg,0fABPho2JTj4YZVsMjsUNR,1C8vJqfSxRgF2lAxnwJz9E,3cZvGx80KaW9PrJ0OBez7o,607muQQkKQGweEVD6hAgwM,3PFF8Rjo6MFi6lT87uAT33,7CEp2jyohd05jqAiWafcOK,2JJTLtccyOLEqFGMaJEyZv,7oT5JOWwxnwcZRI6NLzhWs,4kaY4LbdbomICC25gYGGtn,6gjmCJkyh45kw4vN7gv99o,30H0FtOCtb5jESDvFcxqXZ,37dkyQQNJLaqk09kkNr7In,7neOIVKDsLaUXV5y84jGuY,18krdoAbqH1jHwymcaIyom,21P1ueLcjEGcKBDzwNL3xs,2Ghu1DdMwxS3VAyB7i38Wo,4TPXKIuXg411bVMZPZdYZl,52FaH5DT8zJzTBvkzhbCtC,7F8uVSXOgdAJBuGimjqoGu,7htOPFqaCfI6j5ssnz2cla,5ptViFrfoKdGPTdd9oQCwr,5efB9wfc6dn3pzll9ElIrH,0cAFqRrz8OqAoHdbiCM5OD,7foTlQj81Z7Ckz9o4tU9yF,7mFigNlS2dsKMhcmJyfpeg,7ijWcf4FsoxoyPK4B9WGp6,2zLRE8rUhH2i7maIU5sWVI,6oKr5vjv2MPG1r5rJNVpUw,6raQqIU6I73Cl7heEjjkkS,5bHIPBAyUdKhTAib5qpqih,2GBrW5lRWjAQMhK612qzVg,1S2LT0vPyOL0xgkUSGMPsg,0NoppScLnCvISNy2CJOnqp,2zlgwqw8BLX2JGB76LIFeF,2ENZ9lWpoLAGFDJsDb2Cbt,67QGnT1Vdfuuy4HkLTUVjj,1HYzRuWjmS9LXCkdVHi25K,0bBrEmo01hYu6gBz4UW9Q8,68ABnHNR4y2COQa4eaM6PS,3tP6QKbXvtrxiDI7QwKyUf,7g97EfyxPG5XZgYmLig9ML"
    getHeader = {
        "Authorization" : "Bearer " + token
    }

    res = requests.get(endpoint, headers=getHeader)
    track_data_autumn1 = res.json()
    
    return track_data_autumn1

def gettrackData_autumn2(token):
    
    endpoint = "https://api.spotify.com/v1/tracks?ids=3zM2yi75oB3v00sZvWUzIn,5Df08ImWepnNDWoOS7pIxq,3ySSbGT5BepfePnva86js7,7I7TTfKcDDAeSf6HPgbdPT,44AbcJTKmV3hipk9gKgUbA,0SPZ7y0fJiozsuWLSAocOl,7CkjU55ROZSwb95dzGan0o,1HOcUR5aloWDwLAsPtWwel,6edYCvijlAPQ1GLPJvDZze,4OHq2ao4pXmGq9OOuP3lxb,5RKnHL0pcT5fPNB38oL4wv,1w2hClDL1xH4FPZIipZ1FJ,0cd3t9ifOeJVirxWxcUNsJ,0O5bo4CqoUcXGyRPoeTHSB,5AkyvofVWUqds8x1HHgDU9,5i6gHFXg4aLK5xvc2jJJC5,3Ml2s37uS9jqRM2R3bfDiB,1OqDvYVDhJyFZny7XlfIyZ,09Nhl3YQnChjlq8WmJz7FS,4B6cJ34Mkfiu4Xo8t8QU7F,7saJl9V0kRYGWuyeURHYNU,0enqhUkjhENOS0x7z9JwgL,68VyLnTpNSeuGUOghdt6MS,6Au7CCNN2wXgCNxdavgxDM,58DqPqnPOrXEIU7Lj0s5PW,3mNbGPCLCxia3yvwWp2P51,6RBziRcDeiho3iTPdtEeg9,6oGcWTN8RAl6VjUappXYHM,4jX2t5UJX0odaOY2VJahmx,0tgxvf4rqBBeEB54h0nnRD"
    getHeader = {
        "Authorization" : "Bearer " + token
    }

    res = requests.get(endpoint, headers=getHeader)
    track_data_autumn2 = res.json()
    
    return track_data_autumn2

def gettrackData_summer1(token):
    
    endpoint = "https://api.spotify.com/v1/tracks?ids=46E1ic6n099e76t5J1TbHn,02UNF1uo5f0UNgc1qx5XGt,0y4c7qajdQDZ55PZ7RkwyG,6xZbRSkdowxgRj6U8qQF1b,4ayr28xOK5Jp5Ag1vNMopT,3CEs5Jnov3YkmYn0Vezrcr,5EzitieoPnjyKHAq0gfRMa,3VC1IEz9M1txlMSx3h3tPM,7nKQ5WAcjnG48knyLuo8gO,5SE57ljOIUJ1ybL9U6CuBH,1ZgfAxHQCXLt8o1VXEHHAt,1Zyd6zQnC6XIIzmg3hP7Ot,56bHclo7YNvpujMveLElQn,4as4XEOR03oGm1STUKl6pa,1Rrj7KyS2R6SP9CQMDJW1w,7nkp1uuSbKkoxMvEs8cSw0,5G8YqJQ6oyPkxBSjpkCVRy,7BiaLnXa10sBpBEcFfm4PP,2YkjXEab4USTV9uuAgC90E,3mjfQvA5gAV6XnH0ZWnIyI,2co7H0J0xQhbcHcXUk9dCn,3t723PlEADna6GjgquoMRW,7IE8eERSpTC9Jaw3arl99B,4eiPbjcTEJDQcsv7WV0vfD,5Z4aqpT39KpY8gbHoJWdou,7gr57cYekMWriyJYbT7oZ4,2Go7eMyOdfKqKOC4x32RYt,0t3Jr6FABrKYLxGgdbco3f,7lthOBXNue2IvedLRfkod8,58402Fg3CUAwsRr5CtJkWH,4O6aJs7sGvhcnMVOwCHC45,0WZhf0isd4av5qlFfKknC3,3DbJBVdTQb4fFcVnSgirer,5dn6QANKbf76pANGjMBida,0EAUxlC7jGzCUkRcn9ydLF,7tQTOyhv9BAjKoMoegHncb,7BR3N1IbXTjEJffLd8aics,42rziXmwGA04hNSMi2MliA,2fJ70dRX7J4jiVxKUQQp7C,1SdLedoEjrMRu5AnvK2EYk,5rIsrawNyPv1q8v11iwJsh,4JViGq60SvqtQXI3WK0OLS,0v1x6rN6JHRapa03JElljE,5KawlOMHjWeUjQtnuRs22c,4L1MHK27ifT30Ndicpr7js,5joNJn9LUvYcamWwa2iYCL,3NfgdU9mbIVhcJF3XvC0c9,0m3W71Oliiv3gQWXi2YAmJ,381g0b6QZxC13SzA2HRMIc,5qSoW3ewNlhRN3FNZPmVns"
    getHeader = {
        "Authorization" : "Bearer " + token
    }

    res = requests.get(endpoint, headers=getHeader)
    track_data_summer1 = res.json()
    
    return track_data_summer1

def gettrackData_summer2(token):
    
    endpoint = "https://api.spotify.com/v1/tracks?ids=1sHT1fYy8hlr9X48PmenVI,3WNuXdBxk8tQ2VI020dqvE,7pNNnrmd3pBIsQTenWExLy,4jQDaI7FRGaDB0llURpnNf,0icGgAiUx5b0amQLycmGUr,0aOf8m2Y7eGsV17WsuH8Xj,12GJcC8SdDYpkbHvFrgp1w,1iIhGHzzrzqQfuNkFI2qAn,4Bmk7JYOquhWmSMMW4WebM,60UEnuG7U7URpqGpUrXSsq,1aDarBap4uQgOt9k4fxWd8,7gQWTvDx7VJRzeRbnlyIm4,7qDbAc6xMW07T7yyMnQqS8,2lAxhE5s3x7OS9sfhsgT1F,2oka7JFVuzimrhZxanlNox,5XTQXTzEVpYq8wL6DZYgSz,5mtEzYr9nGgp57atg6JwX0,7sEwz6PjhQ1bbSSWb6IBid,4CuuqoDzMXeIBEKrP6fSIm,40wb1DugiG4c4ztCt9oaWp,7oEm5Q1virEUB9H0XjWZzF,5ZbwJYmRtJe5Uy9nFkki8W,2AIWoHr9DF6y4KALCBKWQS,1kFevEv3s7Gf6o5xSDR5DL,6fDFxA3j4WpfeCVihCPWSH,1L1N5X35wFk8d5VlyNy2Oa,7GvA9Elz4M91DYl74FAjtD,2J4P46vCFm1rPkNkp9pZWX,0pYacDCZuRhcrwGUA5nTBe,481yYUbtfs67PaKYKxJOeF,1117juaaAkSIUsQxTmmcKM,5vubdGDI1f6Dgq8l9kYOXV,3b7OgfU9SY8C7YBJgTKS74,2MsNSKQNQNRklkKFxxvIav,07IlTJZln2vfZtJ7vR4IMf,3ObPkJQAgjAhTwYvDhPrAW,2VJOpzv5sBpstCX9venJr5,4NKQTbmiBtm1MwqBbQQhpM,5crARIrvoMiMf2AdlD78WN,59FBFyeST1vqN8G41YgFS6,5BXr7hYZQOeRttkeWYTq5S,3VqeTFIvhxu3DIe4eZVzGq,54HsCR7lJJdwxmEnTY1JfF,53YZi9zgTnF0Py0K6ejyWz,28xjm4FnnGI4Xnds7VoNSl,24PhZrRiALtUXgdwXkEwGt,7od91jr6uXk0JoxVaIRA18,2Pp9osgyIcw6o1avfDDDhH,6kH1sKkvgN4Yikake52glq,2avJo0RwtC1zWiOx4CaGWG"
    getHeader = {
        "Authorization" : "Bearer " + token
    }

    res = requests.get(endpoint, headers=getHeader)
    track_data_summer2 = res.json()
    
    return track_data_summer2

def gettrackData_spring1(token):
    
    endpoint = "https://api.spotify.com/v1/tracks?ids=0a3Zd8Bjs8WvnrRfYQQVAL,1IdM9JrXYuMYiTdM983oH4,5A0ut5JjeNLgGaScBIRyBU,6YOXdy9jShw66iOnBzQMKv,0g1AmSKokPboFrxmG1dxKx,3ucfniv4fLB3RPA6N9iLM2,2uUKMGgpJmud58RY9UPtni,5ktwBE88NKZSfmk6Lw2KhS,2nJDePK69THatYkjkjQFE8,3z9s9hp6ouAxH0IUojkC6L,1nlKYpqe2qT1fwiXMr6ju3,3rd8SMsGluOuCw8vaRG5BL,3mmLyEhphJAaW7hyEXAD8l,3PX5Hkkhh4da6Sntk3LwYo,1pz24zu5H9A0S1a2NKT4F0,5WLLVrfFNbseupmtv0p2B1,1GlFf1f1fkvAs0Ni3UCk64,63M8a0AXYVBoZZfZmJbt6O,1HOcUR5aloWDwLAsPtWwel,65wvbMx87q6IHOBWTKAhWr,1paEGBBeqDYfb9AppAt7BO,5ClmwNjQAz1RwLw16V8hsz,5IYnriBBJz1iz1ki3bJnWo,1OCheuNSzM6kBF1d6yWaeh,0GsRx0gPft6RmijIwMsKmG,3MdJSXjBarAYuuJ7rjJLDk,3jM4UiYD4GLhlbDzGRVkkX,3y7ByLZ05tluscOTRgEJ9Y,27zrFrtUtWl2urlvjOn5xc,6T3Mlx5fr71sm0u1YDAb4R,3PWyoYwI4iHLnLWltMt4gd,5TLAKCWzRqi9AY1NdCe0q0,0lBeCroAGkEdjwKZ3xfcLg,469ENLOUiuk31ET76Y8o0U,3CWjpvvz9jUtyRVSLIAsPU,5gkB40BDQE1CvtXpF6fcPm,4as4XEOR03oGm1STUKl6pa,4vh0x47AvwbCywPOlEmfFQ,2mg7JShA6HPvWPvQQ70FDI,4door6xOPf2auseb5Foc9f,0jnUqXkSxqe8hLkPVfzIjz,4X3OlLezpBmskDaqlpINQ8,7i6FTYnqGAy7ICUB8bkPoh,3uA8SjMyDtwtt0jLPMQbVD,4NPARrLIbtMl29ZJv8ESr2,52nTtJWHO7aqBfoDp9YPQs,4h2fsF8dnXtqx4SNsF15KW,0FMNyc1bjwLVCnLL7ZZcvg,2HC6c1d7SiznMV4rkmmxBB,4TihhtLHSnrokOGBeUzSPN"
    getHeader = {
        "Authorization" : "Bearer " + token
    }

    res = requests.get(endpoint, headers=getHeader)
    track_data_spring1 = res.json()
    
    return track_data_spring1

def gettrackData_spring2(token):
    
    endpoint = "https://api.spotify.com/v1/tracks?ids=1ew4EemwjPuSsCuj1ezEfB,3h3fLFPHPIaH1qtItyOhfM,01aVuBzov1TL2iCNhwkguC,4dhGHF3e4s0LmGaNeGlhRF,2BFAuDIbegplcWK9iS4fUR,4hRA2rCPaCOpoEIq5qXaBz,2OrMdePbuUHaNZIcUBC6cG,4Dr2hJ3EnVh2Aaot6fRwDO,6pm3SR1vvrV54AOJWsN7y7,4F9qxQqmkFnBjIvrpiQ7jV,5F6CQgUvHY8p7hpVWSgPT4,4T5fM8eGg5Pj6PLtIGLeU5,0cd3t9ifOeJVirxWxcUNsJ,5NkpsRKvSBukdYQtl3WLZW,1hu25PizQCZj7adOqFEs7y,4rWNW1MU4SGIE4tmN2pZm6,2KqG4GrxMbeEf1IfDwgSE8,4BFZuak8V5kMxx86reStVg,3JBnDOUd18QKjDqSYuOfpm,3F39QYbMWCEvD2zPAECDG5,4EIJ8e7f0104nDFFVhWg0x,1AhfmrzSrDmOIstpRO9wTI,6oAjIsATA9fZPwMnkcfa6S,13On7DYsJ3IrWxBWuOwM8t,21Ov4I4s3dPFAJxd2zAfp7,6ksOaijLwaSWTVRtPgakt0,36UcoqH2P24RtSGbLKLK3w,459LljnQrewu7DcOyhpPYg,1s2s9sd0DOINkrmufuWST0,6Gy46si3ZaGvax7REx24Dc,5Y9hGEOA9o5xdA8RHt8jKw,064lcSgMcllMmVlP0oxlJD,2lQW8bo5EEqLtwTqsT6Wlm,2Yi4Zlcqmt3ibLeOoRnVuT,1dOD5F2hX5TBtKdQlEseR7,1rL3u6JsjQT9Cxg1oHTJEK,48hyqz1yiZTz4rkyKQzqdF,3P3UA61WRQqwCXaoFOTENd,3OxSOsN5UwdRM36KJPLqHK,2izPoWJ6xAuZUNJkdXO3YS,2xms6U7ngGDBYJ4RnRTPyz,107ipu6Vd5OWF5vZZrmzqI,3d98r5yXtWoVmoYYIaWX5h,0sAOiAiIlq3NU7xzM7oaf7,6swTeMijodi9XzShJL0f2Z,5m2tbM2w8mG76uwFgla2iF,1dpixaJ9toPeLL2AXm86ox,45H0YKiZmzZGE9jiEi7FBq,395vU3XBsgKd5iRXT9x94P,0HuBQaSF9UP7IF78wJQvyx"
    getHeader = {
        "Authorization" : "Bearer " + token
    }

    res = requests.get(endpoint, headers=getHeader)
    track_data_spring2 = res.json()
    
    return track_data_spring2

# audio_features 수집
def gettrackAudioFeatures_winter(token):
    
    endpoint = "https://api.spotify.com/v1/audio-features?ids=78bSWIqoNPdJB8QpCVkv0K,2VNpT9fRk1kyksT0S4coZR,4dYODiAYvJHWQJtNganYCY,0wk4GYAryLcXEMvfhzU1bv,2KhNgn4w8LHxn3ybLoofh4,30NvzcboJe3GQRIDkJM0k3,5lEvC4905fBtL9GjJKionT,7rxnGhTlqU3FRUzd8F4R3d,5RLYcoMDw5y0ULlCUvMzsQ,7tIFeLQFS7A6DLcZ12Mv3U,1k555u88NiaBJH6AWlf5rA,48ssDYE9KA7gt7bx01RrT7,24XLVxCLOhNEsjGBUrECsc,1TUkEXQrskATO9SoB4QMUN,3JBnDOUd18QKjDqSYuOfpm,4QqROKO0RtV5CvxE7g90uw,3uA8SjMyDtwtt0jLPMQbVD,63oTx2gvxdNv9qGYQCA005,0c0Gf3FpG1NKKThB434Qbl,7LN1f9jAIu7yxBzsLMN7RB,55tdBGmnhA3pPqn9Ih4vzb,0PkpRtJqrwuXhbdtJuQm7E,6z1kLsntE7FuzKZHZWrXYN,0WSTInLqMrT9po0LAHpZCJ,1mMI14irOrynB5yvQY1Taz,61limJA2zOeHiYkKJHOFtB,1KMc5CXwEkjklwSqPMQjB1,4RUF7vLA3KutJHfQ1eGWuA,3UNXEhxZ1bXQ87osUTfxQl,5f3TJj7s2R0CmffNXTneF7,1oWe4At8PLglBRAeQVcglM,2gN7FWVu7rq1MxJ7DGjhtb,25tkPPlBrYCXkSIAASibtL,3m1LYtflSvSFz4Hu7O4GIF,5xDrO9DEDJGUQGfyoHvgDJ,7z4TxEA4mXG1ChgxXp7Mj3,6RS6rcjnWrdfVuu2U2W2dj,4T2cOfemKB0owJS2JOu7dF,2M7xLL49EPNaX5u6GOj5ue,77jnpzZS9oIGquIGNaKBk6,4rhiJhZyEwEm1tzG4y3vl7,5NHX9nf376Qlt5fsU84SQb,6uYBDTTolezL3ne2HsXDm0,1bUacg9mWo407qZvsknlFd,3Pqp7yCHo6hbxMS0ZGc93N,1eyek0KJEh2v5HQ9uQSybb,0a6dOdshuoE6H5nRErl5Yb,4blIJNUxmJGvvQJJZxXB8S,3kSANhW7k6lMMhYgGH33rK,6TBJkXHPhu3EsMk1bshwuI,0JL7DoEqAUcOntWmBuOSdh,4YTvuLSqKshDOJvwyDmAYS,10PzmnIzAwd4vRRDUamEwr,1qOla2w5bk6jb5C4RCDZyE,3MEcq4JRbQImU04hBtyM0w,6MPAgclYe1F9LSYXxOuoBC,1E8Cztx0OIj4zm1IZh2XXj,1lhm29o3syw122xynSKaAK,2TkHnzYwHEoTVgoyqf6UJ2,72cq3rZCIEYaq1TM8y5LBQ,6GS3lnAVy5w6AHWEKYzYeS,5rZkRaL4AjykFgw49KULyo,6pm3SR1vvrV54AOJWsN7y7,2TfsNTyC4uuamXBZJnU0ga,6bXqLHhpWoGzPXjm8e9uBY,3SiTPm2IOaCz1cWFv6LSjn,4lLtcSEIGqO7pvXCUvDtIU,48BG1jM0IvYCXcB0rGkUU2,4ilsJT4GNG9dYidf5qcBVb,3CYH422oy1cZNoo0GTG1TK,7Gj8f0zhVvSveNuXRkUGhN,6ZzYETKetIfNUsZUb23jgG,6A1GBCMwbfhkB9e1thR8a8,7i1pavASRUZk62ejaUIESa,1sYSP7gKa5kdKIfhANfori,6SLMyJPRTh2zCX9SJJHTZQ,3JISGU3qHjPaBdWSh6ZJdq,1Cit71poDuP2mxqH35oW9W,45taTTB4hvmb6AnRla8aoF,0l9LpCsYufB1e5PJSvOXbU,6HG6B14eXGGvral4v8JTfG,38uLSU8bZ4g1vrBl1KHHpg,2bU2EvhMM4Z1M1CLJlnZH1,3WGd1zqLLAWUqPCEVTskT3,3DO8WRX72c1Z5hduVL1Nd5,0GPJSHYaXh8rZSSJoUMgyl,18uwL0vNUanqZH0ro2QcOP,75ls0gurX68lUmMjE7QcsE,0rbKrBvZUYY9GN9l057BuY,4SjXHwsZevaRo1M2EQgHf6,1JJUsWVriEtXr8lHSQXTIy,7kZnkHvbHwWWmXMR0vtbVh,3afkJSKX0EAMsJXTZnDXXJ,3K8tRD2Prik7FXbD8lZ6DC,16LATbHXLu0gh8MCw1hUGl,0zd2SSzszSuHCMpzokkKUo,6yTZXMiGHX8bwAQHZvQxkf,1S80okWdnarCmC0KhJPxgK,2bNTtfRuUYgt32fe1X2zaD,36UcoqH2P24RtSGbLKLK3w"
    getHeader = {
        "Authorization" : "Bearer " + token
    }

    res = requests.get(endpoint, headers=getHeader)
    track_features_winter = res.json()
    
    return track_features_winter

def gettrackAudioFeatures_autumn(token):
    
    endpoint = "https://api.spotify.com/v1/audio-features?ids=5mwZ597mJSZ4MtO0EtxWBE,31ZAhjSUqcNutSdVcd93a9,1KkMPNfvkmqHefdD4zWcNG,0lN2KeotmSpAoBMRcSXTX6,6Vu5jrlveGRcQ7FqUujsut,7hSxOrxogaR7YGpg4l8wmd,5kPpA4aMFeAQnahSnTIOi4,3rxJpoEe435WLkaqJK5dnO,3QRUPaizh0X42xNQMr8aPg,0fABPho2JTj4YZVsMjsUNR,1C8vJqfSxRgF2lAxnwJz9E,3cZvGx80KaW9PrJ0OBez7o,607muQQkKQGweEVD6hAgwM,3PFF8Rjo6MFi6lT87uAT33,7CEp2jyohd05jqAiWafcOK,2JJTLtccyOLEqFGMaJEyZv,7oT5JOWwxnwcZRI6NLzhWs,4kaY4LbdbomICC25gYGGtn,6gjmCJkyh45kw4vN7gv99o,30H0FtOCtb5jESDvFcxqXZ,37dkyQQNJLaqk09kkNr7In,7neOIVKDsLaUXV5y84jGuY,18krdoAbqH1jHwymcaIyom,21P1ueLcjEGcKBDzwNL3xs,2Ghu1DdMwxS3VAyB7i38Wo,4TPXKIuXg411bVMZPZdYZl,52FaH5DT8zJzTBvkzhbCtC,7F8uVSXOgdAJBuGimjqoGu,7htOPFqaCfI6j5ssnz2cla,5ptViFrfoKdGPTdd9oQCwr,5efB9wfc6dn3pzll9ElIrH,0cAFqRrz8OqAoHdbiCM5OD,7foTlQj81Z7Ckz9o4tU9yF,7mFigNlS2dsKMhcmJyfpeg,7ijWcf4FsoxoyPK4B9WGp6,2zLRE8rUhH2i7maIU5sWVI,6oKr5vjv2MPG1r5rJNVpUw,6raQqIU6I73Cl7heEjjkkS,5bHIPBAyUdKhTAib5qpqih,2GBrW5lRWjAQMhK612qzVg,1S2LT0vPyOL0xgkUSGMPsg,0NoppScLnCvISNy2CJOnqp,2zlgwqw8BLX2JGB76LIFeF,2ENZ9lWpoLAGFDJsDb2Cbt,67QGnT1Vdfuuy4HkLTUVjj,1HYzRuWjmS9LXCkdVHi25K,0bBrEmo01hYu6gBz4UW9Q8,68ABnHNR4y2COQa4eaM6PS,3tP6QKbXvtrxiDI7QwKyUf,7g97EfyxPG5XZgYmLig9ML,3zM2yi75oB3v00sZvWUzIn,5Df08ImWepnNDWoOS7pIxq,3ySSbGT5BepfePnva86js7,7I7TTfKcDDAeSf6HPgbdPT,44AbcJTKmV3hipk9gKgUbA,0SPZ7y0fJiozsuWLSAocOl,7CkjU55ROZSwb95dzGan0o,1HOcUR5aloWDwLAsPtWwel,6edYCvijlAPQ1GLPJvDZze,4OHq2ao4pXmGq9OOuP3lxb,5RKnHL0pcT5fPNB38oL4wv,1w2hClDL1xH4FPZIipZ1FJ,0cd3t9ifOeJVirxWxcUNsJ,0O5bo4CqoUcXGyRPoeTHSB,5AkyvofVWUqds8x1HHgDU9,5i6gHFXg4aLK5xvc2jJJC5,3Ml2s37uS9jqRM2R3bfDiB,1OqDvYVDhJyFZny7XlfIyZ,09Nhl3YQnChjlq8WmJz7FS,4B6cJ34Mkfiu4Xo8t8QU7F,7saJl9V0kRYGWuyeURHYNU,0enqhUkjhENOS0x7z9JwgL,68VyLnTpNSeuGUOghdt6MS,6Au7CCNN2wXgCNxdavgxDM,58DqPqnPOrXEIU7Lj0s5PW,3mNbGPCLCxia3yvwWp2P51,6RBziRcDeiho3iTPdtEeg9,6oGcWTN8RAl6VjUappXYHM,4jX2t5UJX0odaOY2VJahmx,0tgxvf4rqBBeEB54h0nnRD"
    getHeader = {
        "Authorization" : "Bearer " + token
    }

    res = requests.get(endpoint, headers=getHeader)
    track_features_autumn = res.json()
    
    return track_features_autumn

def gettrackAudioFeatures_summer(token):
    
    endpoint = "https://api.spotify.com/v1/audio-features?ids=46E1ic6n099e76t5J1TbHn,02UNF1uo5f0UNgc1qx5XGt,0y4c7qajdQDZ55PZ7RkwyG,6xZbRSkdowxgRj6U8qQF1b,4ayr28xOK5Jp5Ag1vNMopT,3CEs5Jnov3YkmYn0Vezrcr,5EzitieoPnjyKHAq0gfRMa,3VC1IEz9M1txlMSx3h3tPM,7nKQ5WAcjnG48knyLuo8gO,5SE57ljOIUJ1ybL9U6CuBH,1ZgfAxHQCXLt8o1VXEHHAt,1Zyd6zQnC6XIIzmg3hP7Ot,56bHclo7YNvpujMveLElQn,4as4XEOR03oGm1STUKl6pa,1Rrj7KyS2R6SP9CQMDJW1w,7nkp1uuSbKkoxMvEs8cSw0,5G8YqJQ6oyPkxBSjpkCVRy,7BiaLnXa10sBpBEcFfm4PP,2YkjXEab4USTV9uuAgC90E,3mjfQvA5gAV6XnH0ZWnIyI,2co7H0J0xQhbcHcXUk9dCn,3t723PlEADna6GjgquoMRW,7IE8eERSpTC9Jaw3arl99B,4eiPbjcTEJDQcsv7WV0vfD,5Z4aqpT39KpY8gbHoJWdou,7gr57cYekMWriyJYbT7oZ4,2Go7eMyOdfKqKOC4x32RYt,0t3Jr6FABrKYLxGgdbco3f,7lthOBXNue2IvedLRfkod8,58402Fg3CUAwsRr5CtJkWH,4O6aJs7sGvhcnMVOwCHC45,0WZhf0isd4av5qlFfKknC3,3DbJBVdTQb4fFcVnSgirer,5dn6QANKbf76pANGjMBida,0EAUxlC7jGzCUkRcn9ydLF,7tQTOyhv9BAjKoMoegHncb,7BR3N1IbXTjEJffLd8aics,42rziXmwGA04hNSMi2MliA,2fJ70dRX7J4jiVxKUQQp7C,1SdLedoEjrMRu5AnvK2EYk,5rIsrawNyPv1q8v11iwJsh,4JViGq60SvqtQXI3WK0OLS,0v1x6rN6JHRapa03JElljE,5KawlOMHjWeUjQtnuRs22c,4L1MHK27ifT30Ndicpr7js,5joNJn9LUvYcamWwa2iYCL,3NfgdU9mbIVhcJF3XvC0c9,0m3W71Oliiv3gQWXi2YAmJ,381g0b6QZxC13SzA2HRMIc,5qSoW3ewNlhRN3FNZPmVns,1sHT1fYy8hlr9X48PmenVI,3WNuXdBxk8tQ2VI020dqvE,7pNNnrmd3pBIsQTenWExLy,4jQDaI7FRGaDB0llURpnNf,0icGgAiUx5b0amQLycmGUr,0aOf8m2Y7eGsV17WsuH8Xj,12GJcC8SdDYpkbHvFrgp1w,1iIhGHzzrzqQfuNkFI2qAn,4Bmk7JYOquhWmSMMW4WebM,60UEnuG7U7URpqGpUrXSsq,1aDarBap4uQgOt9k4fxWd8,7gQWTvDx7VJRzeRbnlyIm4,7qDbAc6xMW07T7yyMnQqS8,2lAxhE5s3x7OS9sfhsgT1F,2oka7JFVuzimrhZxanlNox,5XTQXTzEVpYq8wL6DZYgSz,5mtEzYr9nGgp57atg6JwX0,7sEwz6PjhQ1bbSSWb6IBid,4CuuqoDzMXeIBEKrP6fSIm,40wb1DugiG4c4ztCt9oaWp,7oEm5Q1virEUB9H0XjWZzF,5ZbwJYmRtJe5Uy9nFkki8W,2AIWoHr9DF6y4KALCBKWQS,1kFevEv3s7Gf6o5xSDR5DL,6fDFxA3j4WpfeCVihCPWSH,1L1N5X35wFk8d5VlyNy2Oa,7GvA9Elz4M91DYl74FAjtD,2J4P46vCFm1rPkNkp9pZWX,0pYacDCZuRhcrwGUA5nTBe,481yYUbtfs67PaKYKxJOeF,1117juaaAkSIUsQxTmmcKM,5vubdGDI1f6Dgq8l9kYOXV,3b7OgfU9SY8C7YBJgTKS74,2MsNSKQNQNRklkKFxxvIav,07IlTJZln2vfZtJ7vR4IMf,3ObPkJQAgjAhTwYvDhPrAW,2VJOpzv5sBpstCX9venJr5,4NKQTbmiBtm1MwqBbQQhpM,5crARIrvoMiMf2AdlD78WN,59FBFyeST1vqN8G41YgFS6,5BXr7hYZQOeRttkeWYTq5S,3VqeTFIvhxu3DIe4eZVzGq,54HsCR7lJJdwxmEnTY1JfF,53YZi9zgTnF0Py0K6ejyWz,28xjm4FnnGI4Xnds7VoNSl,24PhZrRiALtUXgdwXkEwGt,7od91jr6uXk0JoxVaIRA18,2Pp9osgyIcw6o1avfDDDhH,6kH1sKkvgN4Yikake52glq,2avJo0RwtC1zWiOx4CaGWG"
    getHeader = {
        "Authorization" : "Bearer " + token
    }

    res = requests.get(endpoint, headers=getHeader)
    track_features_summer = res.json()
    
    return track_features_summer

def gettrackAudioFeatures_spring(token):

    endpoint = "https://api.spotify.com/v1/audio-features?ids=0a3Zd8Bjs8WvnrRfYQQVAL,1IdM9JrXYuMYiTdM983oH4,5A0ut5JjeNLgGaScBIRyBU,6YOXdy9jShw66iOnBzQMKv,0g1AmSKokPboFrxmG1dxKx,3ucfniv4fLB3RPA6N9iLM2,2uUKMGgpJmud58RY9UPtni,5ktwBE88NKZSfmk6Lw2KhS,2nJDePK69THatYkjkjQFE8,3z9s9hp6ouAxH0IUojkC6L,1nlKYpqe2qT1fwiXMr6ju3,3rd8SMsGluOuCw8vaRG5BL,3mmLyEhphJAaW7hyEXAD8l,3PX5Hkkhh4da6Sntk3LwYo,1pz24zu5H9A0S1a2NKT4F0,5WLLVrfFNbseupmtv0p2B1,1GlFf1f1fkvAs0Ni3UCk64,63M8a0AXYVBoZZfZmJbt6O,1HOcUR5aloWDwLAsPtWwel,65wvbMx87q6IHOBWTKAhWr,1paEGBBeqDYfb9AppAt7BO,5ClmwNjQAz1RwLw16V8hsz,5IYnriBBJz1iz1ki3bJnWo,1OCheuNSzM6kBF1d6yWaeh,0GsRx0gPft6RmijIwMsKmG,3MdJSXjBarAYuuJ7rjJLDk,3jM4UiYD4GLhlbDzGRVkkX,3y7ByLZ05tluscOTRgEJ9Y,27zrFrtUtWl2urlvjOn5xc,6T3Mlx5fr71sm0u1YDAb4R,3PWyoYwI4iHLnLWltMt4gd,5TLAKCWzRqi9AY1NdCe0q0,0lBeCroAGkEdjwKZ3xfcLg,469ENLOUiuk31ET76Y8o0U,3CWjpvvz9jUtyRVSLIAsPU,5gkB40BDQE1CvtXpF6fcPm,4as4XEOR03oGm1STUKl6pa,4vh0x47AvwbCywPOlEmfFQ,2mg7JShA6HPvWPvQQ70FDI,4door6xOPf2auseb5Foc9f,0jnUqXkSxqe8hLkPVfzIjz,4X3OlLezpBmskDaqlpINQ8,7i6FTYnqGAy7ICUB8bkPoh,3uA8SjMyDtwtt0jLPMQbVD,4NPARrLIbtMl29ZJv8ESr2,52nTtJWHO7aqBfoDp9YPQs,4h2fsF8dnXtqx4SNsF15KW,0FMNyc1bjwLVCnLL7ZZcvg,2HC6c1d7SiznMV4rkmmxBB,4TihhtLHSnrokOGBeUzSPN,1ew4EemwjPuSsCuj1ezEfB,3h3fLFPHPIaH1qtItyOhfM,01aVuBzov1TL2iCNhwkguC,4dhGHF3e4s0LmGaNeGlhRF,2BFAuDIbegplcWK9iS4fUR,4hRA2rCPaCOpoEIq5qXaBz,2OrMdePbuUHaNZIcUBC6cG,4Dr2hJ3EnVh2Aaot6fRwDO,6pm3SR1vvrV54AOJWsN7y7,4F9qxQqmkFnBjIvrpiQ7jV,5F6CQgUvHY8p7hpVWSgPT4,4T5fM8eGg5Pj6PLtIGLeU5,0cd3t9ifOeJVirxWxcUNsJ,5NkpsRKvSBukdYQtl3WLZW,1hu25PizQCZj7adOqFEs7y,4rWNW1MU4SGIE4tmN2pZm6,2KqG4GrxMbeEf1IfDwgSE8,4BFZuak8V5kMxx86reStVg,3JBnDOUd18QKjDqSYuOfpm,3F39QYbMWCEvD2zPAECDG5,4EIJ8e7f0104nDFFVhWg0x,1AhfmrzSrDmOIstpRO9wTI,6oAjIsATA9fZPwMnkcfa6S,13On7DYsJ3IrWxBWuOwM8t,21Ov4I4s3dPFAJxd2zAfp7,6ksOaijLwaSWTVRtPgakt0,36UcoqH2P24RtSGbLKLK3w,459LljnQrewu7DcOyhpPYg,1s2s9sd0DOINkrmufuWST0,6Gy46si3ZaGvax7REx24Dc,5Y9hGEOA9o5xdA8RHt8jKw,064lcSgMcllMmVlP0oxlJD,2lQW8bo5EEqLtwTqsT6Wlm,2Yi4Zlcqmt3ibLeOoRnVuT,1dOD5F2hX5TBtKdQlEseR7,1rL3u6JsjQT9Cxg1oHTJEK,48hyqz1yiZTz4rkyKQzqdF,3P3UA61WRQqwCXaoFOTENd,3OxSOsN5UwdRM36KJPLqHK,2izPoWJ6xAuZUNJkdXO3YS,2xms6U7ngGDBYJ4RnRTPyz,107ipu6Vd5OWF5vZZrmzqI,3d98r5yXtWoVmoYYIaWX5h,0sAOiAiIlq3NU7xzM7oaf7,6swTeMijodi9XzShJL0f2Z,5m2tbM2w8mG76uwFgla2iF,1dpixaJ9toPeLL2AXm86ox,45H0YKiZmzZGE9jiEi7FBq,395vU3XBsgKd5iRXT9x94P,0HuBQaSF9UP7IF78wJQvyx"
    getHeader = {
        "Authorization" : "Bearer " + token
    }

    res = requests.get(endpoint, headers=getHeader)
    track_features_spring = res.json()
    
    return track_features_spring



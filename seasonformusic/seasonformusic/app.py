from flask import Flask, render_template, request
import pickle
import numpy as np
from music import *

with open('model.pkl','rb') as pickle_file:
   model = pickle.load(pickle_file)

seasonformusic = Flask(__name__) #어플리케이션 이름 지정

@seasonformusic.route('/')
def send():
    # root url인 ('/')로 접근 했을 경우 send.html를 렌더링한다.
    return render_template('send.html')


@seasonformusic.route('/recv', methods=['POST', 'GET']) # 받을 경우
def recv():
    data = request.form['inpute_code']

    dict_info, df_data = getTrackFeatures(token, data)
    pred = model.predict(df_data)

    track_name = dict_info

    return render_template('recv.html', pred=pred, track_name=track_name,df_data=df_data)

if __name__ == '__main__': # Debug Mode ON
    seasonformusic.run(debug=True)

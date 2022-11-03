import psycopg2
import csv

host="peanut.db.elephantsql.com"
database="jjdzdqcb"
user="jjdzdqcb"
password="lqCFF6vLb2jGnymXDRcprmav_GJ_GxVb"

connection = psycopg2.connect(
    host=host,
    user=user,
    password=password,
    database=database
)

cur = connection.cursor()

cur.execute("DROP TABLE track_table CASCADE;")

cur.execute("DROP TABLE IF EXISTS track_table;")


cur.execute("""CREATE TABLE track_table (
				Id INTEGER,
				track_name VARCHAR(128),
                track_id VARCHAR(128) NOT NULL UNIQUE,
                track_popularity INTEGER,
                track_number INTEGER,
                track_season VARCHAR(128));
			""")

cur.execute("DROP TABLE audio_features_table CASCADE;")

cur.execute("DROP TABLE IF EXISTS audio_features_table;")

cur.execute("""CREATE TABLE audio_features_table (
				Id INTEGER,
                danceability real,
                energy real,
                key real,
                loudness real,
                mode INT,
                speechiness real,
                acousticness real,
                instrumentalness real,
                liveness real,
                valence real,
                tempo real,
                track_id VARCHAR(128) NOT NULL UNIQUE,
                FOREIGN KEY(track_id) REFERENCES track_table(track_id));
			""")


with open('track_df.csv', 'r', encoding='UTF-8') as read_obj:
    csv_reader = csv.reader(read_obj)
    list_of_csv = list(csv_reader)

list_data=[]

for i in range(1,len(list_of_csv)):
  list_data.append(list_of_csv[i])

for i in list_data[0:]:
    cur.execute('INSERT INTO track_table (Id, track_name, track_id, track_popularity, track_number, track_season) VALUES (%s,%s,%s,%s,%s,%s) ON CONFLICT (track_id) DO NOTHING', i)

with open('df_audio_features.csv', 'r', encoding='UTF-8') as read_obj:
    csv_reader = csv.reader(read_obj)
    list_of_csv = list(csv_reader)

list_data2=[]

for i in range(1,len(list_of_csv)):
  list_data2.append(list_of_csv[i])

for i in list_data2[0:]:
    cur.execute('INSERT INTO audio_features_table (Id, danceability, energy,key,loudness,mode,speechiness,acousticness,instrumentalness,liveness,valence,tempo,track_id) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s) ON CONFLICT (track_id) DO NOTHING', i)

connection.commit()

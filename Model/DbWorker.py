import datetime

import psycopg2
from Model.Player import Player


class DbWorker:
    def create_connection(self):
        self.connection = psycopg2.connect(
            database="FootballClub",
            user="postgres",
            password="1",
            host="127.0.0.1",
            port="5432"
        )
        self.cursor = self.connection.cursor()

    def save_player(self, player):
        self.create_connection()
        today = datetime.datetime.today().strftime("%d.%m.%Y")
        if player.type == 'goalkeeper':
            self.cursor.execute(
                "INSERT INTO gk_info (full_name,kicking_play,hand_play,dives,penalty,training_program,date) VALUES (%s,%s,%s,%s,%s,%s,%s)",
                (player.full_name, int(player.indicators[0]), int(player.indicators[1]), int(player.indicators[2]),
                 int(player.indicators[3]), int(player.last_train), today)
            )
        else:
            self.cursor.execute(
                "INSERT INTO players_info(full_name, speed, completion, penalty, long_shots, penalty_acc, awnings, "+
                "dribbling, long_pass,short_pass, intercepts, head_game, selection, tackle, training_program, date)"+
                "VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",
                (player.full_name, int(player.indicators[0]), int(player.indicators[1]), int(player.indicators[2]),
                 int(player.indicators[3]), int(player.indicators[4]), int(player.indicators[5]), int(player.indicators[6]),
                 int(player.indicators[7]), int(player.indicators[8]), int(player.indicators[9]), int(player.indicators[10]),
                 int(player.indicators[11]), int(player.indicators[12]), int(player.last_train), today)
            )
        self.connection.commit()
        print("Record inserted successfully")
        self.connection.close()

    def get_player_history(self, full_name, player_type):
        self.create_connection()
        if player_type == 'goalkeeper':
            self.cursor.execute("SELECT * FROM gk_info WHERE full_name='" + str(full_name) + "'")
            rows = self.cursor.fetchall()
            for row in rows:
                print(row)
        else:
            self.cursor.execute("SELECT * FROM players_info WHERE full_name=%s", str(full_name))
            rows = self.cursor.fetchall()
            for row in rows:
                print(row)
        print("Operation done successfully")
        self.connection.close()

    def get_player(self,full_name):
        pass
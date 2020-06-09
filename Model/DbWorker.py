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
        self.connection.close()

    def get_player_history(self, full_name, player_type):
        self.create_connection()
        player_info = list()
        if player_type == 'goalkeeper':
            self.cursor.execute("SELECT full_name, hand_play, kicking_play, dives, penalty, training_program FROM gk_info WHERE full_name='" + str(full_name) + "' order by date")
            rows = self.cursor.fetchall()
            for row in rows:
                player_info.append([row[0], [row[1], row[2], row[3], row[4], row[5]]])
                print(player_info)
        else:
            self.cursor.execute("SELECT full_name, speed, completion, penalty, long_shots, penalty_acc, awnings, dribbling, long_pass, short_pass, intercepts, head_game, selection, tackle, training_program FROM players_info WHERE full_name='" + str(full_name) + "' order by date")
            rows = self.cursor.fetchall()
            for row in rows:
                player_info.append([row[0], [row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10], row[11], row[12], row[13], row[14]]])
        self.connection.close()
        return player_info

    def get_player_list(self, player_type):
        self.create_connection()
        player_list = list()
        if player_type == 'goalkeeper':
            self.cursor.execute("SELECT full_name FROM gk_info GROUP BY full_name")
            rows = self.cursor.fetchall()
            for row in rows:
                player_list.append(row[0])
        else:
            self.cursor.execute("SELECT full_name FROM players_info GROUP BY full_name")
            rows = self.cursor.fetchall()
            for row in rows:
                player_list.append(row[0])
        self.connection.close()
        return player_list

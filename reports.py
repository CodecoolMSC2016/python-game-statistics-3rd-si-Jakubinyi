
# Report functions


def count_games(file_name):
    game_counter = 0
    with open(file_name, "r") as data_file:
        for line in data_file:
            game_counter += 1
    return game_counter


def decide(file_name, year):
    with open(file_name, "r") as data_file:
        for line in data_file:
            row_list = line.strip("\n").split("\t")
            if int(row_list[2]) == year:
                return True
        return False


def get_latest(file_name):
    with open(file_name, "r") as data_file:
        latest_year = 0
        for line in data_file:
            row_list = line.strip("\n").split("\t")
            if int(row_list[2]) > latest_year:
                latest_year = int(row_list[2])
                latest_title = str(row_list[0])
        return latest_title


def count_by_genre(file_name, genre):
    with open(file_name, "r") as data_file:
        game_counter = 0
        for line in data_file:
            row_list = line.strip().split("\t")
            if row_list[3] == genre:
                game_counter += 1
        return game_counter


def get_line_number_by_title(file_name, title):
    with open(file_name, "r") as data_file:
        line_number = 0
        for line in data_file:
            line_number += 1
            row_list = line.strip().split("\t")
            if row_list[0] == title:
                return line_number
        raise ValueError

game_prop = {"title": 0, "total copies sold": 1,
             "release date": 2, "genre": 3, "publisher": 4}


def count_games(file_name):
    with open(file_name, "r") as data_file:
        game_counter = 0
        for line in data_file:
            game_counter += 1
    return game_counter


def decide(file_name, year):
    with open(file_name, "r") as data_file:
        for line in data_file:
            row_list = line.strip("\n").split("\t")
            if int(row_list[game_prop["release date"]]) == year:
                return True
        return False


def get_latest(file_name):
    with open(file_name, "r") as data_file:
        latest_year = 0
        for line in data_file:
            row_list = line.strip("\n").split("\t")
            if int(row_list[game_prop["release date"]]) > latest_year:
                latest_year = int(row_list[game_prop["release date"]])
                latest_title = str(row_list[game_prop["title"]])
        return latest_title


def count_by_genre(file_name, genre):
    with open(file_name, "r") as data_file:
        game_counter = 0
        for line in data_file:
            row_list = line.strip("\n").split("\t")
            if row_list[game_prop["genre"]] == genre:
                game_counter += 1
        return game_counter


def get_line_number_by_title(file_name, title):
    with open(file_name, "r") as data_file:
        line_number = 0
        for line in data_file:
            line_number += 1
            row_list = line.strip("\n").split("\t")
            if row_list[game_prop["title"]] == title:
                return line_number
        raise ValueError


def sort_abc(file_name):
    with open(file_name, "r") as data_file:
        titles = []
        titles_sorted = []
        for line in data_file:
            row_list = line.strip("\n").split("\t")
            titles.append(row_list[game_prop["title"]])
        for i in range(len(titles)):
            for index in range(len(titles)):
                if titles[index] == min(titles):
                    titles_sorted.append(titles[index])
                    del titles[index]
                    break
        return titles_sorted


def get_genres(file_name):
    with open(file_name, "r") as data_file:
        genres = []
        genres_sorted = []
        for line in data_file:
            row_list = line.strip("\n").split("\t")
            if not row_list[game_prop["genre"]] in genres:
                genres.append(row_list[game_prop["genre"]])
        genres_sorted = sorted(genres, key=lambda x: x.lower())
        return genres_sorted


def when_was_top_sold_fps(file_name):
    with open(file_name, "r") as data_file:
        top = 0
        rows_lists = []
        for line in data_file:
            row_list = line.strip("\n").split("\t")
            rows_lists.append(row_list)
        certain_genre_list = []
        for game in range(len(rows_lists)):
            if rows_lists[game][game_prop["genre"]] == "First-person shooter":
                certain_genre_list.append(
                    rows_lists[game])
        if len(certain_genre_list) == 0:
            raise ValueError
        else:
            for game in range(len(certain_genre_list)):
                if float(certain_genre_list[game][game_prop["total copies sold"]]) > float(top):
                    top = certain_genre_list[game][
                        game_prop["total copies sold"]]
            for game in range(len(certain_genre_list)):
                if certain_genre_list[game][game_prop["total copies sold"]] == top:
                    return int(certain_genre_list[game][game_prop["release date"]])

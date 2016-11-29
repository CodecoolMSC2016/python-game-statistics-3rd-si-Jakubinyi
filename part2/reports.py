import math

game_prop = {"title": 0, "total copies sold": 1,
             "release date": 2, "genre": 3, "publisher": 4}


def get_most_played(file_name):
    with open(file_name, "r") as data_file:
        top = 0
        rows_lists = []
        for line in data_file:
            row_list = line.strip("\n").split("\t")
            rows_lists.append(row_list)
            if float(row_list[game_prop["total copies sold"]]) > float(top):
                top = float(row_list[game_prop["total copies sold"]])
    for row_list in rows_lists:
        if float(row_list[game_prop["total copies sold"]]) == float(top):
            return row_list[game_prop["title"]]


def sum_sold(file_name):
    with open(file_name, "r") as data_file:
        total = 0
        for line in data_file:
            row_list = line.strip("\n").split("\t")
            total += float(row_list[game_prop["total copies sold"]])
        return total


def get_selling_avg(file_name):
    with open(file_name, "r") as data_file:
        selling_list = []
        for line in data_file:
            row_list = line.strip("\n").split("\t")
            selling_list.append(
                float(row_list[game_prop["total copies sold"]]))
        return sum(selling_list) / len(selling_list)


def count_longest_title(file_name):
    with open(file_name, "r") as data_file:
        longest = 0
        for line in data_file:
            row_list = line.strip("\n").split("\t")
            if len(row_list[game_prop["title"]]) > longest:
                longest = len(row_list[game_prop["title"]])
        return longest


def get_date_avg(file_name):
    with open(file_name, "r") as data_file:
        dates = []
        for line in data_file:
            row_list = line.strip("\n").split("\t")
            dates.append(float(row_list[game_prop["release date"]]))
        return math.ceil(sum(dates) / len(dates))


def get_game(file_name, title):
    with open(file_name, "r") as data_file:
        for line in data_file:
            row_list = line.strip("\n").split("\t")
            if row_list[game_prop["title"]] == title:
                row_list[game_prop["total copies sold"]] = float(
                    row_list[game_prop["total copies sold"]])
                row_list[game_prop["release date"]] = int(
                    row_list[game_prop["release date"]])
                return row_list


def count_grouped_by_genre(file_name):
    with open(file_name, "r") as data_file:
        genre_dictionary = {}
        for line in data_file:
            row_list = line.strip("\n").split("\t")
            try:
                genre_dictionary[row_list[game_prop["genre"]]] += 1
            except KeyError:
                genre_dictionary[row_list[game_prop["genre"]]] = 1
        return genre_dictionary


def get_date_ordered(file_name):
    with open(file_name, "r") as data_file:
        rows_lists = []
        for line in data_file:
            row_list = line.strip("\n").split("\t")
            rows_lists.append(row_list)
    rows_lists = sorted(rows_lists, key=lambda x: x[
                        game_prop["title"]], reverse=False)
    rows_lists = sorted(rows_lists, key=lambda x: int(
        x[game_prop["release date"]]), reverse=True)
    title_list = []
    for i in range(len(rows_lists)):
        title_list.append(rows_lists[i][game_prop["title"]])
    return title_list

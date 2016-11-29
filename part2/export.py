from reports import *


def export_file(question, answer, export_file="part2/reports.txt"):
    """ Exporting the reports into a single export file.

    Arguments:
    question -- Judy's questions
    answer -- the value/result of the imported function
    export_file -- the name of the export file (default: reports.txt)
    """
    with open(export_file, "a") as file:
        file.write(question + "\n" + str(answer) + "\n")


def main():
    file_name = "game_stat.txt"

    export_file("What is the most played game", get_most_played(file_name))
    export_file(
        "How many copies have been sold total (million)?", sum_sold(file_name))
    export_file("What is the average selling?", get_selling_avg(file_name))
    export_file("How many characters long is the longest title?",
                count_longest_title(file_name))
    export_file("What is the average of the release dates?",
                get_date_avg(file_name))
    export_file("What properties has a game?",
                get_game(file_name, "StarCraft"))
    export_file("How many games are there grouped by genre?",
                count_grouped_by_genre(file_name))
    export_file("What is the date ordered list of the games? ",
                get_date_ordered(file_name))


if __name__ == "__main__":
    main()

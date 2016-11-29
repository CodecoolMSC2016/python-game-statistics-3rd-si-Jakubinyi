from reports import *


def export_file(question, answer, export_file="reports.txt"):
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

    export_file("How many games are in the file?", count_games(file_name))
    export_file("Is there a game from a given year?", decide(file_name, 1998))
    export_file("Which was the latest game?", get_latest(file_name))
    export_file("How many games do we have by genre?",
                count_by_genre(file_name, "RPG"))
    export_file("What is the line number of the given game (by title)?",
                get_line_number_by_title(file_name, "Diablo III"))
    export_file(
        "What is the alphabetical ordered list of the titles?", sort_abc(file_name))
    export_file("What are the genres?", get_genres(file_name))
    export_file(
        "What is the release date of the top sold First-person shooter game?",
        when_was_top_sold_fps(file_name))


if __name__ == "__main__":
    main()

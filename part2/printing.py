from reports import *


def printer_function(function_name, parameter=None, file_name="game_stat.txt"):
    """ The printer_function  print the return value(s) of the report function.

    Arguments:
    function_name -- the name of the imported function
    parameter -- the parameter of the imported function (default: None)
    file_name -- the name of the input file of the imported function (default: game_stat.txt)
    """
    if parameter == None:
        print(function_name(file_name))
    else:
        print(function_name(file_name, parameter))


def main():
    printer_function(get_most_played)
    printer_function(sum_sold)
    printer_function(get_selling_avg)
    printer_function(count_longest_title)
    printer_function(get_date_avg)
    printer_function(get_game, "StarCraft")
    printer_function(count_grouped_by_genre)
    printer_function(get_date_ordered)


if __name__ == '__main__':
    main()

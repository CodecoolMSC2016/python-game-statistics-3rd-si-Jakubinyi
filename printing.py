from reports import *
# Printing functions


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
    printer_function(count_games)
    printer_function(decide, 1998)
    printer_function(get_latest)
    printer_function(decide, 1998)
    printer_function(count_by_genre, "RPG")


if __name__ == '__main__':
    main()

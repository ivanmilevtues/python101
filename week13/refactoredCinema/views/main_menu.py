from interface import main_menu
from controllers.input_parser import InputParser
from controllers.db_manager import show_movies


def print_menu(*args, **kwargs):
    print(main_menu)


CALL_MAIN_FUNC = {
    "show movies": show_movies,
    # "show movie projections": show_movie_projection,
    # "make reservation": make_reservation,
    # "cancel reservation": cancel_reservation,
    "help": print_menu
}


def main():
    while True:
        spell = input("> ")
        if len(spell.split(' ')) > 2:
            InputParser.call_function(InputParser.input_parser(spell),
                                      CALL_MAIN_FUNC)
        else:
            InputParser.call_function(spell, CALL_MAIN_FUNC)


if __name__ == '__main__':
    main()

from settings import SharedValues, COLS, ROWS, FREE_SEAT, TAKEN_SEAT
from controllers.sign import log_in
from controllers.db_manager import show_movies, show_movie_projection,\
    give_free_spots, give_taken_spots, commit_reservation, delete_reservation
from controllers.validators import logged


@logged
def make_reservation():
    while True:
        tickets = int(input('> How many tickets you want: '))
        show_movies()
        movie_id = input('> Choose movie by id: ')
        show_movie_projection(movie_id)
        projection = input('> Choose projection: ')
        if give_free_spots(projection) >= tickets:
            break
        else:
            print('Not enough free spots!')
    salon = show_movie_theater(projection)

    seats = []
    for _ in range(tickets):
        while True:
            row = int(input('> Select row: '))
            col = int(input('> Select column: '))
            if not check_if_free(salon, row, col):
                break
            print('Select again those spots were taken')
        s.append((row, col))

    commit_reservation(seats, projection)


def show_movie_theater(projection):
    salon = [[FREE_SEAT for _ in range(COLS)] for _ in range(ROWS)]
    taken_spots = give_taken_spots(projection)
    for spot in taken_spots:
        salon[spot.row][spot.col] = TAKEN_SEAT
    print_matrix(salon)
    return salon


def print_matrix(matrix):
    row_num = 1
    print('   ', end='')
    for a in range(1, COLS + 1):
        print(a, end=' ')
    for row in matrix:
        print()
        if(row_num < 10):
            print(str(row_num), end="  ")
        else:
            print(str(row_num), end=" ")
        for el in row:
            print(el, end=" ")
        row_num += 1
    print()


def check_if_free(matrix, row, col):
    return matrix[row][col] == TAKEN_SEAT


@logged
def cancel_reservation():
    delete_reservation(SharedValues.user_logged)
    print('Reservation canceled!')

# This File contains the functions to check the Piece's neighbours
# albeit Square or another Piece
# Created by JiaWei and Kenny (20/3/18)

from board import *

# This function takes in a Board filled with Pieces and identifies
# each Piece's neighbours
def find_neighbour(new_board):

    # For every piece in the Board's piece list
    for piece in new_board.pieces:

        # For every Piece's Direction (TOP, BOTTOM, LEFT, RIGHT)
        for dir in range(LEFT, BOTTOM + 1):

            other_piece = occupied(piece, dir, new_board.pieces)

             # See if the Direction is occupied by a Piece
            if(other_piece):
                # Set the Piece's Direction to the other Piece
                piece.set_neighbour(dir, other_piece)

            # If not, see if the Direction is occupied by a Square
            else:
                other_square = occupied(piece, dir, new_board.squares)
                # set the current piece's direction to that square
                piece.set_neighbour(dir, other_square)


# This function takes in a Piece and goes through either the Board's
# Piece or Square List to check what (obj) is occupying the Piece's Direction
# (TOP, BOTTOM, LEFT, RIGHT)
def occupied(piece, dir, list):

    # For every object in the Board's list
    for obj in list:

        # Return the object if it is at the Direction of the Piece
        if (piece.v_location + delta_v(dir)) == obj.v_location and (piece.h_location + delta_h(dir)) == obj.h_location:
            return obj

    return None

def delta_v(dir):
    if dir == TOP:
        return 1
    if dir == BOTTOM:
        return -1
    return 0


def delta_h(dir):
    if dir == RIGHT:
        return 1
    if dir == LEFT:
        return -1
    return 0

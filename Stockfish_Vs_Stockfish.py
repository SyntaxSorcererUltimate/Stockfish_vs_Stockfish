import chess
from stockfish import Stockfish
import time
path = input("Stockfish Binary Path Here in Quotes for Windows")

# Initialize the two Stockfish engines
stockfish1 = Stockfish(path)
stockfish2 = Stockfish(path)

# Set up the board
board = chess.Board()

# Loop until the game is over
while not board.is_game_over():
    # Set the position for the current player
    if board.turn:
        stockfish1.set_fen_position(board.fen())
        # Get the best move
        best_move = stockfish1.get_best_move()
    else:
        stockfish2.set_fen_position(board.fen())
        # Get the best move
        best_move = stockfish2.get_best_move()

    # Convert the best move to a move object
    stock_move = chess.Move.from_uci(best_move)

    # Print the move in Standard Algebraic Notation
    print(board.san(stock_move))

    # Make the best move
    board.push(stock_move)

    # Wait for 6 seconds
    time.sleep(6)

# Print the final board
print("Final position:")
print(board)

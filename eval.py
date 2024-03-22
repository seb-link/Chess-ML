import chess,random,math,pickle
import chess.engine
import numpy as np

engine = chess.engine.SimpleEngine.popen_uci("/Users/seb/Programs/Python/chess/train/stockfish")


def board_to_array(board : chess.Board):
    # Initialize an empty numpy array
    board_array = np.zeros(65, dtype=np.int8)

    if board.turn == chess.WHITE :
        board_array[64] = 1
    else :
        board_array[64] = 0
    # Iterate over the board squares
    for square, piece in board.piece_map().items():
        # Map chess pieces to numeric values
        piece_value = {
            "P": 1, "N": 2, "B": 3, "R": 4, "Q": 5, "K": 6,
            "p": -1, "n": -2, "b": -3, "r": -4, "q": -5, "k": -6
        }.get(piece.symbol())

        # Set the piece value in the numpy array
        board_array[square] = piece_value

    return board_array

labels = []
board_dataset = []
def main() :
    global labels,board_dataset,centpawn
    board = chess.Board()
    for i in range(random.randint(0,5)) : 
        board.push(random.choice(list(board.legal_moves)))
    while not board.is_game_over() :
        if board.turn == chess.WHITE :
            engine.configure({"Skill Level": 20})
            result = engine.play(board, chess.engine.Limit(time=.1))
        else : 
            engine.configure({"Skill Level": 1})
            result = engine.play(board, chess.engine.Limit(time=.1))
        eval = engine.analyse(board,chess.engine.Limit(time=.1))    
        if eval["score"].relative.is_mate() :
            if board.turn == chess.WHITE : 
                win_percent = 100
                lose_percent = 0
            elif board.turn == chess.BLACK :
                win_percent = 0
                lose_percent = 100
            centpawn = False
        else  : 
            centpawn = True
        if board.turn == chess.WHITE : 
            if centpawn :
                win_percent = 50 + 50 * (2 / (1 + math.exp(-0.00368208 * eval["score"].relative.cp)) - 1)
                lose_percent = 50 + 50 * (2 / (1 + math.exp(-0.00368208 * eval["score"].black().cp)) - 1)
        else : 
            if centpawn :
                win_percent = 50 + 50 * (2 / (1 + math.exp(-0.00368208 * eval["score"].relative.cp)) - 1)
                lose_percent = 50 + 50 * (2 / (1 + math.exp(-0.00368208 * eval["score"].white().cp)) - 1)

        board_dataset.append(board_to_array(board))
        labels.append([win_percent,lose_percent])
        board.push(result.move)

x = int(1)
for i in range(x) :
    main()
    print(i+1,"/" ,x ,"Game Played !")
    
engine.quit()

with open("x_train","wb") as f:
    pickle.dump(board_dataset, f)

with open("y_train","wb") as f:
    pickle.dump(labels, f)

print("bye")
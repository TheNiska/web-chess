from flask import Flask
from flask_socketio import SocketIO, emit
from chess import Board
from views import main_bp

app = Flask(__name__)
app.secret_key = "vLi!4i9Wclwl8wL"
app.register_blueprint(main_bp)
socketio = SocketIO(app)

app.brd = Board()


@socketio.on('chess_move')
def handle_move(data):
    pos1 = data['pos1']
    pos2 = data['pos2']
    square_content = None

    isValid = app.brd.move(pos1, pos2)
    if isValid:
        square_content = app.brd.board[pos2].sprite

    msg = {}
    msg['valid'] = isValid
    msg['pos1'] = pos1
    msg['pos2'] = pos2
    msg['square_content'] = square_content

    emit('chess_response', msg, broadcast=True)


if __name__ == "__main__":
    socketio.run(app, host="0.0.0.0", debug=True)

from flask import (render_template, request, session, flash, jsonify,
                   Blueprint, current_app)


main_bp = Blueprint('bp', __name__)


@main_bp.route('/', methods=['GET', 'POST'])
def chess():
    brd = current_app.brd
    letters = {1: 'a', 2: 'b', 3: 'c', 4: 'd', 5: 'e', 6: 'f', 7: 'g', 8: 'h'}
    return render_template("chess.html", letters=letters, board=brd.board)

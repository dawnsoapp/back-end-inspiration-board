from flask import Blueprint, request, jsonify, make_response, abort
from app import db
from app.models.board import Board
from app.routes.helper import validate_model

# example_bp = Blueprint('example_bp', __name__)
board_bp = Blueprint("board", __name__, url_prefix="/board")

# CREATE


@board_bp.route("", methods=["POST"])
def create_board():
    request_body = request.get_json()
    try:
        new_board = Board.from_dict(request_body)
        db.session.add(new_board)
        db.session.commit()
        return make_response(jsonify({"board": new_board.to_dict()}), 201)
    except KeyError as error:
        abort(make_response(
            {"details": "Cannot create board. Invalid data."}, 400))

# READ


@board_bp.route("", methods=["GET"])
def read_all_boards():
    boards = Board.query.all()
    boards_response = [board.to_dict() for board in boards]

    return jsonify(boards_response)


@board_bp.route("/<board_id>", methods=["GET"])
def read_one_board(board_id):
    board = validate_model(Board, board_id)
    return jsonify({"board": board.to_dict()})
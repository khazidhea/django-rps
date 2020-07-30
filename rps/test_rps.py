from .models import Game, Move
from .services import create_game, start_game, make_move


def test_game_create(user_factory):
    user1 = user_factory('user1')
    user2 = user_factory('user2')

    game = create_game([user1, user2])

    assert user1 in game.users.all()
    assert user2 in game.users.all()
    assert game.status == 'created'


def test_game_start(user_factory, game_factory):
    user1 = user_factory('user1')
    user2 = user_factory('user2')
    game = game_factory([user1, user2])

    start_game(game)

    assert game.status == 'started'


def test_make_first_move(user_factory, game_factory):
    user1 = user_factory('user1')
    user2 = user_factory('user2')
    game = game_factory([user1, user2], status=Game.STATUS_STARTED)

    move = make_move(game, user1, Move.ROCK)

    assert move.id
    assert move.value == Move.ROCK


def test_make_last_move(user_factory, game_factory, move_factory):
    user1 = user_factory('user1')
    user2 = user_factory('user2')
    game = game_factory([user1, user2], status=Game.STATUS_STARTED)
    move = move_factory(game, user1, Move.ROCK)

    make_move(game, user2, Move.SCISSORS)

    assert game.status == Game.STATUS_FINISHED

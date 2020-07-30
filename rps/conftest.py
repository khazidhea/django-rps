import pytest
from .models import User, Game, Move
from .services import create_game, start_game


@pytest.fixture
def user_factory(db):
    def _create_user(username):
        return User.objects.create_user(username, 'password')
    return _create_user


@pytest.fixture
def game_factory(db):
    def _create_game(users, status=None):
        game = create_game(users)
        if status == Game.STATUS_STARTED:
            start_game(game)
        return game
    return _create_game


@pytest.fixture
def move_factory(db):
    def _create_move(game, user, value):
        move = Move.objects.create(game=game, user=user, value=value)
        return move
    return _create_move

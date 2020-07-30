from .models import Game, Move


def create_game(users):
    game = Game.objects.create()
    for user in users:
        game.users.add(user)
    return game


def start_game(game):
    game.status = Game.STATUS_STARTED
    game.save()


def finish_game(game):
    game.status = Game.STATUS_FINISHED
    game.save()


def move_winner(move1, move2):
    if (move1.value == Move.ROCK and move2.value == Move.SCISSORS)  or \
        (move1.value == Move.SCISSORS and move2.value == Move.PAPER) or \
        (move1.value == Move.PAPER and move2.value == Move.ROCK):
        return move1
    elif (move2.value == Move.ROCK and move1.value == Move.SCISSORS)  or \
        (move2.value == Move.SCISSORS and move1.value == Move.PAPER) or \
        (move2.value == Move.PAPER and move1.value == Move.ROCK):
        return move2


def game_winner(game):
    for move1 in game.moves.all():
        rest_of_the_moves = game.moves.exclude(id=move1.id)
        if all(move_winner(move1, move2) for move2 in rest_of_the_moves):
            return move1.user


def make_move(game, user, value):
    move = Move.objects.create(game=game, user=user, value=value)
    winner = game_winner(game)
    if winner:
        finish_game(game)
    return move

import click
from elopy.elo import calculate_rating, rating_variation, invert_score


@click.group()
def cli():
    """
    A simple ELO rating calculator
    """
    pass


@cli.command()
@click.argument('player_rating', type=int)
@click.argument('opponent_rating', type=int)
@click.argument('score', type=click.Choice(['win', 'loss', 'draw', '1', '0.5', '0'], case_sensitive=False))
@click.option('-k', '--k-factor', default=20, show_default=True)
@click.option('--round/--no-round', default=True)
def rate(player_rating, opponent_rating, score, k_factor, round):
    """
    Return new ratings after a match.
    """
    new_player_rating = calculate_rating(player_rating, opponent_rating, score, k_factor, round)
    new_opponent_rating = calculate_rating(opponent_rating, player_rating, invert_score(score), k_factor, round)

    # Adding some color to the output
    if new_player_rating > player_rating:
        p_fg = 'green'
        o_fg = 'red'
    elif new_player_rating < player_rating:
        p_fg = 'red'
        o_fg = 'green'
    else:
        p_fg = 'yellow'
        o_fg = 'yellow'

    click.echo(f'Player rating: {click.style(str(new_player_rating), fg=p_fg)}')
    click.echo(f'Opponent rating: {click.style(str(new_opponent_rating), fg=o_fg)}')

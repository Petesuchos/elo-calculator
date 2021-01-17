def transformed_rating(rating):
    return 10 ** (rating/400)


def expected_score(player_rating, opponent_rating):
    return transformed_rating(player_rating) / (transformed_rating(player_rating)
                                                + transformed_rating(opponent_rating))


def normalized_score(score):
    if score == 'win' or score == '1' or score == 1:
        norm_score = 1
    elif score == 'draw' or score == 'tie' or score == '0.5' or score == 0.5:
        norm_score = 0.5
    elif score == 'loss' or score == '0' or score == 0:
        norm_score = 0
    else:
        raise ValueError('Invalid value for score. Choose from [win, draw, tie, loss, 1, 0.5, 0]')
    return norm_score


def invert_score(score):
    if score == 'win' or score == '1' or score == 1:
        inv_score = 0
    elif score == 'draw' or score == 'tie' or score == '0.5' or score == 0.5:
        inv_score = 0.5
    elif score == 'loss' or score == '0' or score == 0:
        inv_score = 1
    else:
        raise ValueError('Invalid value for score. Choose from [win, draw, tie, loss, 1, 0.5, 0]')
    return inv_score


def rating_variation(player_rating, opponent_rating, score, k_factor=20):
    score = normalized_score(score)
    return k_factor * (score - expected_score(player_rating, opponent_rating))


def calculate_rating(player_rating, opponent_rating, score, k_factor=20, round_rating=True):
    score = normalized_score(score)
    new_rating = player_rating + rating_variation(player_rating, opponent_rating, score, k_factor)
    if round_rating:
        new_rating = round(new_rating)

    return new_rating

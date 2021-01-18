Elo Calculator
###############

A simple command line interface for calculating elo rating.

Usage
======

.. code-block::

    $ elo rate PLAYER_RATING OPPONENT_RATING SCORE [-k] [--round/--no-round]

Where

PLAYER_RATING
    an integer representing the rating of the player

OPPONENT_RATING
    an integer representing the rating of the opponent

SCORE
    - win or 1
    - loss or 0
    - draw, tie or 0.5

`--k`
    The K factor, a constant that impacts how
    the rating will change in a single match.

`--round / --no-round`
    Round results to the nearest integer.

Examples:
----------

.. code-block::

    $ elo rate 1800 1750 win

    > Player rating: 1809
    > Opponent rating: 1741

.. code-block::

    $ elo rate 2100 1900 loss -k 64 --no-round

    > Player rating: 2051.4
    > Opponent rating: 1948.6


How the ELO rating is calculated
=================================

The first step is to compute the **transformed rating** R
for each player.
This step will simplify further calculations.


.. math::
    R_i = 10^{r_i/400}


.. _`expected result`:

Then we calculate the **expected result** E for each player.

.. math::
    E_1 = \frac{ R_1 } {R_1 + R_2}

    E_2 = \frac{ R_2 } {R_1 + R_2}

After the match is complete we can
compute the **rating variation**
:math:`\Delta r_i`
for each player.

.. math::
    \Delta r_i = K (s_i - E_i)

Where:

K
    the K factor is a constant that regulates
    by how much the ratings will vary in a single game.

:math:`s_i`
    is the score of the player i in the game.

    - :math:`s_i = 1` if the player wins,
    - :math:`s_i = 0` if the player loses and
    - :math:`s_i = 0.5` if the match is a draw.

And :math:`E_i`
    is the `expected result`_ of the match

Finally the **new rating** :math:`r'_i` can be calculated by:

.. math::
    r'_i = r_i + \Delta r_i



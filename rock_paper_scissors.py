import random
import matplotlib.pyplot as plt  # <- Replace Plotly with Matplotlib

def play_round(player1_move, player2_move):
    if player1_move == player2_move:
        return 'tie'
    elif (player1_move == 'rock' and player2_move == 'scissors') or \
         (player1_move == 'paper' and player2_move == 'rock') or \
         (player1_move == 'scissors' and player2_move == 'paper'):
        return 'player1'
    else:
        return 'player2'

# Player 1: Random strategy
def random_strategy():
    return random.choice(['rock', 'paper', 'scissors'])

# Player 2: Rule-based strategy
def strategy2(player1_move, player2_move, previous_winner):
    if previous_winner is None:
        return 'paper'
    elif previous_winner == 'player1':
        options = ['rock', 'paper', 'scissors']
        if player2_move in options:
            options.remove(player2_move)
        return options[0]
    elif previous_winner == 'player2':
        return player1_move
    else:
        options = ['rock', 'paper', 'scissors']
        if player2_move in options:
            options.remove(player2_move)
        return options[0]

def simulate(strategy1, strategy2, num_games):
    player1_wins = 0
    player2_wins = 0
    ties = 0
    previous_winner = None
    previous_player2_move = None

    for _ in range(num_games):
        player1_move = strategy1()
        player2_move = strategy2(player1_move, previous_player2_move, previous_winner)
        outcome = play_round(player1_move, player2_move)

        if outcome == 'player1':
            player1_wins += 1
        elif outcome == 'player2':
            player2_wins += 1
        else:
            ties += 1

        previous_winner = outcome
        previous_player2_move = player2_move

    # Plot using matplotlib
    x = ['Player 1 Wins', 'Player 2 Wins', 'Ties']
    y = [player1_wins, player2_wins, ties]

    plt.figure(figsize=(6, 4))
    bars = plt.bar(x, y, color=['green', 'red', 'gray'])
    plt.title('Simulation Results')
    plt.xlabel('Outcome')
    plt.ylabel('Number of Games')

    # Add values on top of bars
    for bar in bars:
        yval = bar.get_height()
        plt.text(bar.get_x() + bar.get_width()/2, yval + 0.01 * max(y), f'{yval:.0f}', ha='center', va='bottom')

    plt.tight_layout()
    plt.show()

    print(f"Player 1 wins: {player1_wins} games")
    print(f"Player 2 wins: {player2_wins} games")
    print(f"Ties: {ties} games")

# Run simulation
num_runs = 10
num_games = 10000

for run in range(num_runs):
    print(f"Run {run + 1}:")
    simulate(random_strategy, strategy2, num_games)
    print("-" * 30)

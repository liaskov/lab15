#   "Rock, paper, scissors" game
import random


ACTIONS = ["Rock", "Paper", "Scissors"]
VICTORIES = {
    ACTIONS[0]: ACTIONS[2],  # Rock beats scissors
    ACTIONS[1]: ACTIONS[0],  # Paper beats rock
    ACTIONS[2]: ACTIONS[1],  # Scissors beats paper
}


# here the player chooses a Rock, Paper or Scissors
def get_user_selection(actions):
    choices = [f"{action}[{num}]" for num, action in enumerate(actions)]
    choices_str = ", ".join(choices)
    selection = int(input(f"Enter a choice ({choices_str}): "))
    user_action = actions[selection]
    return user_action


# choosing a computer action based on randomness
def get_computer_selection(actions):
    computer_action = random.choice(actions)
    return computer_action


def get_determine_winner(victories, user_action, computer_action):
    defeats = victories[user_action]
    if user_action == computer_action:
        result = f"Both players selected {user_action}. It's a tie!"
    elif computer_action in defeats:
        result = f"{user_action} beats {computer_action}! You win!"
    else:
        result = f"{computer_action} beats {user_action}! You lose."
    return result


if __name__ == "__main__":
    user_selection = get_user_selection(ACTIONS)
    print(user_selection)
    computer_selection = get_computer_selection(ACTIONS)
    print(computer_selection)
    determine_winner = get_determine_winner(
        VICTORIES, user_selection, computer_selection
    )
    print(determine_winner)

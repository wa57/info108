import random

def gameRules():
	return {
		"rock": {
			"beats": "scissors",
		},
		'paper': {
			'beats': 'rock',
		},
		'scissors': {
			'beats': 'paper',
		}
	}


def checkInput(user_input):
	user_move = user_input.lower()

	possible_moves = ['rock', 'paper', 'scissors']
	cpu_move = random.choice(possible_moves)

	checkVictor(user_move, cpu_move)


def checkVictor(user_move, cpu_move):
	rules = gameRules()

	print("Your Move: " + str(user_move))
	print("CPU Move: " + str(cpu_move))

	if user_move == cpu_move:
		print('Tie')
	elif user_move == rules[cpu_move]['beats']:
		print('You lose')
	elif rules[user_move]['beats'] == cpu_move:
		print('You win') 

	checkInput(input('Play again? '))





	


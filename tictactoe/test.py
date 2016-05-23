def checkInput(user_input):
	sanitized_input = user_input.lower()

	return {
		'rock': 0,
		'paper': 1,
		'scissors': 2
	}[sanitized_input]

print('Welcome to Rock, Paper, Scissors. Type Rock, Paper, or Scissors to get started.')

user_input = input('')

test = checkInput(user_input)

print(test)
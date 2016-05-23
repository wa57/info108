def checkInput(user_input):
	sanitized_input = user_input.lower()

	return {
		'rock': 0,
		'paper': 1,
		'scissors': 2
	}[sanitized_input]


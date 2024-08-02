import random

def generate_lotto_numbers():
	return random.sample(range(1,46),6)


print(generate_lotto_numbers())

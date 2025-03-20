import random

first_names = ["Jake", "Emma", "Tyler", "Sophia", "Mason", "Olivia", "Liam", "Ava"]
last_names = ["Smith", "Johnson", "Brown", "Davis", "Wilson", "Clark", "Lewis", "Taylor"]

def generate_random_name():
    first = random.choice(first_names)
    last = random.choice(last_names)
    return f"{first} {last}"
import random
import time

OPERATORS = ["+", "-", "*"]
MIN_OPERAND = 2
MAX_OPERAND = 12
TOTAL_PROBLEMS = 10
tries = 0

points = 0


def generate_problem():
    left = random.randint(MIN_OPERAND, MAX_OPERAND)
    right = random.randint(MIN_OPERAND, MAX_OPERAND)
    operator = random.choice(OPERATORS)

    expr = str(left) + " " + str(operator) + " " + str(right)
    answer = eval(expr)

    return expr, answer


wrong = 0
input("Press enter to start!")
print("-----------------------")

start_time = time.time()

for i in range(TOTAL_PROBLEMS):
    expr, answer = generate_problem()
    while True:
        problem = input("Problem #" + str(i + 1) + ": " + expr + " = ")
        if problem == str(answer):
            points += 1
            tries += 1
            break
        wrong += 1
        tries += 1


accuracy = points / tries * 100
end_time = time.time()
total_time = end_time - start_time

print("-----------------------")
print(f"You got {points} in {total_time.__round__()} seconds and a {accuracy.__round__()}%")
children = input("Enter names of children seperated by spaces: ").split()
n = int(input("Enter the step number (n): "))

circle = list(children)

current_possition = 0

while len(circle) > 1:
    currnet_possition = (current_possition + n - 1) % len(circle)
    removed_child = circle.pop(current_possition)

    print(f"Removed {removed_child}")

winner = circle[0]


print(f'Winner is {winner}')

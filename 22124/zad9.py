queue = []
while True:
    name = input("Enter a name: ")
    if name == "END":
        print(f"{len(queue)} people remaining.", queue)
        break
    elif name =="PAID":
        for people in queue:
            print(people)
            queue.clear

        queue = []

    else:
        queue.append(name)

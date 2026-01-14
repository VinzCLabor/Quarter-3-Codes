names = ["Vinz", "Lia", "Jake"]
steps = [
    [4500, 5200, 4800, 5000, 5300],
    [4000, 4100, 3900, 4200, 4600],
    [6000, 5800, 5900, 6100, 6200]
]

days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]

print("Name".ljust(10), end="")
for day in days:
    print(day.ljust(10), end="")
print()

for i in range(len(names)):
    print(names[i].ljust(10), end="")
    for j in range(len(steps[i])):
        print(str(steps[i][j]).ljust(10), end="")
    print()

totals = []

for i in range(len(steps)):
    total = 0
    for j in range(len(steps[i])):
        total += steps[i][j]
    totals.append(total)

highest = totals[0]
lowest = totals[0]
highest_person = names[0]

for i in range(len(totals)):
    if totals[i] > highest:
        highest = totals[i]
        highest_person = names[i]
    if totals[i] < lowest:
        lowest = totals[i]

print()
print("Person with highest total steps:", highest_person)
print("Difference between highest and lowest:", highest - lowest)

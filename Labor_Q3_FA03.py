names = ["Vinz", "Lia", "Jake"]
steps = [
    [4500, 5200, 4800, 5000, 5300],
    [4000, 4100, 3900, 4200, 4600],
    [6000, 5800, 5900, 6100, 6200]
]

days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]

# Print table
print("Name".ljust(10), end="")
for day in days:
    print(day.ljust(10), end="")
print()

for i in range(len(names)):
    print(names[i].ljust(10), end="")
    for j in range(len(steps[i])):
        print(str(steps[i][j]).ljust(10), end="")
    print()

print()

# Calculate totals and averages
for i in range(len(names)):
    total = 0

    for j in range(len(steps[i])):
        total += steps[i][j]

    average = total / len(steps[i])

    print(names[i], "Total steps:", total)
    print(names[i], "Average steps:", average)
    print()

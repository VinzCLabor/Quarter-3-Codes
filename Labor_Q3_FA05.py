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

day_totals = []

for j in range(len(days)):
    total = 0
    for i in range(len(names)):
        total += steps[i][j]
    day_totals.append(total)

most_active_day = days[0]
highest = day_totals[0]

for i in range(len(day_totals)):
    print(days[i] + " total steps:", day_totals[i])
    if day_totals[i] > highest:
        highest = day_totals[i]
        most_active_day = days[i]

print("Most active day overall:", most_active_day)

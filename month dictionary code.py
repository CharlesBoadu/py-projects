days = {'January':31, 'February':28, 'March':31, 'April':30,
        'May':31, 'June':30, 'July':31, 'August':31,
        'September':30, 'October':31, 'November':30, 'December':31}

user_month = input("Enter a month's name: ")
for month in days:
    if month[:3] == user_month[:3]:
        print(days[month], "days are in the month of", month)

items = list(days.items())
items.sort()
print("\nThe months in alphabetical order is: ")
for i in items:
    print(i)

print("\nThe months of the year that has 31 days are: ")
for months in days:
    if days[months] == 31:
        print(months)

items = list(days.items())
items = [(i[1], i[0]) for i in items]
items.sort()
print("\nThe days of the month in ascending order is: ")
for i in items:
    print(i)

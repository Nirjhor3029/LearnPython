for item in 'Python':
    print(item)

for item in ['Mosh', 'Jara', 'Nirjhor']:
    print(item)

for item in range(10):
    print(item)

print("print 5-9 by range")
for item in range(5, 10):
    print(item)

print("print 5-19 by range and forward by 2")
for item in range(5, 20, 2):
    print(item)

# Matrix
for x in range(4):
    for y in range(3):
        for z in range(3):
            print(f"({x}, {y}, {z} )")

#  Practice : F Shape

numbers = [5, 2, 5, 2, 2]

for x_count in numbers:
    print("X" * x_count)


for x_count in range(6):
    for y_count in range(numbers[x_count]):
        print("Y", end="")
    print()

for count_x in numbers:
    output = ''
    for count_y in range(count_x):
        output += 'Z'
    print(output)

























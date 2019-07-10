names = ['John', 'Bob', 'Mosh', 'Sarah', 'Mashrafi']

print(names)
print(names[0])
print(names[1])
print(names[-1])
print(names[-2])
print(names[2])

print(names[2:])
print(names[2:4])
print(names[:-1])
print(names[:3])
print(names[:])
print(names )

names_2 = []
names_2 = ["Hello", "Nirjhor"]
names_2[1] = "ok"
print(names_2)

# Excercise
numbers = [2, 3, 4, 20, 2, 1, 50, 99, 34, 56, 35]
max = number[0]
for number in numbers:
    if(max<number):
        max = number
print(f"Max Number is: {max}")
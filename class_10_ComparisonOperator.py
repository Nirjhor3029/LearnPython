# As simple as  C Programming
# >
# >=
# <
# <=
# ==
# !=

# Exercise

name = input("Name please: ")
length_of_name = len(name)
if length_of_name < 3:
    print("Name must be at least 3 characters")
elif length_of_name > 50:
    print("Name can be a maximum 50 characters")
else:
    print("Name looks good")


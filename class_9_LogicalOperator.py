has_high_income = True
has_good_credit = True
if has_high_income and has_good_credit:
    print("They are eligible for loan")
else:
    print("They are Not eligible for loan")


has_criminal_record = False

# not works just like  ( ! )
if has_high_income and not has_criminal_record:
    print("They are eligible for loan")
else:
    print("They are Not eligible for loan")

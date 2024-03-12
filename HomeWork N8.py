# HomeWork Number8
# Validation


import re

home_phone = "Phone number: 21-38-96"

pattern = r"\w+\s\w+\W\s\d\d\D\d\d\D\d\d"

if re.findall(pattern, home_phone) is not None:
    print("Successful")
    print(home_phone)
else:
    print("Error. Please, try again.")

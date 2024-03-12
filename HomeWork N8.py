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


mobile_phone = "Phone number: +380982738841"

pattern = r"\w+\s\w+\W\s\W\d\d\d\d\d\d\d\d\d\d\d\d"

if re.search(pattern, mobile_phone) is not None:
    print("Successful")
    print(mobile_phone)
else:
    print("Error. Please, try again.")

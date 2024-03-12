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



email = "Email Address: forthehomework@gmail.com"

pattern = r"\w+.\w+\W\s\w{14}\W\w+\W\w+"

if re.match(pattern, email) is not None:
    print("Successful")
    print(email)
else:
    print("Error. Please, try again.")



user = "User name: Peter James O'Conor"

pattern = r"\w{4}\s\w{4}\W\s\w{5}\s\w{5}\s\w{1}\W\w{5}"

if re.search(pattern, user) is not None:
    print("Successful")
    print(user)
else:
    print("Error. Please, try again.")



user_password = "Password: qWeRtY*123*"
pattern = r"\w+.\W\s\w{6}\W\d{3}\W"

if re.match(pattern, user_password) is not None:
    print("Successful")
    print(user_password)

else:
    print("Error. Please, try again.")


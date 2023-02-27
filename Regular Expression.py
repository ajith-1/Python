# * -- 0 times or more occurance in partten
# + -- 1 or more times occurance in partten
# ? -- 0 or 1 times match in partten
# \ escape -- match special character
# [] group operator -- match group of character [a-zA-Z0-9]
#\d -- digits(0-9)
#\w -- numbers and alphabetics (a-z and 0-9)
#{} -- range operator
# re -- regular expression module


import re  # re module
email="python23..learn#1@gmail.com"
partten=re.compile("[a-zA-Z0-9]+\.+[a-zA-Z0-9]+\#[0-9]\@[a-zA-Z0-9]+\.[a-zA-Z0-9]+")  #compile() to force compile
result=partten.findall(email)   #finfing parttrn in email
print(result)

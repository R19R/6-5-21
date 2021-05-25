'''2. pass string and count the repeatation of the string like
     input1- `Bldfdrfd$34fd',
     input2 -  'fd'
     output - 3'''


string = str(input("Enter the String or sentance: "))
sub_string = str(input("Enter the sub string: "))


# print(string.lower().count(sub_string))

#without using count

import re

match = len(re.findall(sub_string, string))

print(match)



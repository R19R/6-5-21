'''3.  seperate the string based on the the second input like
     input1 - `this is bhas`
     input 2 - 3
     output - ['thi', 'sis', 'bha', 's']'''

string = str(input("Enter the string: ")).replace(" ", "")

s = int(input("Enter the number to split the string: "))


print(list(string[i:i+s] for i in range(0,len(string),s)))
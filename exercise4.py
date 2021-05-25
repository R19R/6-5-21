'''4.  generate the random list up to length 10 and create the tuples like first and last and append in the list'''

random_list = [x for x in range(10)]



new_list = list(zip(random_list[0:5], random_list[-1:-6:-1]))

random_list.append(new_list)
print(random_list)
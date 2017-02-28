salary = {
    'Zoe': 145000,
    'Ali': 27000,
    'Ben': 33000,
    'Tommy': 43000,
    'Sue': 67000
}
print salary

#salary['Joe'] = 55000
#salary['Ben'] = None

#del salary['Ali']
#v = salary.pop('Ali')
#print v
#print salary


key_list = salary.keys()
key_list.sort()
print key_list

for key in key_list:
    print "name: {:>6s},  salary: {:6d}".format(key, salary[key])
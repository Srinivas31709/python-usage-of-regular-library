import random
n=random.randbytes(3)
print(n)
print(random.randrange(1,8))
print(random.randint(100,211))
mylist=["yes","no","why yes","why no"]
mylist1={"yes","no","why yes","why no"}
mylist2={'yes':'why yes','no':'why no'}
print(random.choice(list(mylist2.items())))
#print(random.choice(mylist1))
random.shuffle(mylist)
print(mylist)
#1
#list: a collection of strings
#tuple: basically a list, except it cannot be changed or
#modified once created
#indexing: taking something from a list
#mutability: the liability to change
#immutability: to not be able to change

#2-3 
#You can change and manipulate lists, but you cannot with 
#tuples.

#You can use the indexing to use something from the lists 
#and tuples, and you can change things in lists.

#4

mylist=[1, 2, 0, 8]
mylist.append(5)
mylist.remove(1)
mylist[2]=9
print(mylist)

#5

mytuple=("a", "b", "c", "d")
#print (mytuple(3))
#mytuple[2]="f"
#line 26 and line 27 are errors since tuple objects are 
#not callable
mytuple2=("me", "my", "yes", "why")
conc=mytuple+mytuple2
print (conc)

#6

#  Lists are very similar to tuples, since they are both
#the same general thing. They both can be printed out
#and they can both be usedin different ways. However,
#they are not really the same. Lists, for example, can be 
#manipulated and changed in a lot of ways, making it more
#liable to be modified in future codes. Tuples, however,
#cannot be called out and cannot be modified or manipulated
#in any way.
#  Usually, I would prefer lists, because if I ever need to 
#change a tuple, I would need to go back a lot of codes to 
#change it. Another reason why I would choose lists over
#tuples is when I am just generally using them. Lists,
#I can use it as a list all the time, but tuples cannot be
#changed. When I am writing codes, I would like some more 
#flexibility, not just using the tuples that cannot actually
#be changed.
#  Some people might think that tuples are better when you
#are writing things that are not meant to be changed in the
#first place. I would disagree, because even when some 
#things are not meant to be changed, you might change 
#thought and try to change the tuple to a list. Like so, 
#it would be better if you could be prepared. The only 
#reason for tuples, as far as I can see, is for security.
#If your code is shared to the public, I guess it would be 
#better if you had an unchangeable code. Still, it would not
#really moean anything, since if your code was public, 
#it would be changeable anyway. 

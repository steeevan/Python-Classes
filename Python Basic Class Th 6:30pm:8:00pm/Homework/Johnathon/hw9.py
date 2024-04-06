#1-2: with help

yes = [1, 2, 3, 4, 5, 5, 2, 5, 3, 6]

def square(number):
    return number**2

new = list(map(square, yes))
print (new)

yes=list(dict.fromkeys(yes))
print (yes)

#3-4

RGB_value=("red, (255,0,0)")
print (RGB_value)
RGB_value=("red, #FF0000")
print (RGB_value)
#5-6

cities_pop={
  "Chino Hills pop.": 20319,
  "Chino pop.": 19320
}
cities_pop["Sacremento pop."]=20391
cities_pop.pop("Chino Hills pop.")
cities_pop["Chino pop."]=19934
print (cities_pop)

#7-8

first={1,4,5}
second={2,5,1}
subset_third=first.issubset(second)
union_third=first.union(second)
intersect_third=first.intersection(second)
different_third=first.difference(second)

a=["cookie", "party", "yes", "yes", "why", "cookie", "chocolate chip cookie", "cookie"]
a=set(a)
print (a)

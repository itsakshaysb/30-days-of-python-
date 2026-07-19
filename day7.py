it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

print(len(it_companies))
(it_companies.add("twitter"))
comp2 ={'open ai','kimi'}
it_companies.update(comp2)
it_companies.pop()
print(it_companies)

set3=A.union(B)
print (set3)
print(A.intersection(B))
print(A.symmetric_difference(B))
print(A.issubset(B))
print(A.isdisjoint(B))
del set3
age2=set(age)
if len(age)>len(age2):
    print ("lenght of the list is big")
else :
    print("length of the set is high")
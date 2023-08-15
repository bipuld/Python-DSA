mytuple = ('Hello', 'World', 'Python')
print((mytuple))
l=list(mytuple)
l.append('pratice')
l.insert(0,'Nepal is ')
l[2]='Ne'
# for removing data
l.remove('Ne')
l.pop(2)
del l[2]
new_list=[i for i in l if  i!='Hello']
print(new_list)
# conversion for list in to tuples
my_tuples=tuple(l)
print(type(my_tuples))
fruits = ("apple", "banana", "orange", "grape")
# asc=fruits.sort()
f=list(fruits)
# print(f)
asc=f.sort(reverse=True)
print(asc)
numbers = (4, 2, 7, 1, 9, 5)
l=list(numbers)
print(l)

# # Creating a dictionary
student = {
    'name': 'Alice',
    'age': 21,
    'major': 'Computer Science'
}
print(student['name'])
print(f"the student name is {student['name']} and major is {student['major']}") 
print(f"the age of {student['name']}" , 'he age is ',student['age'])
print(student.key())







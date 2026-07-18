word=['Thirty', 'Days', 'Of', 'Python']
sentence = ' '.join(word)
print(sentence)

word2=['Coding', 'For', 'All']
sentence2 = ' '.join(word2)
print(sentence2)

company = "Coding For All"
print(company)

length = len(company)
print(length)

upper_case = company.upper()
print(upper_case)
lower_case = company.lower()
print(lower_case)

print(company.capitalize())
print(company.title())
print(company.swapcase())

slice = company[0:6]
print(slice)

index = company.index('Coding')
print(index)

name=company.replace('Coding', 'Python')
print(name)

newcomp=company.split( )
print(newcomp)

new_cop= "facebook, google, microsoft, apple, ibm, oracle, amazon"
new_cop_list = new_cop.split(", ")
print(new_cop_list) 

word2= ['Coding', 'For', 'All']
accronym = ''
for i in word2:
    accronym += i[0]
print(accronym)

inex = company.index('C')
index2 = company.index('F')
print(inex, index2)
sentance3 ='You cannot end a sentence with because because because is a conjunction'
index3 = sentance3.index('because')
rindex3 = sentance3.rindex('because')
slice3 = sentance3[0:index3]+sentance3[rindex3+7:]
print(slice3)


company2 = "Coding For All"
print (company2.startswith('Coding'))

endwith = company2.endswith('Coding')
print(endwith)

strip1='   Coding For All      ' 
print(strip1.strip())


pythonlist = ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
print('#'.join(pythonlist))

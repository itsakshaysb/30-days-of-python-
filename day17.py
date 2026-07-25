try:
    print(10 + 5)
except:
    print('Something went wrong')

try:
    name = input('Enter your name:')
    year_born = int(input('Year you were born:'))
    age = 2019 - year_born
    print(f'You are {name}. And your age is {age}.')
except:
    print('Something went wrong')

print(*map(lambda a: 'Fizz'*(not a%3)+'Buzz'*(not a%5) or a, range(1,101)),sep='\n')
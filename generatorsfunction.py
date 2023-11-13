#166
# Generator-
# Generator is a function which is responsible to generate a sequence of values.We can write generator functions just like ordinary
# functions, but it uses yield keyword to return values


# Ex-1
def mygen():
    yield 'A'
    yield 'B'
    yield 'C'

g=mygen()
print(type(g))
print(next(g))
print(next(g))
print(next(g))
# print(next(g))


#Ex-2
def countdown(num):
    print("Start Countdown")
    while(num>0):
        yield num
        num=num-1

values=countdown(5)

for x in values:
    print(x)

#Ex-3
#Generate fibconni number by using generator

print("for fibconni series ")

def fib():
    a,b=0,1
    while True:
        yield a
        a,b=b,a+b

for f in fib():
    if f>100:
        break
    print(f)

    

## Generators vs  Normal Collections wrt Perf



##Advantage of Generators Functions
# 1.When compared with class level iterators,generators are very  easy to use
# 2.Improves memory utilization and performance
# 3.Generators are best suitable for reading data from large number of files
# 4. Generators work best for web scraping and crawling
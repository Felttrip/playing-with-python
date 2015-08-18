import random
import time
def main():
    sample = [random.randint(0,2**16) for i in range(1000000)]
    time_it(slow_count,sample)
    time_it(bitwise_and,sample)
    time_it(lookup_table,sample)
    return

#Nate
def lookup_table(listOfNumbers):
    count = {}
    table = {}
    for number in listOfNumbers:
        if not count.has_key(number):
            table[number] = bin(number).count('1')
            count[number] = 1
        else:
            count[number] += 1
    total = 0
    for k, v in count.items():
        total += table[k]*v
    return total

#Ben S.
def bitwise_and(listOfNumbers):
    #build table
    table = [2**i for i in range(17)]
    count = 0
    for number in listOfNumbers:
        for val in table:
            if number & val != 0:
                count += 1
    return count

#Slow algo for checking
def slow_count(listOfNums):
    count = 0
    for number in listOfNums:
        count += bin(number).count('1')
    return count

def time_it(func, sample):
    t1 = time.time()
    num = func(sample)
    t2 = time.time()
    print func.__name__, "time", t2-t1
    return

if __name__ == '__main__':
    main()

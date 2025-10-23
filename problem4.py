def fizzbuzz(i):

    if i % 3 == 0:
    #determines if the given integer is divisbible by 3
        print("Fizz")
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    #determines if the given integer is divisble by 5 AND 3
    if i % 5 == 0:
        print("Buzz")
    #determines if the given integer is disvisble by 5
    if i % 3 == 1 or i % 5 == 1:
        print(i)

    

fizzbuzz(15)
#should print fizz, fizzbuzz, and buzz
fizzbuzz(1)
#should print out 1
fizzbuzz(3)
#should print out fizz

#i did not check for any other possible edgecases

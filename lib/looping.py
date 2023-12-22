#!/usr/bin/env python3

def happy_new_year():
   counter=10
   while counter>=1:
       print(counter)
       counter-=1
   while counter==0:
       print("Happy New Year!")
       break


def square_integers(int_list):
     int_list=([1,2,3,4,5])
     squared_integers=[]
     for item in int_list:
         squared_integers.append(item**2)
     return squared_integers
        

def fizzbuzz():
    counter=0 
    for counter in range(100):
        if (counter+1) % 3 == 0 and (counter+1) % 5 == 0:
            print('FizzBuzz')
        elif (counter+1) % 3 == 0:
            print('Fizz')
        elif(counter+1) % 5 == 0:
            print("Buzz")
        else:
            print(counter+1)

    
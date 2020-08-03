import time
import random #because to have a im felling lucky moment at the end(this is an additional feature)
#this describes what the program does for the user
print('DISCLAIMER: For now this can take only one value. BATTERIES NOT INCLUDED!!!')
def main():
    print('OK!!!')
    time.sleep(0.25)
    
    #asks for the begging value
    print('Type in the range(where do you want it to START!)')
    fir = int(input())
    if fir < 0 :
        print('Wrong statment. Try again')
        time.sleep(1)
        main()
    
    #asks for the end value
    print('Where do you want it to END?')
    end = int(input())
    if end < 0:
        print('Wrong statment. Try again')
        time.sleep(1)
        main()
        
    #expression to check if the first value compared with the second one
    if fir > end :
        print('The end value has to be greater than the first value')
        time.sleep(1)
        main() 
    #asks on what value to check
    print('On what value do you want to check?')
    val = int(input())
    time.sleep(1)
    for i in range(int(fir) , int(end)):
        if i % val == 0:
            print('---------------------')
            print(i)
            print('---')   
            #the one with the small amount of dashes shows the value           
    
    
def begin():
    print('This is a program that can identify the multiples of which number you have typed!!!')


    print('Do you want to start? ')

    time.sleep(0.25)
    print('Type "yes" or "no" ')

    x = input()

    if x == 'yes':
        main()
    elif x == 'no':
        print('Get out of here!!! ')
    else:
        print('Invalid statment. The program will rerun in about a second.')
        time.sleep(0.25)
        begin()

begin()

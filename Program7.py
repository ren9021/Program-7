#********************************************************************
#
#  Developer:         Renee White
#
#  Program #:         7
#
#  File Name:         Program7.py
#
#  Description:       This program calculates faculty pay raises at a company by reading contents of a file
#
#********************************************************************
def main():
    developerInfo()
    print('Project Pay Raise')
    print('')
    inFile = open('program7.txt', 'r')
    lineRead = inFile.readline()
    totalB = 0.0
    totRaise = 0.0
    while lineRead != '':
       words = lineRead.split()
       for word in words:
           num = float(word)
           totalB = totalB + num
           if num > 50000.0:
               if num <= 60000.0:
                   salary = num * 0.07
                   print('This faculty member will receive a 7% raise of $', format(salary, ',.2f'),
                                                                             sep='')
               elif num > 60000.0:
                   salary = num * 0.04
                   print('This faculty member will receive a 4% raise of $', format(salary, ',.2f'),
                                                                             sep='')
           else:
               salary = num * 0.055
               print('This faculty member will receive a 5.5% raise of $', format(salary, ',.2f'),
                                                                           sep='')
           totRaise = totRaise + salary
           Avg = totRaise / 22 
           totalA = totalB + totRaise


               
       lineRead = inFile.readline()
    inFile.close()

    print('')
    print('')
    print('If Project Pay Raise is implemented, the total amount of all raises would be: $', format(totRaise, ',.2f'),
                                                                                             sep='')
    print('The average of all the raises would be: $', format(Avg, ',.2f'),
                                                       sep='')
    print('The total faculty payroll before the raises is: $', format(totalB, ',.2f'),
                                                               sep='')
    print('The total faculty payroll after the raises would be: $', format(totalA, ',.2f'),
                                                                    sep='')
    
    
    
def developerInfo():
    print('Name:     Renee White')
    print('Program:  7')
    print()
      

main()

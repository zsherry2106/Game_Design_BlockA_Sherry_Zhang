#Sherry Zhang
#10/21/21

#Data Lockdown Challenge

import os
os.system('clear')

test_case = input("Enter # of tests: ")
count_test = 0
count_case = 0

if test_case.isdigit():
    test_case = int(test_case)

    while count_test < test_case:
        count_test += 1

        cases = int(input("Enter # of cases: "))

        websites = []
        check = []

        while count_case < cases:
            count_case += 1
            web = input("Enter a website and kilobytes: ")
            websites.append(web)
        
        for web in websites:
            web = web.split(" ")
            if int(web[1]) > 1000 and 'lmco' not in web[0]:
                check.append(web)

        print(check)


# web = web.split(" ")

# if int(web[1]) > 1000 and 'lmco' not in web[0]:
#     check.append(web)

#         print(check)
        



with open('BankChurners.csv') as f:

    lines = [x.split(',') for x in f.readlines()]

#getting indexes for the different columns
for x in range(len(lines[0])):
    if lines[0][x].strip(' \n"') == 'Customer_Age':
        customer_age_index = x
    elif lines[0][x].strip(' \n"') == 'Credit_Limit':
        credit_limit_index = x
    elif lines[0][x].strip(' \n"') == 'Months_on_book':
        months_on_book_index = x
    elif lines[0][x].strip(' \n"') == 'Total_Trans_Amt':
        transactions_index = x
        
#the loop where the bulk of my program will be 
while True:
    print('Hello welcome to your dataset')
    option = input('Which option would you like: 1 sort data or 2 find averages: ')
    
#If statements so the user can choose if they want to sort or average
    if option == '1':
        while True:
            option1 = input('Would you like to: 1 sort by least to most or 2 sort by most to least: ')
            if option1 != '1' and option1 != '2':
                print('Invalid option, try again')
                continue
            while True:
                option2 = input('Would you like to: 1 sort by transaction, 2 sort by months on books or 3 sort by credit limit: ')
                if option2 == '1':
                    if option1 == '1':
                        
                        #If user choices 1 it will run this line
                        lines = [lines[0]] + sorted(lines[1:], key = lambda x: int(x[transactions_index]))
                    else:
                        
                        #If user choices 2 it will run this line
                        lines = [lines[0]] + sorted(lines[1:], key=lambda x: int(x[transactions_index]), reverse=True)
                elif option2 == '2':
                    if option1 == '1':
                        
                        #If user choices 1 it will run this line
                        lines = [lines[0]] + sorted(lines[1:], key = lambda x: int(x[months_on_book_index]))
                    else:
                        
                        #If user choices 2 it will run this line
                        import pandas as pd
                        df = pd.read_csv('BankChurners.csv')
                        print(df.sort_values('Months_on_book',ascending  = False))
                elif option2 == '3':
                    if option1 == '1':
                        lines = [lines[0]] + sorted(lines[1:], key = lambda x: float(x[credit_limit_index]))
                    else:
                        print(df.sort_values('Credit_Limit',ascending  = False))
                else:
                    print('Invalid option, try again')
                    continue

                with open('BankChurners.csv', 'w') as f:
                    new_lines = [','.join(x) for x in lines]
                    f.write(''.join(new_lines))

                print('Successfully sorted')
                
                break
            break
            
            #this is where my option 2 happens
    elif option == '2':
        while True:
            option = input('Would you like to: 1 solve for average customer age, 2 solve average credit limit or 3 find average months on books: ')
            if option == '1':
                total = 0
                for row in lines[1:]:
                    total += int(row[customer_age_index])

                print(f'The average customer age is {round(total/len(lines[1:]))}')
            elif option == '2':
                total = 0
                for row in lines[1:]:
                    total += float(row[credit_limit_index])

                print(f'The average credit limit is {round(total/len(lines[1:]))}')
            elif option == '3':
                total = 0
                for row in lines[1:]:
                    total += int(row[months_on_book_index])

                print(f'The average months on book is {round(total/len(lines[1:]))}')
            else:
                print('Invalid option, try again')
                continue
            break
            
            #stop gag so when i type stop the program ends
    elif option.lower() == 'stop':
        print('Program successfully stopped')
        break
    else:
        print('Invalid option, restarting')

    print('')


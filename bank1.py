def account():
    print("Details of user")
    print('Name:','Harsh Rana')
    print('Account_Number:','300084176114566')
    print('Aaadhar_Number:','78480884777')
    print('Phone_Number:','9027097675')
    print('Category:','General')

def total_amount():
    balance=17000
    print("The total balance of your account is:",balance)

def deposit_withdrw():
    balance=17000
    amount=input("Enter the amount when you deposit:")
    total=balance+amount
    print("After deposit the",amount,"your total balane is:",total)
    amount=input("How many amount you withdrw:")
    if total>=amount:
        total-=amount
        print('After withdrw you total balance is:',total)        

    else:


        print("you have not money")



account()
total_amount()
deposit_withdrw()


'43527510ca1acd4a2f7d65e284b44f43'
"http://api.openweathermap.org/data/2.5/weather?"
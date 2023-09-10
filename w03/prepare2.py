print()
print("Welcome to the loan calculator!")
print("Please enter the following on a scale from 1-10")

loan_size = int(input("How large is the loan? "))
credit = int(input("How good is your credit history? "))
income = int(input("How high is your income? "))
down_payment = int(input("How large is your down payment? "))
decision_tf = False

if(loan_size >= 5):
    if(credit >= 7 and income >= 7):
        decision_tf = True          
    elif(credit >= 7 or income >= 7):
        if(down_payment >= 5):
            decision_tf = True
        else:
            decision_tf = False
    else:
        decision_tf = False
else:
    if(credit < 4):
        decision_tf = False
    else:
        if(income >= 7 or down_payment >= 7):
            decision_tf = True
        elif(income >= 4 and down_payment >= 4):
            decision_tf = True
        else:
            decision_tf = False

if decision_tf:
    print("Congratulations! Your application was approved!")
else:
    print("Sorry. Your application was rejected.")

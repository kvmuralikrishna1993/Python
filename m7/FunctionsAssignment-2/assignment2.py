'''# Assignment-2 - Paying Debt off in a Year
# Now write a program that calculates the minimum fixed monthly
payment needed in order pay off a credit card balance within 12 months.
# By a fixed monthly payment, we mean a single number which does not change each month,
but instead is a constant amount that will be
# paid each month.
# In this problem, we will not be dealing with a minimum monthly payment rate.
# The following variables contain values as described below:
# balance - the outstanding balance on the credit card
# annualInterestRate - annual interest rate as a decimal
# The program should print out one line: the lowest monthly payment
that will pay off all debt in under 1 year, for example:
# Lowest Payment: 180
# Assume that the interest is compounded monthly
according to the balance at the end of the month (after the payment for that month is
# made).
# The monthly payment must be a multiple of $10 and
is the same for all months. Notice that it is possible for the balance to become
# negative using this payment scheme, which is okay.
A summary of the required math is found below:
# Monthly interest rate = (Annual interest rate) / 12.0
# Monthly unpaid balance =
(Previous balance)-(Minimum fixed monthly payment)
# Updated balance each month =
(Monthly unpaid balance)+(Monthly interest rate x Monthly unpaid balance)'''
def payingdebtoffinayear_(bal_, annuminterst_):
    '''Calculation starts here'''
    if bal_ < 0:
        return 0
    paid_ = 10
    episilon = 0.5
    while True:
        mnth_ = 0
        bal2_ = bal_
        while mnth_ != 12:
            unbal_ = bal2_-(paid_)
            bal2_ = unbal_+(unbal_*annuminterst_/12)
            mnth_ = mnth_+1
        if bal2_ <= episilon:
            break
        paid_ = paid_+10
    return paid_
def main():
    '''Main starts here'''
    data = input()
    data = data.split(' ')
    data = list(map(float, data))
    print("Lowest Payment: "+ str(payingdebtoffinayear_(data[0], data[1])))
if __name__ == "__main__":
    main()

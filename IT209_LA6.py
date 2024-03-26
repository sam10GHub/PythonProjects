# IT209_LA6_inheritance_account_S24_ - Lab #6
# Name: Samuel Essandoh
# Given:  Account class and global test code (no changes)
# Create: CheckingAccount as a subclass of Account
#Purpose:This assignment requires you to create a subclass of a class called ‘Account’. It shows the use of inheritance,
#where the subclass CheckingAccount inherits functionality from the Account class
# CheckingAccount:
#    supplies its own 'interest' class variable with value .01
#    adds its own withdrawal_charge class variable with value 10
#    inherits the __init__, deposit, and printStatement methods
#                 and uses them as is (i.e. no changes)
#    overrides calcInterest by supplying its own method and doesn't
#                 use anything from the parent(uses its own
#                 interest rate).
#    overrides withdraw, but runs the parent method ('super()')
#                 while supplying its own 'amount' parameter
#                 (= amount + withdrawal_charge)
#------------------------------------------------------------------

# do not change the Account class code ----------------------------
class Account:
    interest = 0.02
    months = ['January', 'February', 'March', 'April', 'May', 'June',
              'July', 'August', 'September', 'October', 'November', 'December']
    # Reset these class variables to match the desired days and months for the
    #  indicated attribute or transaction
    month = '02'            # <== end statement will be for this month
    depDate = '02/27'       # <== test script will use this day for deposits
    withdrDate = '02/28'    # <== test script will use this day for withdrawals
    monthEnd = '02/29'      # <== end statement will use this as statement date
    def __init__(self, account_holder, acctType = 'Savings'):
        self.balance = 0.0
        self.holder = account_holder
        self.type = acctType
        interest = 0.02
        self.transactionLog = [ ]     # [date, type, amount, balance]
    def deposit (self, date, amount):
        self.balance += amount
        self.transactionLog.append([date, 'deposit', amount, self.balance])
        return self.balance
    def calcInterest(self):
        self.monthlyInterest = self.balance * Account.interest
        self.balance = self.balance + self.monthlyInterest
        return self.monthlyInterest, self.balance
    def withdraw (self, date, amount):
        if amount > self.balance:
            return 'Insufficient Funds'
        self.balance -= amount
        self.transactionLog.append([date, 'withdrawal', amount, self.balance])
        return self.balance
    def printStatement (self, month):
        print ('\nStatement for ', Account.months[int(month) - 1], ' ----------------------')
        print ('Account holder: ', self.holder, '   Type: ', self.type, '\n')
        print('{0:6s} {1:11s}   {2:8s}   {3:8s}'.format('Date', 'Transaction', 'Amount', 'Balance'))
        print('{0:6s} {1:11s}   {2:8s}   {3:8s}'.format('======', '===========', '========', '========='))
        for t in self.transactionLog:
            print('{0:6s} {1:10s}   ${2:8.2f}   ${3:8.2f}'.format(t[0], t[1], t[2], t[3]))
        a, b = self.calcInterest()
        print('\n{0:6s} {1:10s}   @{2:5.2f}      ${3:8.2f}'.format(Account.monthEnd, 'Interest', self.interest, a))
        print('{0:6s} Ending balance           ${1:8.2f}'.format(Account.monthEnd, b))
        print('-------------------------------------------------')


# Add your subclass code here:  --------------------------------------------

class CheckingAccount(Account):
    interest = 0.01
    withdrawal_charge = 10

    def calcInterest(self):
        self.monthlyInterest = self.balance * CheckingAccount.interest
        self.balance = self.balance + self.monthlyInterest
        return self.monthlyInterest, self.balance

    def withdraw(self, date, amount):
        amount += CheckingAccount.withdrawal_charge
        return super().withdraw(date, amount)



#   Global/Executable code follows - do not change this code ------------
input('\n\nHit "Enter" to set up a Saving Account --------------------\n')
a1 = Account('Jeff')
a1.deposit(Account.depDate, 1000)
print('\n', Account.depDate, ' depositing $1,000 for ', a1.holder, ', Balance: ', a1.balance)
# Expected output: the first withdrawal attempt should fail, the second should succeed
input('\nHit "Enter" to withdraw from this account ')
print (Account.withdrDate, ' withdrawing $1100 from: ', a1.holder,
       ', result: ', a1.withdraw(Account.withdrDate, 1100))
print (Account.withdrDate,' withdrawing $100 from ', a1.holder,
       '  , result:  account, balance: ', a1.withdraw(Account.withdrDate, 100))


input('\n\nHit "Enter" to set up a Checking Account ----------------\n')
c1 = CheckingAccount('Elizabeth', acctType = 'Checking')
c1.deposit(Account.depDate, 2000)
print('\n', Account.depDate, ' depositing $2,000 for ', c1.holder, ', Balance: ', c1.balance)
# Expected output: the first withdrawal attempt should fail, the second should succeed
#                  A withdrawal charge should be applied
input('\nHit "Enter" to withdraw from this account ')
print(Account.withdrDate, ' withdrawing $2100 from: ', c1.holder,
      ', result: ', c1.withdraw(Account.withdrDate, 2100))
print(Account.withdrDate, ' withdrawing $100 from ', c1.holder,
      '  , result:  checking, balance: ', c1.withdraw(Account.withdrDate, 100))

input('\n\nHit "Enter" to see monthly statements ---------------------\n')
# Expected output: accounts will show different interest rates, checking will show
#                  a withdrawal charge applied
# Both account class types use the same inherited 'printstatement()' method
a1.printStatement(Account.month)
c1.printStatement(Account.month)

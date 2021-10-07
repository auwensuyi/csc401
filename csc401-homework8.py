
class Bank:

    def __init__(self):
        
       self.atmList = []
       self.messages = []

        
    def message(self, atm_id, msg_text):
        '''
        Prints a message based on input from the ATM
        '''
        text = f"ATM ID: {atm_id}: {msg_text}"
        self.messages.append(text)
        print(text)

    def addATM(self, atm):
        self.atmList.append(atm)

class ATM:

    next_id = 1

    def __init__(self, bank, balance = 50000):
        '''
        <REPLACE WITH YOUR OWN DESCRIPTION>
        '''
        self.bank = bank
        self.balance = balance
        self.history = []
        self.atm_id = ATM.next_id
        ATM.next_id += 1
        self.bank.addATM(self)

    def __repr__(self):
        '''
        <REPLACE WITH YOUR OWN DESCRIPTION>
        '''
        return f"ATM({self.balance})"

    def deposit(self, user_id, deposit):
        '''
        <REPLACE WITH YOUR OWN DESCRIPTION>
        '''
        if deposit.type == "cash":
            self.balance += deposit.amount
        self.history.append(f'deposit,{user_id},{deposit.amount},{deposit.type}')

    def withdraw(self, user_id, amount):
        '''
        <REPLACE WITH YOUR OWN DESCRIPTION>
        '''
        success = True
        hist_text = f'withdraw,{user_id},{amount}' 
        if amount > 300:
            success = False
            error_text = 'Withdrawals over $300 are not permitted'
        elif amount > self.balance:
            success = False
            error_text = 'Withdrawal exceeds balance'
        else:
            success = True
            self.balance = self.balance - amount
        self.history.append(hist_text + f',{success}')
        if not success:
            raise ValueError(error_text)
        if self.balance < 1000:
            self.bank.message(self.atm_id, "Low balance")

class Deposit:
    '''
    A Deposit class that allows the creation of deposit objects with
    a string type and amount
    '''
    def __init__(self, string, amount):
        self.type = string
        self.amount = amount

class SubClassATM(ATM):
    '''
    A Sub class of ATM that does not accept checks
    '''
    def __init__(self, bank, balance):
        '''
        Initiailize by calling thr ATM constructor
        '''
        super().__init__(bank, balance)

    def deposit(self, user_id, deposit):
        '''
        Deposit function that does not accept checks
        '''
        if deposit.type == "check":
            raise ValueError("ATM does not accept checks")
        else:
            ATM.deposit(self, user_id, deposit)

if __name__ == '__main__':
    '''
    Week 7 tests.  Leave these in place.  Add new tests
    after tese tests.
    '''
    # 7.a creating an ATM with no parameter results in a balance of 50000
    my_bank = Bank()
    my_atm = ATM(my_bank)
    assert my_atm.balance == 50000

    # 7.b creating an ATM with a numeric parameter results in a balance of that amount
    my_atm = ATM(my_bank, 10000)
    assert my_atm.balance == 10000

    # 7.c calling deposit with N as the parameter results in a balance of old balance + N
    my_atm.deposit('user1', Deposit("cash",200))
    assert my_atm.balance == 10200
    
    # 7.d calling deposit results in expected string added to history
    assert 'deposit,user1,200,cash' in my_atm.history
    
    # 7.e withdrawing N dollars when N is less than or equal 300 and N is less than the balance, results in a balance of old balance - N.
    my_atm.withdraw('user1', 100)
    assert my_atm.balance == 10100
    
    # 7.f withdrawing N dollars when N is greater than 300 results in a raised exception with expected message
    try:
        my_atm.withdraw('user1', 500)
    except ValueError as e:
        assert str(e) == 'Withdrawals over $300 are not permitted'

    # 7.g withdrawing N dollars when N is greater than the current balance results in a raised exception with expected message
    atm2 = ATM(my_bank, 200)
    try:
        atm2.withdraw('user1', 250)
        assert False, 'should have raised a ValueError'
    except ValueError as e:
        assert str(e) == 'Withdrawal exceeds balance'
        
    # 7.h withdrawing successfully results in expected string added to history
    assert 'withdraw,user1,100,True' in my_atm.history
    
    # 7.i failed withdraw results in expected string added to history
    assert 'withdraw,user1,500,False' in my_atm.history
    
    # 7.j creating multiple ATM instances assigns atm_id to expected values (first ATM has atm_id = 1, 2nd one created has atm_id = 2, etc).
    assert my_atm.atm_id == 2
    assert atm2.atm_id == 3
    
    # 7.k creating multiple ATM instances updates ATM.next_id to expected value.
    assert ATM.next_id == 4

    # 8.ii
    assert my_atm in my_bank.atmList

    # 8.iv
    # last balance above was 10100
    assert my_atm.balance == 10100
    my_atm.deposit('user1', Deposit("check", 100))
    assert my_atm.balance == 10100

    low_atm = ATM(my_bank, 1100)
    low_atm.withdraw('user1', 200)
    text = f"ATM ID: {low_atm.atm_id}: Low balance"
    assert text in my_bank.messages
 


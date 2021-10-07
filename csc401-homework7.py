
class ATM:
    next_id = 1
    
    def __init__(self, balance = 50000):
        self.balance = balance
        self.history = []

        self.atm_id = ATM.next_id

        ATM.next_id += 1



    def deposit(self, user_id, amount):
        self.balance += amount

        self.history.append(f'deposit,{user_id},{amount}')


    def withdraw(self,user_id, amount):
        
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


    def __repr__(self):
        return("ATM({}))".format(self.balance))

    

    

    

    

    
        
                             
        
        

    
    

if __name__ == '__main__':
    '''
    ADD TESTS HERE
    '''
    
    # 7.a creating an ATM with no parameter results in a balance of 50000
    my_atm = ATM()
    assert my_atm.balance == 50000

    # 7.b creating an ATM with a numeric parameter results in a balance of that amount
    my_atm = ATM(10000)
    assert my_atm.balance == 10000

    # 7.c calling deposit with N as the parameter results in a balance of old balance + N
    my_atm.deposit('user1', 200)
    assert my_atm.balance == 10200
    
    # 7.d calling deposit results in expected string added to history
    assert 'deposit,user1,200' in my_atm.history
    
    # 7.e withdrawing N dollars when N is less than or equal 300 and N is less than the balance, results in a balance of old balance - N.
    my_atm.withdraw('user1', 100)
    assert my_atm.balance == 10100
    
    # 7.f withdrawing N dollars when N is greater than 300 results in a raised exception with expected message
    try:
        my_atm.withdraw('user1', 500)
    except ValueError as e:
        assert str(e) == 'Withdrawals over $300 are not permitted'

    # 7.g withdrawing N dollars when N is greater than the current balance results in a raised exception with expected message
    atm2 = ATM(200)
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

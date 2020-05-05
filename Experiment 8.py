class ATM:
    def _init_(self,acc_no,phone_no,pin_no,bal,names):
            self.acc_no = acc_no
            self.phone_no = phone_no
            self.pin_no = pin_no
            self.bal = bal
            self.name=names
    def entry(self):
        print('Welcome to the ATM')
        count = 0
        for count in range(4):
                if(count==3):
                    print('Your account has been blocked.')
                    break
                self.pin_no=p=int(input('Enter your pin '))
                if(p<1000 or p>9999):
                    print('Please enter valid 4 digit pin')
                    count+=1
                    continue
                if(p not in pin_no):
                    print('Invalid pin, try again')
                    count+=1
                    continue
                else:
                    for i in range(len(pin_no)):
                        if (pin_no[i] == p):
                            n = i
                            self.acc_no = acc_no[n]
                            self.phone_no = phone_no[n]
                            self.bal = bal[n]
                            self.name = names[n]

                            opt = {'Account Information': 1, 'Pin Change': 2, 'Balance Enquiry': 3, 'Withdrawal': 4,
                                   'Deposit': 5}
                            print('What would you like to do today? ', opt)
                            c = int(input('Enter choice: '))
                            if c not in [1, 2, 3, 4, 5]:
                                print('Enter valid choice')
                            else:
                                if (c == 1):
                                    s.ac_info()
                                if (c == 2):
                                    s.pin_change()
                                if (c == 3):
                                    s.bal_enq()
                                if (c == 4):
                                    s.withdraw()
                                if (c == 5):
                                    s.deposit()
                    break

    def ac_info(self):
        print('Account holder: ',self.name)
        print('Account Number: ',self.acc_no)
        print('Phone Number: ', self.phone_no)
    def pin_change(self):
        new_p=int(input('Enter new 4 digit pin: '))
        self.pin=new_p
        print('Pin changed successfully')
    def bal_enq(self):
        print("Available balance: ",self.bal)
    def withdraw(self):
        amt=int(input('Enter amount to be withdrawn: '))
        if(amt>self.bal):
            print('Insufficient balance')
        else:
            self.bal=self.bal-amt
            print('Please collect your cash!')
            print('Your updated balance is ', self.bal)
    def deposit(self):
        dep=int(input('Enter amount to be deposited: '))
        self.bal=self.bal+dep
        print('Amount deposited successfully!')
        print('Your updated balance is ', self.bal)


accinfo = {1: ('Nikhil', 467835489013, 8865437209, 4536, 5000000), 2: ('Anuj', 47625363297, 9874526450, 3546, 100000),
           3: ('Sachin', 47453628690, 7684526578, 9856, 45978), 4: ('Samyak', 46589035247, 9845624609, 8761, 76345)}
names=[]
acc_no=[]
phone_no=[]
pin_no=[]
bal=[]
for a, b, c, d, e in accinfo.values():
    names.append(a)
    acc_no.append(b)
    phone_no.append(c)
    pin_no.append(d)
    bal.append(e)

s=ATM()
s.entry()



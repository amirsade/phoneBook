def add_contact(name,phone):
    contacts.append([name,phone])
    return contacts
def list_all():
  for i in contacts:
    print(i)
    if i==contacts[-1]:
        print('I show\'ed you all contacts\n')
        input('Press enter to back menu: ')
        break
def search_by_name(name,phone):
    c = 0
    for i in contacts_read:
        if i[0] == name:
            print(f'Your Indentifier is here , This is your contact: {contacts_read[c]}')
            input('Click Enter to Continue')
            print()
            break
        c+=1
        if i[1]==phone:
            if i[0]!=name:
                print('I dont have This name but I have This number')
                input('If you change and edit contact press enter to back menu and click number 2: ')
                print()
                break
        if i == contacts_read[-1]:
            if i!=[name,phone]:
                print('I dont have your contact')
                print('If you want Join my Phonebook with click number 1 from my page')
                input('for back to menu press enter: ')
                print()
                break
def save_contacts():
    if contacts != None:
        for i in contacts:
            infor1.write(i[0])
            infor1.write(',')
            infor1.write(i[1])
            infor1.write(',')
    return
def load_contacts():
    print('{0:*^100}\n'.format('Your History Contacts:'))
    for c in contacts_read:
        if c[1]:
            c[1]=int(c[1])
            print(c)
    print('{0:^100}'.format('//  \\\ '))
    input('Click Enter For Operation: ')
import os
contacts = []
contacts_read= []
if os.path.isfile('Contacts.csv'):
    with open('Contacts.csv','r+') as infor1:
        a = infor1.read()
        a = a[1:-1]
        a = a.split(',')
        c=0
        for line in a:
            if c==1 or c%2==1:
                contacts_read.append([a[c-1],a[c]])
            c+=1
        load_contacts()
with open('Contacts.csv','a+') as infor1:
    while True:
        print('{0:*^50}'.format('Your Welcome!'))
        print('''{0:*^50}'''.format('''This is a Phonebook for all of you,
        so enjoy with Choose below numbers:\n
        for Choose number1, Click(1)= Create New Member\n
        for Choose number2, Click(2)= Change dtails ForExample(Name or Phone)\n
        for Choose number3, Click(3)= SearchList\n
        for Choose number4, Click(4)= ShowList\n
        for Choose number5 = Press enter to Exit\n
        for Choose number6, Click(6)= Remove contact\n'''))
        print('\-----------------------------------------------------------/')
        num = input('Enter one of number: ')
        if  (num=='') or (num.isalpha()):
            print('You have Click Nothing or choose AlphaBet and Finish your Operations')
            break
        if int(num) == 1:
            name = input('Whats your name?: ')
            print()
            number = input('Enter your phone: ')
            print()
            c = 0
            if number == '' or name == '':
                print('Your not enter name or number!!')
                print()
            if number!='' and name!='':
                if number[0]!='0':
                    for i in number:
                        c+=1
                    if contacts_read!=None:
                        for i in contacts_read:
                            if i[0]==name or i[1]==number:
                                print('You this contact and repeat again!')
                                break
                    while c<11:
                        if len(number)>=11:
                            add_contact(name,number)
                            print('Your operations are successfully Completed')
                            input('Click enter for Choose Another number:')
                            print()
                            break
                        number = input('''Your phone number must have 11 digits Try again,
                        or Click Enter to Exit: ''')
                        if number=='':
                            print('You dont Write and just press enter: ')
                            break
                    else:
                        add_contact(name,number)
                        print('Your operations are successfully Completed')
                        input('Click Enter for Choose Another number:')
                        print()
                if number[0] == '0':
                    print('Your number is start with 0 and is Wrong!')
                    input('press enter for back to menu and begin of first operation: ')
                    print()
        if int(num) == 2:
            namePast = input('Enter your name: ')
            numberPast = input('Enter your phoneNumber: ')
            n = 0
            p = 0
            for i in contacts:
                if i[0] == namePast:
                    number1 = input('Enter new phone: ')
                    contacts[n]=[namePast,number1]
                    print(f'''Your Identifer {contacts[n]} Change successfully! '\n' ''')
                    input('Click Enter to Continue')
                    print()
                    break
                n+=1
            for i in contacts:
                if i[1] == numberPast:
                    name1 = input('Enter new name: ')
                    contacts[p]=[name1,numberPast]
                    print(f'''Your Identifer({contacts[p]}) Change successfully!'\n' ''')
                    input('Click Enter to back Choose Number:')
                    print()
                    break
                p+=1
        if int(num) == 3:
            is_name = input('What is that name?: ')
            is_number = input('What is that number?: ')
            search_by_name(is_name,is_number)
        if int(num) == 4:
            list_all()
        if int(num) == 6:
            is_name = input('What is that name: ')
            c = 0
            for i in contacts_read:
                if i[0]==is_name:
                    contacts.remove(contacts_read[c])
                    print('Your contact is delete successfully')
                    input('Click enter for back to menu: ')
                    print()
                    break
                c+=1
        if int(num)==5:
            break
    if contacts != None:
        save_contacts()         
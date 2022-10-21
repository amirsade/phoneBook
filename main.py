import csv
class PhoneBook:
    file = 'Phone_Book.csv'
    header =('F_name','L_name','Phone','Birth_y')
    def __init__(self,first,last,phone,birth_year):
        self.__first_name = first
        self.__last_name = last
        self.__phone = phone
        self.__birth_year=birth_year
        self.tuple_id = tuple()
        self.list_id = []
        self.tuple_id+=(self.__first_name,self.__last_name,self.__phone,self.__birth_year)
        self.list_id.append(self.tuple_id)
    def add(self):
        if PhoneBook.file ==None:
            with open (PhoneBook.file,'w',newline='') as new_file:
                    write = csv.writer(new_file)
                    write.writerow(PhoneBook.header)
                    for line in PhoneBook.contacts:
                        write.writerow(line)
        else:
            with open(PhoneBook.file,'a',newline = '') as new_file:
                contact = csv.writer(new_file)
                conts=[]
                with open(PhoneBook.file,'r')as new_file2:
                    for line in new_file2:
                        line = line[:-1]
                        cont_read = tuple(line.split(','))
                        conts.append(cont_read)    
                for i in self.list_id:
                    if i not in conts:
                        contact.writerow(self.list_id[0])     
    def search(self,first_name,last_name):
        with open(PhoneBook.file)as new_file2:
            conts = []
            for line in new_file2:
                line = line[:-1]
                cont_read = tuple(line.split(','))
                conts.append(cont_read)
            for i in range(len(conts)):
                if conts[i][0]==first_name and conts[i][1]==last_name:
                    print(f'{conts[i]} This is your identity in my contacts')
                if i == conts[-1] and conts[i][0]!=first_name:
                    print('==You have not Id in my contacts==')
    def change_id(self,first_name,last_name):
        conts = []
        with open(PhoneBook.file)as new_file2:
            for line in new_file2:
                line = line[:-1]
                cont_read = tuple(line.split(','))
                conts.append(cont_read)
            for i in range(len(conts)-1):
                if conts[i][0]==first_name and conts[i][1]==last_name:
                    print(f'I have your id== {conts[i]}')
                    f_name , l_name, phone , b_year = input('Enter f_name,l_name,Phone,b_year: ').split(',')
                    conts[i] = (f_name,l_name,phone,b_year)
                    print(f'Your Id are change now!={conts[i]}')
        with open (PhoneBook.file,'w',newline='') as new_file:
            contact = csv.writer(new_file)
            for i in conts:
                contact.writerow(i)
    def remove(self,first_name,last_name):
        conts = []
        with open(PhoneBook.file)as new_file2:
            for line in new_file2:
                line = line[:-1]
                cont_read = tuple(line.split(','))
                conts.append(cont_read)
            for i in range(len(conts)-1):
                if conts[i][0]==first_name and conts[i][1]==last_name:
                    del conts[i]
        with open(PhoneBook.file,'w',newline='') as new_file:
            contact = csv.writer(new_file)
            for i in conts:
                contact.writerow(i)
    def show_list(self):
        with open(PhoneBook.file)as new_file2:
            read_cont = [row for row in csv.DictReader(new_file2)]
            print(read_cont)
while True:
    print('{0:*^50}'.format('Your Welcome!'))
    print('''{0:*^50}'''.format('''This is a Phonebook for all of you,
    so enjoy with Choose below numbers:\n
    for Choose number1, Click(1)= Add New Member\n
    for Choose number2, Click(2)= Search Id Member\n
    for Choose number3, Click(3)= Change Id Member\n
    for Choose number4, Click(4)= Remove Id Member\n
    for Choose number5, Click(5)= Show list Members\n'''))
    try:
        num = int(input('Enter number: '))
        if num == 1:
            first_name,last_name,phone,birth_year = input('Enter your First_name(,)Last_name(,)Phone(,)Birth_year= ').split(',')
            person = PhoneBook(first_name , last_name , phone , birth_year)
            person.add()
        if num == 2:
            first_name,last_name,phone,birth_year = input('Enter your First_name(,)Last_name(,)Phone(,)Birth_year= ').split(',')
            person = PhoneBook(first_name , last_name , phone , birth_year)
            person.search(first_name , last_name)
        if num == 3:
            first_name,last_name,phone,birth_year = input('Enter your First_name(,)Last_name(,)Phone(,)Birth_year= ').split(',')
            person = PhoneBook(first_name , last_name , phone , birth_year)
            person.change_id(first_name , last_name)
        if num == 4:
            first_name,last_name,phone,birth_year = input('Enter your First_name(,)Last_name(,)Phone(,)Birth_year= ').split(',')
            person = PhoneBook(first_name , last_name , phone , birth_year)
            person.remove(first_name , last_name)
        if num == 5:
            first_name,last_name,phone,birth_year = input('Enter your First_name(,)Last_name(,)Phone(,)Birth_year= ').split(',')
            person = PhoneBook(first_name , last_name , phone , birth_year)
            person.show_list()
    except ValueError:
        print('You did not enter anything or you entered incomplete values!')
        a = input('if you want exit click (v) if not click (Enter): ')
        if a.upper()=='V':
            break
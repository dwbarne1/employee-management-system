class Employee:
    """Creates employee object with name and id"""
    def __init__(self, name, eid):
        self.__name = name
        self.__eid = eid

    @property
    def name(self):
        return self.__name.capitalize()

    @name.setter
    def name(self, new):
        if new.isalpha():
            self.__name = new
        else:
            self.__name = 'Unknown'

    @property
    def eid(self):
        return self.__eid.zfill(4)

    @eid.setter
    def eid(self, new):
        if len(new) == 0:
            self.__eid = '9999'
        else:
            self.__eid = new

    def __str__(self):
        return f'{self.eid}: {self.name}'


class Manager(Employee):
    """Creates manager object by inheriting employee name and id,
    as well as adding to and printing a subordinates list"""
    def __init__(self, name, eid, subordinates=None):
        super().__init__(name, eid)
        if subordinates is None:
            self.subordinates = list()
        else:
            self.subordinates = subordinates

    def add_subordinate(self):
        sub_name = input('Enter subordinate name: ')
        sub_id = input('Enter subordinate ID: ')
        temp = Employee(sub_name, sub_id)
        temp.name = sub_name
        temp.eid = sub_id
        self.subordinates.append(temp)

    def print_subordinates(self):
        for sub in self.subordinates:
            print(f'\t{sub}')


def main():
    """main method"""
    employees = []
    print('\t\t\tEmployee Management System')
    print('\nAdding Employees...')
    while True:
        employees.append(add_employee())
        answer = input('Do you want to enter more? ')
        if answer == 'N'.casefold():
            break
    print('\nPrinting Employee List')
    for employee in employees:
        print(employee)
        if isinstance(employee, Manager):
            print(f'\t{employee.name}\'s Employees')
            employee.print_subordinates()


def add_employee():
    """Adds employee and puts it in the employees list"""
    emp_name = input('\nEnter name: ')
    emp_id = input('Enter ID: ')
    answer = input('Is the employee a manager? (Y/N) ')
    if answer.upper() == 'Y':
        temp = Manager(emp_name, emp_id)
        temp.name = emp_name
        temp.eid = emp_id
        try:
            num_of_subs = int(input('How many subordinates? '))
            for i in range(num_of_subs):
                temp.add_subordinate()
        except:
            print('Invalid value')
    else:
        temp = Employee(emp_name, emp_id)
        temp.name = emp_name
        temp.eid = emp_id
    return temp


if __name__ == "__main__":
    main()

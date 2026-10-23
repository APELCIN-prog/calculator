class Employee:
    def __init__(self, salary):
        super().__init__()
        self.salary = salary

    def check_salary(self):
        return self.salary

class Manager(Employee):
    def __init__(self, salary, count_projects, bonus):
        super().__init__(salary)
        self.count_projects = count_projects
        self.bonus = bonus

    def check_salary(self):
        return self.salary + (self.count_projects * self.bonus)

class Developer(Employee):
    def __init__(self, salary, count_projects, bonus, status="Junior"):
        super().__init__(salary)
        self.count_projects = count_projects
        self.bonus = bonus
        self.status = status

    def check_salary(self):
        if self.status == "Junior":
            return self.salary + (self.count_projects * self.bonus * 1.2)
        elif self.status == "Middle":
            return self.salary + (self.count_projects * self.bonus * 1.5)
        elif self.status == 'Senior':
            return self.salary + (self.count_projects * self.bonus * 2)
        else:
            return self.salary + (self.count_projects * self.bonus)


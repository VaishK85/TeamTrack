# employee.py

class Employee:
    def __init__(self, name, employee_id, joining, designation, promoted_to, salary, bonus, department, email):
        self.name = name
        self.employee_id = employee_id
        self.joining = joining
        self.designation = designation
        self.promoted_to = promoted_to
        self.salary = salary
        self.bonus = bonus
        self.department = department
        self.email = email

    def info(self):
        return (
            f"🆔 Employee ID   : {self.employee_id}\n"
            f"👤 Name          : {self.name}\n"
            f"🏢 Department    : {self.department}\n"
            f"📧 Email         : {self.email}\n"
            f"📅 Joining Date  : {self.joining}\n"
            f"💼 Designation   : {self.designation}\n"
            f"🚀 Promoted To   : {self.promoted_to}\n"
            f"💰 Salary        : {self.salary}\n"
            f"🎁 Bonus         : {self.bonus}"
        )

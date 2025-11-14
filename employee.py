class Employee:
    def __init__(self, emp_id=None, name=None, dept=None, email=None, password=None):
        self.emp_id = emp_id
        self.name = name
        self.dept = dept
        self.email = email
        self.password = password

class Performance:
    def __init__(self, perf_id=None, emp_id=None, task=None, rating=None, remarks=None, date=None):
        self.perf_id = perf_id
        self.emp_id = emp_id
        self.task = task
        self.rating = rating
        self.remarks = remarks
        self.date = date

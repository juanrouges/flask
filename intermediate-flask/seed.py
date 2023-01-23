# having issues seeding file thru the terminal, ask mentor

"""Create sample data for db"""

from models import db, Employee, Department
from app import app

# create all tables
db.drop_all()
db.create_all()

# create sample employees
juan = Employee(name="Juan Rojas", province="ON", department="dsng", salary="120000.85")
carolina = Employee(name="Carolina Alvarado", province="PE", department="hr", salary="900200.95")
martina = Employee(name="Martina Rojas-Alvarado", province="BC", department="mrktng", salary="68200.85")
lucas = Employee(name="Lucas Wood", province="ON", department="mrktng", salary="62000.15")

# create sample departments
marketing = Department(dept_code="mrktng", dept_name="Marketing", dept_phone="18669874596")
human_resources = Department(dept_code="hr", dept_name="Human Resources", dept_phone="18884568975")
design = Department(dept_code="dsng", dept_name="Design", dept_phone="4167895686")


# save employees first
db.session.add_all([juan, carolina, martina, lucas])
db.session.commit()

# save departments second
db.session.add_all([marketing, human_resources, design])
db.session.commit()


from flask import Flask, render_template, redirect, flash
from models import db, connect_db, Employee, Department
from forms import EmployeeForm
from resources import UnitedStates

app = Flask(__name__)
app.app_context().push()

app.config["SQLALCHEMY_DATABASE_URI"]         = "postgresql:///luckylotus"
app.config["SECRET_KEY"]                      = "irulinosvision8976"
app.config["DEBUG"]                           = False
app.config["TEMPLATES_AUTO_RELOAD"]           = True
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"]  = False
app.config["DEBUG_TB_INTERCEPT_REDIRECTS"]    = False
app.config["SQLALCHEMY_ECHO"]                 = False

connect_db(app)

# staff_choices=[("", ""), ('1', 'John Thomas'), ('2', 'Chris Davis'), ('3', 'Lyn Taco')]

@app.route("/")
def index():
  return render_template("index.html")

@app.route("/employees")
def employees():
  employees = Employee.query.all()
  return render_template("employees.html", employees=employees)

@app.route("/employees/new", methods=["GET", "POST"])
def employee_new():
  form = EmployeeForm()
  all_depts = Department.query.all()
  depts = [(dept.dept_code, dept.dept_name) for dept in all_depts]
  form.department.choices = depts
  form.province.choices = UnitedStates.states
  if form.validate_on_submit():
    name = form.name.data
    province = form.province.data
    department = form.department.data
    salary = form.salary.data
    employee_new = Employee(name=name, province=province, department=department, salary=salary)
    db.session.add(employee_new)
    db.session.commit()
    flash(f"{name} was added to company employee directory under {department} department")
    return redirect("/employees")
  else:
    return render_template("employee_form.html", form=form)

@app.route("/employees/<int:employee_id>/edit", methods=["GET", "POST"])
def edit_employee(employee_id):
  employee = Employee.query.get_or_404(employee_id)
  form = EmployeeForm(obj=employee)
  all_depts = Department.query.all()
  depts = [(dept.dept_code, dept.dept_name) for dept in all_depts]
  form.department.choices = depts
  form.province.choices = UnitedStates.states
  if form.validate_on_submit():
    employee.name = form.name.data
    employee.province = form.province.data
    employee.department = form.department.data
    employee.salary = form.salary.data
    db.session.commit()
    return redirect("/employees")
  else:
    return render_template("employee_edit.html", form=form)

@app.route("/about")
def about():
  return render_template("about.html")
"""Create sample data for db"""

from models import db, Todo
from app import app

# create all tables
db.drop_all()
db.create_all()

# create sample todos
one = Todo( title="Make lasagna for dinner", done=True)
two = Todo( title="Feed indigo and Julieta")
three = Todo( title="Doctor's appointment at the hospital")
four = Todo( title="Have fun with the family", done=True)
five = Todo( title="Watch the movie The Way Of Water")

# save todos
db.session.add_all([one, two, three, four, five])
db.session.commit()


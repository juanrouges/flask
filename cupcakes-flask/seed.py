"""Create sample data for db"""

from models import db, Cupcake
from app import app

# create all tables
db.drop_all()
db.create_all()

# create sample cupcakes
one = Cupcake(flavor="Chocolate Pecan Lava", 
              size="Large",
              rating=4.2,
              image="https://picsum.photos/400"
             )

two = Cupcake(flavor="Pink Lemonade Vanilla Dream", 
              size="Medium",
              rating=3.8,
             )

three = Cupcake(flavor="White Belgium Chocolate", 
              size="Small",
              rating=4.8,
             )

four = Cupcake(flavor="Apple Cinnamon Carnaval", 
              size="Large",
              rating=3.6,
              image="https://picsum.photos/400"
             )

five = Cupcake(flavor="Cosmic Rouge Velvet Delight", 
              size="Xlarge",
              rating=4.9
             )

# save cupcakes
db.session.add_all([one, two, three, four, five])
db.session.commit()


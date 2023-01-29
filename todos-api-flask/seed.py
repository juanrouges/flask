# having issues seeding file thru the terminal, ask mentor

"""Create sample data for db"""

from models import db, Pet
from app import app

# create all tables
db.drop_all()
db.create_all()

# Get a categorical image from: cat, dog, bird, bug, tiger, lion, fish

# create sample employees
bandit = Pet( name="Bandit", 
              species="Tiger", 
              photo_url="https://wildcard.codestuff.io/tiger/250/250", 
              age="12",
              notes="Lovable pet tiger that's been around for 12 years.",
              available=False
            )
roberta = Pet( name="Roberta", 
               species="Bird", 
               photo_url="https://wildcard.codestuff.io/bird/250/250", 
               age="3",
               notes="Playful birdy that will amuse you every day with silly antics."
              )
maxi = Pet( name="Maxi", 
            species="Cat", 
            photo_url="https://wildcard.codestuff.io/cat/250/250", 
            age="1",
            notes="Maxi is a chill house cat looking for similar company :).",
            available=False
          )
spots = Pet( name="Spots", 
             species="Dog", 
             photo_url="https://wildcard.codestuff.io/dog/250/250", 
             age="2",
             notes="Energetic is his last name and he will give you a run for your money, looking for an electric partner to get into mischief with."
            )


# save employees first
db.session.add_all([bandit, roberta, maxi, spots])
db.session.commit()


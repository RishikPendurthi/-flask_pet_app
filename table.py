from app import db, Pet

# Add some pet entries
pet1 = Pet(name="Buddy", species="Dog", age=4)
pet2 = Pet(name="Mittens", species="Cat", age=2)
pet3 = Pet(name="Goldie", species="fish", age=1)
pet4 = Pet(name="Charlie", species="parrot", age=3)

# Add to session
db.session.add(pet1)
db.session.add(pet2)
db.session.add(pet3)

# Commit to the database
db.session.commit()

from basic import db, Puppy

##CREATE

my_puppy = Puppy('Rufus', 5)
my_puppy1 = Puppy('Halima',4)

db.session.add_all([my_puppy,my_puppy1])
db.session.commit()

#READ

all_puppies = Puppy.query.all() #list of all objects in the table
print(all_puppies)

#SELECT by ID

puppy_one = Puppy.query.get(1)
print(puppy_one.name)


#FILTERS
puppy_frankie = Puppy.query.filter_by(name='Frankie')
print(puppy_frankie.all())


###UPDATE
first_puppy = Puppy.query.get(1)
first_puppy.age = 10

db.session.add(first_puppy)
db.session.commit()


##DELETE
second_puppy = Puppy.query.get(2)
db.session.delete(second_puppy)
db.session.commit()


#PRINT OUT TABLES
all_puppies = Puppy.query.all()
print(all_puppies)
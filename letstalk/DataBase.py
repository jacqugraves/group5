
from google.appengine.ext import ndb	

commentary=
class DTopic(ndb.Model):
	Topic = ndb.KeyProperty(required=True)
	Category = ndb.KeyProperty(required=True, default='Misc')
	Comments = ndb.ListProperty() 
	





	class MyEntity(db.Model):
    dictionary_string = db.StringProperty()

payload = {{}...{}}

# Store dict
my_entity = MyEntity(key_name=your_key_here)
my_entity.dictionary_string = str(payload)
my_entity.put()

# Get dict
import ast
my_entity_k = db.Key.from_path('MyEntity', your_key_here)
my_entity = db.get(my_entity_k)
payload = ast.literal_eval(my_entity.dictionary_string)


lass User(db.Model):
   movie_list=db.ListProperty(db.Key)



michigan_query = Student.query().filter(Student.university == "U. Mich.")
michigan_students = student_query.fetch()

# Arbitrarily consider the first result. This will fail if the query returned
# no entities.
michigan_transfer = michigan_students[0]
michigan_transfer.university = "Michigan State"
michigan_transfer.put()
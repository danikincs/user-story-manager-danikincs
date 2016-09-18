from models import *

db.connect()
db.drop_table(UserStory)
print("tables drop")
db.create_tables([UserStory], safe=True)
print("table create")

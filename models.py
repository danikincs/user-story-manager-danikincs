from peewee import *

db = PostgresqlDatabase("svindler", "svindler")


class BaseModel(Model):  # Main Class with the database connection.
    """A base model that will use our Postgresql database"""

    class Meta:
        database = db


class UserStory(BaseModel):
    story_title = CharField(null=False)
    user_story = CharField(null=False)
    acceptance_criteria = CharField()
    business_value = FloatField()
    estimation = FloatField()
    status = CharField(default='Planning')

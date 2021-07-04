from peewee import BooleanField, CharField, DateTimeField, Model, TextField

from lifeguard_peewee.connection import connection_factory

DATABASE = connection_factory()


class ValidationModel(Model):
    """
    Validation Model
    """

    class Meta:
        """
        Base Model Meta
        """

        database = DATABASE
        db_table = "validations"

    validation_name = CharField(unique=True)
    status = CharField()
    details = TextField()
    settings = TextField()
    last_execution = DateTimeField()


class NotificationModel(Model):
    """
    Notification Model
    """

    class Meta:
        """
        Base Model Meta
        """

        database = DATABASE
        db_table = "notifications"

    validation_name = CharField(unique=True)
    thread_ids = TextField()
    is_opened = BooleanField()
    options = TextField()
    last_execution = DateTimeField()


DATABASE.create_tables([ValidationModel, NotificationModel])

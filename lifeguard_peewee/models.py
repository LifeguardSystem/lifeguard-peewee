from peewee import BooleanField, CharField, DateTimeField, Model, TextField

from lifeguard_peewee.context import connection_factory


class ValidationModel(Model):
    """
    Validation Model
    """

    class Meta:
        """
        Base Model Meta
        """

        database = connection_factory()
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

        database = connection_factory()
        db_table = "notifications"

    validation_name = CharField(unique=True)
    thread_ids = TextField()
    is_opened = BooleanField()
    options = TextField()
    last_execution = DateTimeField()

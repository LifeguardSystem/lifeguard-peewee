import unittest

from lifeguard_peewee.settings import (
    SETTINGS_MANAGER,
    LIFEGUARD_PEEWEE_DBMS_NAME,
    LIFEGUARD_PEEWEE_HOST,
    LIFEGUARD_PEEWEE_PORT,
    LIFEGUARD_PEEWEE_USER,
    LIFEGUARD_PEEWEE_PASSWORD,
    LIFEGUARD_PEEWEE_DATABASE,
)


class SettingsTest(unittest.TestCase):
    def test_lifeguard_peewee_dbms_name(self):
        self.assertEqual(LIFEGUARD_PEEWEE_DBMS_NAME, "mysql")
        self.assertEqual(
            SETTINGS_MANAGER.settings["LIFEGUARD_PEEWEE_DBMS_NAME"]["description"],
            "DBMS name",
        )

    def test_lifeguard_peewee_host(self):
        self.assertEqual(LIFEGUARD_PEEWEE_HOST, "localhost")
        self.assertEqual(
            SETTINGS_MANAGER.settings["LIFEGUARD_PEEWEE_HOST"]["description"],
            "DBMS host",
        )

    def test_lifeguard_peewee_port(self):
        self.assertEqual(LIFEGUARD_PEEWEE_PORT, 3306)
        self.assertEqual(
            SETTINGS_MANAGER.settings["LIFEGUARD_PEEWEE_PORT"]["description"],
            "DBMS port",
        )

    def test_lifeguard_peewee_user(self):
        self.assertEqual(LIFEGUARD_PEEWEE_USER, "user")
        self.assertEqual(
            SETTINGS_MANAGER.settings["LIFEGUARD_PEEWEE_USER"]["description"],
            "DBMS user",
        )

    def test_lifeguard_peewee_password(self):
        self.assertEqual(LIFEGUARD_PEEWEE_PASSWORD, "password")
        self.assertEqual(
            SETTINGS_MANAGER.settings["LIFEGUARD_PEEWEE_PASSWORD"]["description"],
            "DBMS password",
        )

    def test_lifeguard_peewee_database(self):
        self.assertEqual(LIFEGUARD_PEEWEE_DATABASE, "db")
        self.assertEqual(
            SETTINGS_MANAGER.settings["LIFEGUARD_PEEWEE_DATABASE"]["description"],
            "DBMS database name",
        )

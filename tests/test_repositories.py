from datetime import datetime
import unittest
from unittest.mock import patch, MagicMock

from lifeguard.validations import ValidationResponse
from lifeguard_peewee.models import ValidationModel
from lifeguard_peewee.repositories import (
    PeeweeNotificationRepository,
    PeeweeValidationRepository,
)


class TestPeeweeValidationRepository(unittest.TestCase):
    def setUp(self):
        self.repository = PeeweeValidationRepository()

    @patch("lifeguard_peewee.repositories.ValidationModel")
    def test_fetch_last_validation_result_none(self, mock_model):
        validation_name = "validation"
        mock_model.get.return_value = None

        result = self.repository.fetch_last_validation_result(validation_name)

        self.assertIsNone(result)

    @patch("lifeguard_peewee.repositories.ValidationModel")
    def test_fetch_last_validation_result_not_none(self, mock_model):
        validation_name = "validation"
        mock_model.get.return_value = ValidationModel(
            validation_name="validation",
            status="status",
            details="{}",
            settings="{}",
            last_execution=datetime(2020, 11, 19),
        )

        result = self.repository.fetch_last_validation_result(validation_name)

        self.assertEqual(result.status, "status")
        self.assertEqual(result.details, {})
        self.assertEqual(result.settings, {})
        self.assertEqual(result.last_execution, datetime(2020, 11, 19))

    @patch("lifeguard_peewee.repositories.ValidationModel")
    def test_save_validation_result_create(self, mock_model):

        return_where = MagicMock("return_where")
        return_where.count.return_value = 0

        return_select = MagicMock("return_select")
        return_select.where = MagicMock(name="where")
        return_select.where.return_value = return_where

        mock_model.select.return_value = return_select

        response = ValidationResponse("name", "status", {})

        self.repository.save_validation_result(response)

        mock_model.create.assert_called_with(
            validation_name="name",
            status="status",
            details="{}",
            settings="{}",
            last_execution=None,
        )

    @patch("lifeguard_peewee.repositories.ValidationModel")
    def test_save_validation_result_update(self, mock_model):
        return_where = MagicMock("return_where")
        return_where.count.return_value = 1

        return_select = MagicMock("return_select")
        return_select.where = MagicMock(name="where")
        return_select.where.return_value = return_where

        response = ValidationResponse("name", "status", {})

        self.repository.save_validation_result(response)

        mock_model.update.assert_called_with(
            validation_name="name",
            status="status",
            details="{}",
            settings="{}",
            last_execution=None,
        )

    @patch("lifeguard_peewee.repositories.ValidationModel")
    def test_fetch_all_validation_results_not_none(self, mock_model):
        mock_model.select.return_value = [
            ValidationModel(
                validation_name="validation",
                status="status",
                details="{}",
                settings="{}",
                last_execution=datetime(2020, 11, 19),
            )
        ]

        result = self.repository.fetch_all_validation_results()

        self.assertEqual(result[0].validation_name, "validation")
        self.assertEqual(result[0].status, "status")
        self.assertEqual(result[0].details, {})
        self.assertEqual(result[0].settings, {})
        self.assertEqual(result[0].last_execution, datetime(2020, 11, 19))


class TestPeeweeNotificationRepository(unittest.TestCase):
    def setUp(self):
        self.repository = PeeweeNotificationRepository()

    # TODO implement all tests

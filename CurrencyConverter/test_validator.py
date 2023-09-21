from django.test import TestCase
from .validator.validator import CurrencyConverterValidator

class CurrencyConverterValidatorTestCase(TestCase):
    validator = CurrencyConverterValidator()

    def test_is_get_request_data_valid(self):
        test_source_1 = "USD"
        test_source_2 = "EUR"
        test_source_3 = 777

        test_target_1 = "USD"
        test_target_2 = "EUR"
        test_target_3 = 777

        test_amount_1 = "$123,456,789"
        test_amount_2 = "$123,4444"
        test_amount_3 = "$1"

        is_valid_1 = self.validator.is_get_request_data_valid(test_source_1, test_target_1, test_amount_1)
        is_valid_2 = self.validator.is_get_request_data_valid(test_source_2, test_target_2, test_amount_2)
        is_valid_3 = self.validator.is_get_request_data_valid(test_source_3, test_target_3, test_amount_3)

        self.assertEqual(is_valid_1, True)
        self.assertEqual(is_valid_2, False)
        self.assertEqual(is_valid_3, False)

    def test_validate_get_source(self):
        test_source_1 = "USD"
        test_source_2 = "EUR"
        test_source_3 = 777

        is_valid_1 = self.validator._CurrencyConverterValidator__validate_get_source(test_source_1)
        is_valid_2 = self.validator._CurrencyConverterValidator__validate_get_source(test_source_2)
        is_valid_3 = self.validator._CurrencyConverterValidator__validate_get_source(test_source_3)

        self.assertEqual(is_valid_1, True)
        self.assertEqual(is_valid_2, False)
        self.assertEqual(is_valid_3, False)
    
    def test_validate_get_target(self):
        test_source_1 = "USD"
        test_source_2 = "EUR"
        test_source_3 = 777

        is_valid_1 = self.validator._CurrencyConverterValidator__validate_get_target(test_source_1)
        is_valid_2 = self.validator._CurrencyConverterValidator__validate_get_target(test_source_2)
        is_valid_3 = self.validator._CurrencyConverterValidator__validate_get_target(test_source_3)

        self.assertEqual(is_valid_1, True)
        self.assertEqual(is_valid_2, False)
        self.assertEqual(is_valid_3, False)

    def test_validate_get_amount(self):
        test_amount_1 = "$123,456"
        test_amount_2 = "$123,4444"
        test_amount_3 = "$1"
        test_amount_4 = "1"
        test_amount_5 = "$1,234"
        test_amount_6 = "$1111,1234"

        is_valid_1 = self.validator._CurrencyConverterValidator__validate_get_amount(test_amount_1)
        is_valid_2 = self.validator._CurrencyConverterValidator__validate_get_amount(test_amount_2)
        is_valid_3 = self.validator._CurrencyConverterValidator__validate_get_amount(test_amount_3)
        is_valid_4 = self.validator._CurrencyConverterValidator__validate_get_amount(test_amount_4)
        is_valid_5 = self.validator._CurrencyConverterValidator__validate_get_amount(test_amount_5)
        is_valid_6 = self.validator._CurrencyConverterValidator__validate_get_amount(test_amount_6)

        self.assertEqual(is_valid_1, True)
        self.assertEqual(is_valid_2, False)
        self.assertEqual(is_valid_3, True)
        self.assertEqual(is_valid_4, False)
        self.assertEqual(is_valid_5, True)
        self.assertEqual(is_valid_6, False)
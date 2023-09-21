from django.test import TestCase
from .usecase.usecase import CurrencyConverterUseCase

class CurrencyConverterValidatorTestCase(TestCase):
    usecase = CurrencyConverterUseCase()

    def test_get_new_amount(self):
        test_source_1 = "USD"
        test_source_2 = "TWD"
        test_source_3 = "USD"

        test_target_1 = "USD"
        test_target_2 = "JPY"
        test_target_3 = "JPY"

        test_amount_1 = "$10,000"
        test_amount_2 = "$10,000"
        test_amount_3 = "$1,525"

        new_amount_1 = self.usecase.get_new_amount(test_source_1, test_target_1, test_amount_1)
        new_amount_2 = self.usecase.get_new_amount(test_source_2, test_target_2, test_amount_2)
        new_amount_3 = self.usecase.get_new_amount(test_source_3, test_target_3, test_amount_3)

        self.assertEqual(new_amount_1, "$10000.00")
        self.assertEqual(new_amount_2, "$36690.00")
        self.assertEqual(new_amount_3, "$170496.53")

    def test_get_format_amount(self):
        test_amount_1 = "$100,000"
        test_amount_2 = "$1"
        test_amount_3 = "$30,000"

        new_amount_1 = self.usecase._CurrencyConverterUseCase__get_format_amount(test_amount_1)
        new_amount_2 = self.usecase._CurrencyConverterUseCase__get_format_amount(test_amount_2)
        new_amount_3 = self.usecase._CurrencyConverterUseCase__get_format_amount(test_amount_3)

        self.assertEqual(new_amount_1, 100000)
        self.assertEqual(new_amount_2, 1)
        self.assertEqual(new_amount_3, 30000)

    def test_format_new_amount(self):
        test_amount_1 = 100000.1278
        test_amount_2 = 100
        test_amount_3 = 12333.536

        new_amount_1 = self.usecase._CurrencyConverterUseCase__format_new_amount(test_amount_1)
        new_amount_2 = self.usecase._CurrencyConverterUseCase__format_new_amount(test_amount_2)
        new_amount_3 = self.usecase._CurrencyConverterUseCase__format_new_amount(test_amount_3)

        self.assertEqual(new_amount_1, "$100000.13")
        self.assertEqual(new_amount_2, "$100.00")
        self.assertEqual(new_amount_3, "$12333.54")
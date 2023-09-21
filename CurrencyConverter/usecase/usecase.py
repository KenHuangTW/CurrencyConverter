from django.conf import settings
from decimal import Decimal, ROUND_HALF_UP


class CurrencyConverterUseCase:
    currency_converter_data = settings.CURRENCY_CONVERT['currencies']

    def get_new_amount(self, source: str, target: str, amount: str) -> float:
        """根據target轉換幣值"""
        format_amount = self.__get_format_amount(amount)
        new_amount = format_amount * self.currency_converter_data[source][target]
        return self.__format_new_amount(new_amount)
        
    def __get_format_amount(self, amount:str) -> int:
        """將字串的amount轉換成整數的"""
        return int(amount[1:].replace(",", ""))
    
    def __format_new_amount(self, new_amount:float) -> str:
        """格式化成規定格式"""
        accurate_amount = Decimal(str(new_amount))
        accurate_amount_after_round = accurate_amount.quantize(Decimal('0.00'), rounding=ROUND_HALF_UP)
        return "${:.2f}".format(accurate_amount_after_round)
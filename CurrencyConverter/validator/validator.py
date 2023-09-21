from django.conf import settings
import re


class CurrencyConverterValidator:
    def is_get_request_data_valid(self, source: str, target: str, amount: str) -> bool:
        validate_group = [
            self.__validate_get_source(source),
            self.__validate_get_target(target),
            self.__validate_get_amount(amount)]
        
        if (all(validate_group)):
            return True
        return False
            
    
    def __validate_get_source(self, source: str) -> bool:
        """用於驗證get方法中的source參數
        """
        if (not isinstance(source, str)) or (source not in settings.CURRENCY_GROUP):
            return False
        return True
    
    def __validate_get_target(self, target: str) -> bool:
        """用於驗證get方法中的target參數
        """
        if (not isinstance(target, str)) or (target not in settings.CURRENCY_GROUP):
            return False
        return True
    
    def __validate_get_amount(self, target: str) -> bool:
        """用於驗證get方法中的target參數
        """
        pattern = "^\$\d{1,3}(,\d{3})*"  # 開頭為$ 中間必定為數字和逗號且三個數字之前必定要接逗號

        if isinstance(target, str) and re.fullmatch(pattern, target):
            return True
        return False
from rest_framework.views import APIView
from rest_framework.response import Response
from .validator.validator import CurrencyConverterValidator
from .usecase.usecase import CurrencyConverterUseCase
from django.http import HttpResponseBadRequest


class CurrencyConverter(APIView):
    validator = CurrencyConverterValidator()
    usecase = CurrencyConverterUseCase()

    def get(self, request):
        source = request.GET.get("source", None)
        target = request.GET.get("target", None)
        amount = request.GET.get("amount", None)

        is_valid = self.validator.is_get_request_data_valid(source, target, amount)
        if not is_valid:
            return HttpResponseBadRequest({"msg": "Fail", "Message": "invalid argument"})
        
        new_amount = self.usecase.get_new_amount(source, target, amount)

        return Response({"msg": "Success", "amount": new_amount})
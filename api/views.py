from rest_framework import views
from rest_framework.response import Response
from rest_framework import status

from .integrations.awesomeapi import AwesomeApi


class ConvertView(views.APIView):
    def get(self, request):
        """
        method GET
        """
        params_data = (
            request.GET.get('from', ''),
            request.GET.get('to', ''),
            float(request.GET.get('amount', 0.0)),
        )

        if not all(params_data):
            return Response(
                data={'erro': 'Verifique se os parâmetros foram passados na URL'},
                status=status.HTTP_400_BAD_REQUEST
            )
        awesome = AwesomeApi(from_currency=params_data[0], to_currency=params_data[1])
        converted = awesome.converts(params_data[2])
        return Response(
            data={
                'amount': params_data[2],
                'from': params_data[0],
                'to': params_data[1],
                'converted': converted,
            },
            status=status.HTTP_200_OK
        )

import requests
from rest_framework import viewsets
from rest_framework.decorators import action
from customer.models.moyen_de_paiement import MoyenoDePaiementModel
from customer.serializers.moyen_de_paiement import MoyenoDePaiementModelSerializer

class MoyenoDePaiementModelViewSet(viewsets.ModelViewSet):
    queryset = MoyenoDePaiementModel.objects.all()
    serializer_class = MoyenoDePaiementModelSerializer
    
    
    
    @action(detail=False, methods=['post'])
    def MobileMoney(self, request):
        amount = request.data['amount']
        phone_number = request.data['phone_number']
        user = request.user

        # Exemple d'appel API pour MTN Mobile Money
        url = "https://api.mtn.com/mobilemoney/v1/payments"
        headers = {
            "Authorization": "Bearer your_access_token",
            "Content-Type": "application/json"
        }
        data = {
            "amount": amount,
            "currency": "XOF",
            "externalId": "123456",
            "payer": {
                "partyIdType": "MSISDN",
                "partyId": phone_number
            },
            "payerMessage": "Payment for order",
            "payeeNote": "Mercie de votre paiement"
        }

        response = requests.post(url, headers=headers, json=data)
        response_data = response.json()

        if response.status_code == 201:
            transaction = MoyenoDePaiementModel.objects.create(
                user=user,
                transaction_id=response_data['transactionId'],
                amount=amount,
                status='pending'
            )
            return requests.Response({'status': 'payment initiated', 'transaction_id': transaction.transaction_id})
        else:
            return requests.Response({'status': 'payment failed', 'error': response_data}, status=response.status_code)
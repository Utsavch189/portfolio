from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from src.mail.service.email_service import EmailService
from utils.decorators.handel_exceptions import handel_exception

class EmailApiView(APIView):

    @handel_exception(log=True)
    def post(self,request):
        EmailService.serve(data=request.data)
        return Response({"message":"sent successfully!"},status=status.HTTP_200_OK)
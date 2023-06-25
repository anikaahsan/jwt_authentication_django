from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken

class HomeView(APIView):
    permission_classes=(IsAuthenticated,)

    def get(self,request):
        content={'message':'you are viewing this page because you are authenticated with jwt token'}
        return Response(content)
    
class LogoutView(APIView):
    permission_classes=(IsAuthenticated,)  

    def post(self,request):
        try:  
            # refresh_token=request.data['refresh']
            token=RefreshToken(request.data.get('refresh'))
            token.blacklist()
            return Response('blacklisted')
        except Exception as e:
            return Response(str(e))
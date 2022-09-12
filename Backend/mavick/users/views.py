
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import AuthenticationFailed
from users import serializers
import jwt, datetime

from users.models import User
from users.serializers import UserSerializer

# Create your views here.
class RegisterView(APIView):

    def post(self, request):
        serializer  = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save() 
        return Response(serializer.data)

class LoginView(APIView):

    def post(self, request):
        # Se toman los valores 
        email = request.data['email']
        password = request.data['password']

        # Se busca el usuario por medio del email
        user = User.objects.filter(email=email).first()

        if user is None:
            raise AuthenticationFailed("Usuario no encontrado.")

        if not user.check_password(password):
            raise AuthenticationFailed("Contraseña incorrecta.")

        # Se le agregan 60 minutos al Token con dicho ID
        payload = {
            'id': user.id,
            'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=60),
            'iat': datetime.datetime.utcnow()
        }

        token = jwt.encode(payload, 'secret', algorithm='HS256')
        response = Response()
        response.set_cookie(key='jwt', value=token, httponly=True)
        response.data = {
            'msg' : 'Logeado Correctamente.'
        }
        return response

class UserView(APIView):

    def get(self, request):
        token = request.COOKIES.get('jwt')

        if not token:
            raise AuthenticationFailed("Inautenticado!.")
        try:    
            payload = jwt.decode(token, 'secret', algorithms=['HS256'])
        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed("Inautenticado!.")

        user = User.objects.filter(id = payload['id']).first()
        serializer = UserSerializer(user)

        return Response(serializer.data)

class LogoutView(APIView):

    def post(self, request):
        response = Response()
        response.delete_cookie('jwt')
        response.data = {
            'message' : 'success'
        }
        return response
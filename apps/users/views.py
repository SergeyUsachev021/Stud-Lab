from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from requests import get
from rest_framework_simplejwt.tokens import RefreshToken

from .models import User


class YandexAuthorizeView(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        auth_header = request.META.get('HTTP_AUTHORIZATION', '')
        if not auth_header.startswith('Bearer '):
            return Response({}, status=status.HTTP_401_UNAUTHORIZED)
        token = auth_header.split(' ')[1]
        response = get(
            'https://login.yandex.com/info',
            params={
                "format": "json",
            },
            headers={
                "Authorization": f"Bearer {token}"
            }

        )
        if response.status_code != 200:
            return Response({}, status=status.HTTP_502_BAD_GATEWAY)
        data = response.json()
        yandex_id = int(data.get('yandex_id', 0))
        if not yandex_id:
            return Response({}, status=status.HTTP_502_BAD_GATEWAY)
        login = data.get('login')
        email = data.get('default_email')
        try:
            user = User.objects.get(yandex_id=yandex_id)
        except User.DoesNotExist:
            try:
                user = User.objects.get(email=email)
                user.yandex_id = yandex_id
            except User.DoesNotExist:
                user = User.objects.create_user(username=login, email=email, yandex_id=yandex_id, is_active=True)
                user.set_unusable_password()
            user.save()
        refresh = RefreshToken.for_user(user)
        return Response({
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        }, status=status.HTTP_200_OK)

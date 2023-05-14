from rest_framework import viewsets, response, mixins
from .serializers import RegiserSerializers, TokenSerializers
from ..models import UserModels
from drf_yasg.utils import swagger_auto_schema
from rest_framework.decorators import action
from rest_framework import permissions
from .serializers import LogOutSerializer
from rest_framework.response import Response


class GetToken(mixins.CreateModelMixin,
               viewsets.GenericViewSet):
    queryset         = UserModels.objects.all()
    serializer_class = RegiserSerializers
    # permission_classes = (IsAdminUser,)


class Authenticate(viewsets.ViewSet):
    # permission_classes = (IsAdminUser,)
    serializer_class = TokenSerializers

    @swagger_auto_schema(query_serializer=TokenSerializers)
    @action(detail=False, methods=['get'])
    def login(self, request, *args, **kwargs):
        query_params = request.query_params
        ser = self.serializer_class(data=query_params)
        ser.is_valid(raise_exception=True)
        status, detail = UserModels.decrypt_token(query_params['token'])
        return response.Response(detail, status=status) 

class LogOut(viewsets.ViewSet):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = LogOutSerializer

    def create(self, request, *args, **kwargs):
        ser = self.serializer_class(data=request.data)
        ser.is_valid(raise_exception=True)
        refresh = ser.data['refresh']
        user = request.user
        status, detail = user.logout(refresh)
        return Response({'detail': detail}, status=status)
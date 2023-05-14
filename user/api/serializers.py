from rest_framework import serializers
from ..models import UserModels
from rest_framework.reverse import reverse_lazy
from ..messages import Messages
from django.conf import settings
from rest_framework.exceptions import ValidationError


class RegiserSerializers(serializers.ModelSerializer):
    redirect_url = serializers.SerializerMethodField()
    api_key = serializers.SlugField(write_only=True)

    class Meta:
        model = UserModels
        fields = ['api_key', 'user_id', 'redirect_url']
        extra_kwargs ={'user_id': {'write_only' : True, 'validators': None}}

    def validate_api_key(self, value):
        if not value == settings.API_KEY:
            raise ValidationError({'error' : Messages.INVALID_API_KEY.value})
        return value
       
    def get_redirect_url(self, obj):
        request = self.context.get('request')
        url = f"{reverse_lazy('authenticate-login', request=request)}?token={obj.token_generator()}"
        return url

    def create(self, validated_data):
        user_id = validated_data['user_id']
        obj, _ = UserModels.objects.get_or_create(user_id=user_id)
        return obj


class TokenSerializers(serializers.Serializer):
    token = serializers.CharField(
        max_length=32,
        error_messages=Messages.TOKEN_ERROR_MESSAGES.value  
    )

class LogOutSerializer(serializers.Serializer):
    refresh = serializers.CharField(
        required=True, allow_null=False, allow_blank=False)

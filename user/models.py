from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from rest_framework_simplejwt.tokens import RefreshToken
from django.shortcuts import get_object_or_404
from rest_framework import status
from .utils import token_generate
from django.core.cache import cache
import uuid
from rest_framework.exceptions import ValidationError
from .messages import Messages
from django.conf import settings
from django.db.models import Q


class UserModels(AbstractUser):
    id = models.UUIDField(_("id"), primary_key=True, default=uuid.uuid4, editable=False)
    user_id = models.SlugField(_("user_id"), db_index=True)

    class Meta(object):
        constraints = [models.UniqueConstraint(
            fields=['user_id'],
            condition=Q(is_staff=False),
            name='UNIQUE_USER_ID'
        )]

    def __str__(self):
        if self.is_superuser:
            return self.username
        return self.user_id

    def save(self, *args, **kwargs):
        if not self.username:
            self.username = f'{self.id}'
        super().save(*args, **kwargs)

    def logout(self, refresh):
        RefreshToken(refresh).blacklist()
        cache.set(self.pk, 'blocked', 180)
        return status.HTTP_200_OK, Messages.LOGOUT.value

    def tokens(self):
        refresh = RefreshToken.for_user(self)
        return {
            'refresh': str(refresh),
            'access': str(refresh.access_token)
            }

    def token_generator(self):
        token = token_generate()
        if cache.keys(f"*_{self.user_id}"):
            cache.delete(cache.keys(f"*_{self.user_id}")[0]) 
        cache.set(f"{token}_{self.user_id}", {'token': token, "user_id" : self.user_id}, settings.TOKEN_EXPIRATION_TIME)
        return token

    @staticmethod
    def decrypt_token(token):
        try:
            decrypt = cache.get(''.join(cache.keys(f"{token}_*"))) 
            user_id = decrypt['user_id']
            obj = get_object_or_404(UserModels, user_id=user_id)
            cache.delete(f"{token}_{user_id}")
        except:
            raise ValidationError({'error' : Messages.INVALID_TOKEN.value})
        return (
            status.HTTP_200_OK,
            {'refresh_token' : obj.tokens()['refresh'], 'access_token' : obj.tokens()['access']}
        )

from enum import Enum
from django.utils.translation import gettext_lazy as _


class Messages(Enum):
    INVALID_TOKEN = _("token is not valid")
    INVALID_API_KEY = _("api_key is not valid")
    TOKEN_ERROR_MESSAGES = {
        'invalid': _('Not a valid string.'),
        'blank': _('token may not be blank.'),
        'max_length': _('Ensure the token has no more than {max_length} characters.'),
        'min_length': _('Ensure the token has at least {min_length} characters.'),
    }
    LOGOUT = _('You are logged out')
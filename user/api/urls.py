from .views import GetToken, Authenticate, LogOut
from  rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'authenticate', Authenticate, basename='authenticate')
router.register(r'get_token', GetToken, basename='get_token')
router.register(r'logout', LogOut, basename='logout')

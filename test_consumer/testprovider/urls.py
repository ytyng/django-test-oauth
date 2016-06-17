from allauth.socialaccount.providers.oauth2.urls import default_urlpatterns
from .provider import TestProvider

urlpatterns = default_urlpatterns(TestProvider)

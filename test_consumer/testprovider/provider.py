from allauth.socialaccount import providers
from allauth.socialaccount.providers.base import ProviderAccount
from allauth.socialaccount.providers.oauth2.provider import OAuth2Provider


class TestAccount(ProviderAccount):

    def to_str(self):
        dflt = super(TestAccount, self).to_str()
        return self.account.extra_data.get('name', dflt)


class TestProvider(OAuth2Provider):
    id = 'testprovider'
    name = 'Test Provider'
    account_class = TestAccount

    def get_default_scope(self):
        return ['read', 'write']

    def get_site(self):
        settings = self.get_settings()
        return settings.get('SITE', 'testprovider')

    def extract_uid(self, data):
        uid = str(data['user_id'])
        return uid

    def extract_common_fields(self, data):
        return dict(username=data.get('email', 'no name'))

providers.registry.register(TestProvider)

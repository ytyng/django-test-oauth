from django.http import JsonResponse
from oauth2_provider.views.generic import ProtectedResourceView


class ProfileView(ProtectedResourceView):
    def get(self, request, **kwargs):
        user = request.resource_owner

        return JsonResponse({
            'user_id': user.id,
            'email': user.email,
            'date_joined': user.date_joined,
            'secret_message': 'The quick brown fox',
        })


profile_view = ProfileView.as_view()

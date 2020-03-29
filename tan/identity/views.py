from django.contrib.auth import views
from django.urls import reverse


class IdentityLoginView(views.LoginView):
    template_name = 'identity/login.html'

    # Redirect to time zone view after login
    # Pass the next parameter to the TZ view
    # TZ template will redirect to next after AJAX request
    def get_success_url(self):
        next = self.request.GET.get('next', '/')
        url = reverse('timezone:set-timezone')
        return f'{url}?next={next}'

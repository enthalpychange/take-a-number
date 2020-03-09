from django.contrib.auth import views


class IdentityLoginView(views.LoginView):
    template_name = 'identity/login.html'

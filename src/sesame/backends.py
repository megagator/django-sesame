from django.contrib.auth import backends as auth_backends

from .tokens_v1 import parse_token

__all__ = ["ModelBackend"]


class SesameBackendMixin:
    """
    Authenticate with a django-sesame token.

    Mix this class in an authentication backend providing ``get_user(user_id)``.

    """

    def authenticate(self, request, sesame):
        """
        Check the token and return the corresponding user.

        """
        # This check shouldn't be necessary, but it can avoid problems like
        # issue #37 and Django's built-in backends include similar checks.
        if sesame is None:
            return
        return parse_token(sesame, self.get_user)


class ModelBackend(SesameBackendMixin, auth_backends.ModelBackend):
    """
    Authenticate with a django-sesame token.

    """

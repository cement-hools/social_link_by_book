from django.contrib.auth import get_user_model

User = get_user_model()


class EmailAuthBackend(object):
    """Выполняет аутентификацию пользователя по e-mail."""

    def authenticate(self, request, username=None, password=None):
        try:
            user = User.objects.get(email=username)
            if user.check_password(password):
                # Этот метод выполняет шифрование пароля и сравнивает результат с тем, который хранится в базе данных;
                return user
            return None
        except User.DoesNotExist:
            return None

    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None

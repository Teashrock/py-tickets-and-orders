from django.contrib.auth import get_user_model
User = get_user_model()


def create_user(username, password, email=None, first_name=None, last_name=None):
    user = User.objects.create_user(
        username=username,
        password=password,
        email=email,
        first_name=first_name,
        last_name=last_name
    )
    return user
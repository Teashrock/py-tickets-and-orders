from django.contrib.auth import get_user_model
User = get_user_model()


def create_user(username, password, email=None, first_name=None, last_name=None) -> User:
    user = User.objects.create_user(
        username=username,
        password=password,
        email=email,
        first_name=first_name,
        last_name=last_name
    )
    return user


def get_user(user_id) -> User:
    return User.objects.get(pk=user_id)


def update_user(user_id, username=None, password=None, email=None, first_name=None, last_name=None) -> None:
    user = User.objects.get(pk=user_id)
    user.username = username
    user.email = email
    user.first_name = first_name
    user.last_name = last_name
    user.set_password(password)
    user.save()
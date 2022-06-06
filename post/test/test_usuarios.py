import pytest

from django.contrib.auth.models import User

@pytest.mark.django_db
def test_common_user_creation():
    user = User.objects.create_user(
            username='dasdas',
            email='asdasda@gmail.com',
            nombres='wegw gwgwe',
            password='12345',
            is_staff=False
    )
    assert User.username == 'dasdas'

@pytest.mark.django_db
def test_superuser_creation():
    user = User.objects.create_superuser(
            username='dasdas',
            email='asdasda@gmail.com',
            nombres='wegw gwgwe',
            password='12345'
    )

    assert user.is_superuser

@pytest.mark.django_db
def test_staff_user_creation():
    user = User.objects.create_user(
            username='dasdas',
            email='asdasda@gmail.com',
            nombres='wegw gwgwe',
            password='12345',
            is_staff=False
    )

    assert user.is_staff
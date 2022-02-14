import pytest
from django.contrib.auth import get_user_model

from kefir_api import serializers


class TestUserAPI:

    @pytest.mark.django_db(transaction=True)
    def test_01_users_not_auth(self, client):
        response = client.get('/api/users/')

        assert response.status_code != 404, \
            'Страница `/api/users/` не найдена, проверьте этот адрес в *urls.py*'

        assert response.status_code == 401, \
            'Проверьте, что при GET запросе `/api/users/` без авторизации возвращается статус 401'

    @pytest.mark.django_db(transaction=True)
    def test_02_users_admin_not_auth(self, client, admin):
        response = client.get(f'/api/users/1/')

        assert response.status_code != 404, \
            'Страница `/api/users/1/` не найдена, проверьте этот адрес в *urls.py*'

        assert response.status_code == 401, \
            'Проверьте, что при GET запросе `/api/users/1/` без авторизации возвращается статус 401'

    @pytest.mark.django_db(transaction=True)
    def test_03_users_id_auth(self, user_client, user):
        response = user_client.get(f'/api/users/{user.id}/')

        assert response.status_code != 404, \
            f'Страница `/api/users/{user.id}/` не найдена, проверьте этот адрес в *urls.py*'

        assert response.status_code != 401, \
            f'Проверьте, что при GET запросе `/api/users/{user.id}/` при авторизации пользователя не возвращается статус 401'

        assert response.status_code == 200, \
            f'Проверьте, что при GET запросе `/api/users/{user.id}/` при авторизации пользователя возвращается статус 200'

        assert response.data.serializer.__class__ == serializers.UserSerializer, \
            'Проверьте, что используется верный сериалайзер'

    @pytest.mark.django_db(transaction=True)
    def test_04_users_admin_id_auth(self, admin_client, admin_user):
        response = admin_client.get(f'/api/users/{admin_user.id}/')

        assert response.status_code != 404, \
            f'Страница `/api/users/{admin_user.id}/` не найдена, проверьте этот адрес в *urls.py*'

        assert response.status_code != 401, \
            f'Проверьте, что при GET запросе `/api/users/{admin_user.id}/` при авторизации администратора не возвращается статус 401'

        assert response.status_code == 200, \
            f'Проверьте, что при GET запросе `/api/users/{admin_user.id}/` при авторизации администратора возвращается статус 200'

        assert response.data.serializer.__class__ == serializers.UserForAdminSerializer, \
            'Проверьте, что используется верный сериалайзер'

    @pytest.mark.django_db(transaction=True)
    def test_05_users_auth(self, user_client, user):
        response = user_client.get(f'/api/users/')

        assert response.status_code != 404, \
            'Страница `/api/users/` не найдена, проверьте этот адрес в *urls.py*'

        assert response.status_code != 401, \
            'Проверьте, что при GET запросе `/api/users/` при авторизации пользователя не возвращается статус 401'

        assert response.status_code == 200, \
            'Проверьте, что при GET запросе `/api/users/` при авторизации пользователя возвращается статус 200'

        assert response.data[
                   'results'].serializer.child.__class__ == serializers.UserSerializer, \
            'Проверьте, что используется верный сериалайзер'

        assert len(response.data) == 4, \
            'Проверьте, что при GET запросе `/api/users/` при авторизации пользователя работает паджинатор'

    @pytest.mark.django_db(transaction=True)
    def test_06_users_admin_auth(self, admin_client, admin_user):
        response = admin_client.get('/api/users/')

        assert response.status_code != 404, \
            'Страница `/api/users/` не найдена, проверьте этот адрес в *urls.py*'

        assert response.status_code != 401, \
            'Проверьте, что при GET запросе `/api/users/` при авторизации пользователя не возвращается статус 401'

        assert response.status_code == 200, \
            'Проверьте, что при GET запросе `/api/users/` при авторизации пользователя возвращается статус 200'

        assert response.data[
                   'results'].serializer.child.__class__ == serializers.UserForAdminSerializer, \
            'Проверьте, что используется верный сериалайзер'

        assert len(response.data) == 4, \
            'Проверьте, что при GET запросе `/api/users/` при авторизации пользователя работает паджинатор'

    @pytest.mark.django_db(transaction=True)
    def test_07_users_id_patch_auth(self, user_client, admin_client, user):
        data = {
            'username': 'UserTest1',
            'is_superuser': True
        }
        user_client.patch(f'/api/users/{user.id}/', data=data)
        response = admin_client.get(f'/api/users/{user.id}/')

        assert response.data['username'] == 'UserTest1', \
            f'Проверьте, что при запросе PATCH `/api/users/{user.id}` пользователем изменяются данные'

        assert response.data['is_superuser'] is False

    @pytest.mark.django_db(transaction=True)
    def test_08_users_id_patch_auth(self, user_client, admin_client, user):
        data = {
            'username': 'UserTest1',
            'is_superuser': True
        }
        admin_client.patch(f'/api/users/{user.id}/',
                           data=data,
                           content_type='application/json')
        response = admin_client.get(f'/api/users/{user.id}/')

        assert response.data['username'] == 'UserTest1', \
            f'Проверьте, что при запросе PATCH `/api/users/{user.id}/` администратором изменяются данные'

        assert response.data['is_superuser'] is True, \
            f'Проверьте, что при запросе PATCH `/api/users/{user.id}/` администратором изменяются данные'

    @pytest.mark.django_db(transaction=True)
    def test_09_users_another_id_patch_auth(self, user_client, admin_client, user):
        data = {
            'username': 'UserTest2',
        }
        user_1 = get_user_model().objects.create(
            username='TestUser2',
            email='testuser2@fake.fake',
            password='123456',
        )
        response_patch = user_client.patch(f'/api/users/{user_1.id}/', data=data)
        response = admin_client.get(f'/api/users/{user_1.id}/')

        assert response.data['username'] != 'UserTest1', \
            f'Проверьте, что при запросе PATCH `/api/users/{user_1.id}/` другим пользователем не изменяются данные'

        assert response_patch.status_code == 403

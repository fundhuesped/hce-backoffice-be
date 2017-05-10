#!/usr/bin/python
# -*- coding: utf-8 -*-

from rest_framework.test import APITestCase, APIClient
from django.contrib.auth.models import User
from rest_framework import status

import base64

class LogingTest(APITestCase):
    def test_login_ok(self):
        """
        Asegura hacer el login de un usuario
        :return:
        """
        user = User.objects.create_user(username="Foo", email="sa@sa.com", password="BarBarBar")
        user.save()
        basicToken = 'Rm9vOkJhckJhckJhcg=='
        client = APIClient()
        client.credentials(HTTP_AUTHORIZATION='Basic ' + basicToken)
        response = client.post('/core/user/login/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_login_fail(self):
        """
        Asegura fallar en el login de un usuario
        :return:
        """
        User.objects.create_user(username="Foo", email="sa@sa.com", password="BarBarBar")
        basicToken = 'VGVzdDpTYXJhemE='
        client = APIClient()
        client.credentials(HTTP_AUTHORIZATION='Basic ' + basicToken)
        response = client.post('/core/user/login/')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_logout(self):
        """
        Asegura cerrar una sesión
        :return:
        """
        User.objects.create_user(username="Foo", email="sa@sa.com", password="BarBarBar")
        basicToken = 'VGVzdDpCYXJCYXJCYXI='
        client = APIClient()
        client.credentials(HTTP_AUTHORIZATION='Basic ' + basicToken)
        response = client.post('/core/user/login/')
        client.credentials()
        response = client.delete('/core/user/logout/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

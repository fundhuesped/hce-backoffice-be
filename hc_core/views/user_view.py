#!/usr/bin/python
# -*- coding: utf-8 -*-
from rest_framework import generics
from rest_framework.views import Response
from django.contrib.auth import login, logout
from rest_framework.permissions import AllowAny
from rest_framework.permissions import IsAuthenticated
from hc_core.serializers import UserSerializer
from hc_core.serializers import PasswordChangeSerializer
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import Permission, Group
from django.http import JsonResponse


class UserLogin(generics.CreateAPIView):
    serializer_class = UserSerializer
    permission_classes = AllowAny,
    def post(self, request, *args, **kwargs):
        login(request, request.user)
        tokens = Token.objects.filter(user=request.user)
        if tokens.count()>=1:
            token = tokens[0]
        else:
            token = Token.objects.create(user=request.user)
        return Response(UserSerializer(request.user).data, headers={'auth-token': token.key})


class UserLogout(generics.DestroyAPIView):
    serializer_class = UserSerializer
    permission_classes = AllowAny,
    def delete(self, request, *args, **kwargs):
        logout(request)
        return Response({})


class PasswordChangeView(generics.GenericAPIView):
    """
    Calls Django Auth SetPasswordForm save method.
    Accepts the following POST parameters: new_password1, new_password2
    Returns the success/fail message.
    """

    serializer_class = PasswordChangeSerializer
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({})


class Permissions(generics.GenericAPIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        permissionToCheck = self.request.data['permission']
        print("=== Permission to check: ", permissionToCheck)
        permissionsFound = list(request.user.get_group_permissions())
        #print("=== User Permissions:", permissionsFound)
        hasPerm = permissionToCheck in permissionsFound
        print("=== User has Permission:", hasPerm)
        
        return JsonResponse({ 'permission': permissionToCheck, 'hasPerm': hasPerm, 'success': 'true'})


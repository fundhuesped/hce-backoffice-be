#!/usr/bin/python
# -*- coding: utf-8 -*-
from django.contrib.auth.models import User
from rest_framework import serializers
from django.conf import settings
from rest_framework import exceptions
from django.contrib.auth.forms import SetPasswordForm
from django.contrib.auth.models import Group

class GroupSerializer(serializers.ModelSerializer):    
    class Meta:
        model = Group
        fields = ('name',)
        

class UserSerializer(serializers.ModelSerializer):
    password = serializers.Field(
        write_only=True
    )

    groups = GroupSerializer(many=True)

    def validate(self, attrs):
        user = super(UserSerializer, self).validate(self, attrs)
        user.set_password(attrs['password'])
        return user

    class Meta:
        model = User
        fields = ('password', 'first_name', 'last_name', 'email','groups')

class PasswordChangeSerializer(serializers.Serializer):

    old_password = serializers.CharField(max_length=128)
    new_password1 = serializers.CharField(max_length=128)
    new_password2 = serializers.CharField(max_length=128)

    set_password_form_class = SetPasswordForm

    def __init__(self, *args, **kwargs):
        self.logout_on_password_change = getattr(
            settings, 'LOGOUT_ON_PASSWORD_CHANGE', False
        )
        super(PasswordChangeSerializer, self).__init__(*args, **kwargs)

        self.request = self.context.get('request')
        self.user = getattr(self.request, 'user', None)

    def validate_old_password(self, value):
        invalid_password_conditions = (
            True,
            self.user,
            not self.user.check_password(value)
        )

        if all(invalid_password_conditions):
            raise serializers.ValidationError('Invalid password')
        return value

    def validate(self, attrs):
        self.set_password_form = self.set_password_form_class(
            user=self.user, data=attrs
        )


        if not self.set_password_form.is_valid():
            raise serializers.ValidationError(self.set_password_form.errors)
        if attrs['old_password'] == attrs['new_password1']:
            raise serializers.ValidationError('Same password')
        return attrs

    def save(self):
        self.set_password_form.save()
        if not self.logout_on_password_change:
            from django.contrib.auth import update_session_auth_hash
            update_session_auth_hash(self.request, self.user)
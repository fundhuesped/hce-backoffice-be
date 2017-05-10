
#!/usr/bin/python
# -*- coding: utf-8 -*-

from hc_common.serializers import TypeNestedSerializer
from django.contrib.auth.models import User


class UserNestedSerializer(TypeNestedSerializer):

    def to_internal_value(self, data):
        if (isinstance(data, list) or isinstance(data, dict)):
            if 'id' in data:
                local = User.objects.filter(pk=data['id'])
            else:
                return data
        else:
            local=User.objects.filter(pk=data)
        if local.count() > 0:
            return local[0]
        else:
            raise ValueError('User not found')
            
    class Meta(TypeNestedSerializer.Meta):
        model = User
        fields = ('id', 'first_name', 'last_name', 'username')

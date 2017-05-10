#!/usr/bin/python
# -*- coding: utf-8 -*-

from hc_common.serializers import TypeNestSerializer
from hc_common.models import SocialService


class SocialServiceNestSerializer(TypeNestSerializer):
    class Meta(TypeNestSerializer.Meta):
        model = SocialService

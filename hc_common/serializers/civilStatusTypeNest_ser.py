#!/usr/bin/python
# -*- coding: utf-8 -*-

from hc_common.serializers import TypeNestSerializer
from hc_common.models import CivilStatusType


class CivilStatusTypeNestSerializer(TypeNestSerializer):
    class Meta(TypeNestSerializer.Meta):
        model = CivilStatusType

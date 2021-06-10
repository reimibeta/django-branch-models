from rest_flex_fields import FlexFieldsModelSerializer
from rest_framework import serializers

from branch_models.models import Branch


class BranchSerializer(FlexFieldsModelSerializer):

    class Meta:
        model = Branch
        # exclude = ('removed_by',)
        fields = [
            'id',
            'url',
            'name',
            'created_date',
            'updated_date',
            'is_active',
        ]
        expandable_fields = {}

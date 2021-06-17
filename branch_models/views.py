from django.shortcuts import render
from django_rest_framework.pagination import StandardResultsSetPagination
from rest_framework import viewsets

from branch_models.models import Branch
from branch_models.serializers import BranchSerializer


class BranchViewSet(viewsets.ModelViewSet):
    queryset = Branch.objects.order_by('-id').all()
    pagination_class = StandardResultsSetPagination
    serializer_class = BranchSerializer

from django.contrib.auth import get_user_model
from activity.models import ActivityPeriod
from activity.serializers import UserListSerializer
from activity.paginations import PaginateBy20
from rest_framework import generics, filters
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

User = get_user_model()


class UserActivityListViewSet(generics.ListAPIView):
    permission_classes = (IsAuthenticated,)
    filter_backends = (filters.SearchFilter, filters.OrderingFilter)
    search_fields = ('first_name', 'username', 'last_name', 'tz', 'ext_id')
    ordering_fields = '__all__'
    ordering = ('-id',)
    model = User
    pagination_class = PaginateBy20
    queryset = User.objects.all()
    lookup_field = 'ext_id'

    def list(self, request):
        queryset = self.filter_queryset(self.get_queryset())
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = UserListSerializer(page, many=True)
            return self.get_paginated_response(serializer.data)
        serializer = UserListSerializer(queryset, many=True)
        return Response(serializer.data)
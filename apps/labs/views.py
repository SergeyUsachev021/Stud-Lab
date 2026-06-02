from django.db import IntegrityError

from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response

from apps.labs.models import ArchivedLab, Lab
from apps.labs.serializers import ArchivedLabSerializer, LabDetailSerializer, LabSerializer


class LabViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Lab.objects.prefetch_related('files').all()
    permission_classes = [AllowAny]

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return LabDetailSerializer

        return LabSerializer

    def get_permissions(self):
        if self.action in ('archive', 'unarchive'):
            return [IsAuthenticated()]

        return super().get_permissions()

    @action(detail=True, methods=['post'], url_path='archive')
    def archive(self, request, pk=None):
        archive_item, created = ArchivedLab.objects.get_or_create(
            user=request.user,
            lab=self.get_object(),
        )

        response_status = status.HTTP_201_CREATED if created else status.HTTP_200_OK

        return Response(
            ArchivedLabSerializer(
                archive_item,
                context={'request': request},
            ).data,
            status=response_status,
        )

    @archive.mapping.delete
    def unarchive(self, request, pk=None):
        deleted_count, _ = ArchivedLab.objects.filter(
            user=request.user,
            lab=self.get_object(),
        ).delete()

        if deleted_count == 0:
            return Response(
                {'detail': 'Этой лабораторной нет в архиве.'},
                status=status.HTTP_404_NOT_FOUND,
            )

        return Response(status=status.HTTP_204_NO_CONTENT)


class ArchiveViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = ArchivedLabSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return (
            ArchivedLab.objects
            .filter(user=self.request.user)
            .select_related('lab')
            .prefetch_related('lab__files')
        )
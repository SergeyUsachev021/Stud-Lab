from rest_framework import serializers

from .models import ArchivedLab, Lab, LabFile


class LabFileSerializer(serializers.ModelSerializer):
    class Meta:
        model = LabFile
        fields = ['id', 'file']


class LabSerializer(serializers.ModelSerializer):
    is_archived = serializers.SerializerMethodField()

    class Meta:
        model = Lab
        fields = [
            'id',
            'name',
            'description',
            'year',
            'university',
            'faculty',
            'type_work',
            'author',
            'downloaded_times',
            'is_archived',
        ]

    def get_is_archived(self, obj):
        request = self.context.get('request')

        if not request or not request.user.is_authenticated:
            return False

        return ArchivedLab.objects.filter(
            user=request.user,
            lab=obj,
        ).exists()


class LabDetailSerializer(LabSerializer):
    files = LabFileSerializer(many=True, read_only=True)

    class Meta(LabSerializer.Meta):
        fields = LabSerializer.Meta.fields + [
            'level',
            'course',
            'manager',
            'created_time',
            'verified',
            'files',
        ]


class ArchivedLabSerializer(serializers.ModelSerializer):
    lab = LabSerializer(read_only=True)

    class Meta:
        model = ArchivedLab
        fields = ['id', 'lab', 'created_at']
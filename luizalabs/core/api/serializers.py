from core.models import UserMagalu
from rest_framework import serializers


class UserMagaluSerializer(serializers.ModelSerializer): # forms.ModelForm

    class Meta:
        model = UserMagalu
        fields = [
            'id',
            'user',
            'title',
            'content',
            'timestamp',
        ]
        read_only_fields = ['id', 'user']

    # converts to JSON
    # validations for data passed

    def validate_title(self, value):
        query_set = UserMagalu.objects.filter(title__iexact=value)  # including instance
        if self.instance:
            query_set = query_set.exclude(pk=self.instance.pk)
        if query_set.exists():
            raise serializers.ValidationError("This title has already been used")
        return value

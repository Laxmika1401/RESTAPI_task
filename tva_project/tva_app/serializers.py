from .models import tva_table
from rest_framework import serializers
class usersSerializer(serializers.ModelSerializer):
    class Meta:
        model = tva_table
        fields = ('id',
                  'first_name',
                  'last_name',
                  'company',
                  'city',
                  'state',
                  'zip',
                  'email',
                  'web',
                  'age'
                )
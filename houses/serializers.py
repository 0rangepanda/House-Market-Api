from rest_framework import serializers
from houses.models import House
from users.models import User

class HouseSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')


    def create(self, validated_data):
        """
        Create and return a new instance, given the validated data.
        """
        return House.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing instance, given the validated data.
        """
        for field in validated_data:
            instance.__setattr__(field, validated_data.get(field))
        instance.save()
        return instance

    class Meta:
        model = House
        fields = ('url', 'id',
                  'name', 'address', 'zipcode', 'status', 'description',
                  'owner')

        extra_kwargs = {
            'url': {
                'view_name': 'houses:house-detail',
            }
        }

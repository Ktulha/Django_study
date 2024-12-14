from rest_framework import serializers, validators

from api.models import ApiUser, Product,  Warehouse

API_USER_TYPES = [
    ('consumer', 'Consumer'),
    ('supplier', 'Supplier'),

]


class UserSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=128, validators=[
        validators.UniqueValidator(ApiUser.objects.all())
    ])
    email = serializers.EmailField(max_length=128, validators=[
        validators.UniqueValidator(ApiUser.objects.all())
    ])
    password = serializers.CharField(max_length=128, write_only=True)
    user_type = serializers.ChoiceField(
        choices=API_USER_TYPES, default='consumer')

    def create(self, validated_data):
        user = ApiUser.objects.create(
            username=validated_data['username'],
            email=validated_data['email'],
            user_type=validated_data['user_type']

        )
        user.set_password(validated_data['password'])
        user.save()
        return user


class WarehouseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Warehouse
        fields = '__all__'
        extra_kwargs = {"id": {"read_only": True}}


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'
        extra_kwargs = {"id": {"read_only": True}}

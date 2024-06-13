from django.contrib.auth.models import User

from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    
    password = serializers.CharField(write_only=True, required=False)
    
    def create(self, validated_data):
        print(validated_data)
        password = validated_data.pop("password")
        user = User.objects.create(**validated_data)
        user.set_password(password)
        print(validated_data)
        user.save()
        
        return user
    
    class Meta:
        model = User
        fields = ['url', 'id', 'email', 'username', 'first_name', 'last_name', 'password']
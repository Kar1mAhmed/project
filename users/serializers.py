from rest_framework import serializers
from .models import User

from dj_rest_auth.serializers import UserDetailsSerializer


class UserRegisterSerializer(UserDetailsSerializer):

    password2 = serializers.CharField(
        style={'input_type': 'password'}, write_only=True)

    class Meta:
        model = User
        exclude = ['is_superuser', 'is_staff', 'last_login', 'date_joined', 'is_active']
        extra_kwargs = {
            'password': {
                'write_only': True
            }
        }

    def save(self, request):
        user = User(
            email=self.validated_data['email'],
            username=self.validated_data['username'],
            first_name=self.validated_data['first_name'],
            last_name=self.validated_data['last_name'],
            national_id=self.validated_data['national_id'],
        )

        optional_fields = ['notification_token']

        for field in optional_fields:
            if field in self.validated_data:
                setattr(user, field, self.validated_data[field])

        password = self.validated_data['password']
        password2 = self.validated_data['password2']

        if password != password2:
            raise serializers.ValidationError(
                {'password': 'Passwords must match.'})
        user.set_password(password)
        user.save()
        return user


class CustomUserDetailsSerializer(UserDetailsSerializer):

    class Meta:
        model = User
        exclude = ['is_superuser', 'is_staff', 'last_login', 'date_joined',
                   'is_active', 'password', 'groups', 'user_permissions']
        read_only_fields = ('id', )
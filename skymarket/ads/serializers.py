from rest_framework import serializers
from ads.models import Ad, Comment


# Сериалайзеры. Предлагаем Вам такую структуру, однако вы вправе использовать свою

class CommentSerializer(serializers.ModelSerializer):
    # сериалайзер для модели Comment
    class Meta:
        model = Comment
        fields = '__all__'


class AdSerializer(serializers.ModelSerializer):
    # сериалайзер для модели Ad
    class Meta:
        model = Ad
        fields = '__all__'


class AdDetailSerializer(serializers.ModelSerializer):
    # сериалайзер для модели Ad
    class Meta:
        model = Ad
        fields = '__all__'

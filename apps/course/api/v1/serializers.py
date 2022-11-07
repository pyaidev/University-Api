from rest_framework import serializers

from apps.accounts.api.v1.serializers import AccountUpdateSerializer
from apps.blog.api.v1.serializers import CategorySerializer, TagSerializer
from ...models import Course, Lesson


class CourseCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Course
        fields = ['id', 'author', 'title', 'image', 'category', 'tags', 'description', 'detail', 'created_at']
        extra_kwargs = {
            'author': {'required': False, 'allow_null': True},
            'tags': {'required': False, 'allow_null': True},
            'category': {'required': False, 'allow_null': True},
        }

    def create(self, validated_data):
        request = self.context['request']
        user_id = request.user.id
        tags = validated_data.pop('tags', [])
        obj = Course.objects.create(author_id=user_id, **validated_data)
        for tag in tags:
            obj.tags.add(tag)
        return obj


class CourseGetSerializer(serializers.ModelSerializer):
    author = AccountUpdateSerializer(required=False, read_only=True)
    category = CategorySerializer(required=False, read_only=True)
    tags = TagSerializer(required=False, read_only=True, many=True)

    class Meta:
        model = Course
        fields = ['id', 'author', 'title', 'image', 'category', 'tags', 'description', 'detail', 'created_at']


class LessonGetSerializer(serializers.ModelSerializer):
    course = CourseGetSerializer(required=False, read_only=True)

    class Meta:
        model = Lesson
        fields = ['id', 'course', 'title', 'duration', 'video', 'description', 'created_at']


class LessonPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = ['id', 'course', 'title', 'duration', 'video', 'description', 'created_at']


import rest_framework

import models


class LanguageSerializer(
        rest_framework.serializers.HyperlinkedModelSerializer):

    class Meta:
        model = models.Language
        fields = ('id', 'name')


class CommentSerializer(
        rest_framework.serializers.HyperlinkedModelSerializer):

    language = rest_framework.serializers.CharField(max_length=32)

    class Meta:
        model = models.Comment
        fields = ('id', 'language', 'votes',
                  'source', 'commentary',
                  'tags')

    def create(self, validated_data):
        """`language` comes in as a char string. Here, we map
        the related Language object to the new Comment.
        """
        language_name = validated_data.get('language')
        validated_data['language'] = models.Language.objects.get(
            name=language_name)
        return models.Comment.objects.create(**validated_data)


class TagSerializer(
        rest_framework.serializers.HyperlinkedModelSerializer):

    class Meta:
        model = models.Tag
        fields = ('id', 'name')


class VoteSerializer(
        rest_framework.serializers.HyperlinkedModelSerializer):

    class Meta:
        model = models.Vote
        fields = ('id', 'comment', 'weight')

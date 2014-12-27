import rest_framework

import models


class LanguageSerializer(
        rest_framework.serializers.HyperlinkedModelSerializer):

    class Meta:
        model = models.Language
        fields = ('id', 'name')


class CommentSerializer(
        rest_framework.serializers.HyperlinkedModelSerializer):

    class Meta:
        model = models.Comment
        fields = ('id', 'language', 'votes',
                  'source', 'commentary',
                  'tags')


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

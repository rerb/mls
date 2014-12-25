from rest_framework import viewsets

import models
import serializers


class CommentViewSet(viewsets.ModelViewSet):
    '''
    API endpoint for Comment CRU.
    '''
    queryset = models.Comment.objects.all()
    serializer_class = serializers.CommentSerializer

    def post_save(self, comment, *args, **kwargs):
        if type(comment.tags) is list:
            # If tags were provided in the request.
            saved_comment = models.Comment.objects.get(pk=comment.pk)
            for tag in comment.tags:
                saved_comment.tags.add(tag)


class LanguageViewSet(viewsets.ModelViewSet):
    '''
    API endpoint for Language CRU.
    '''
    queryset = models.Language.objects.all()
    serializer_class = serializers.LanguageSerializer


class VoteViewSet(viewsets.ModelViewSet):
    '''
    API endpoint for Vote CRU.
    '''
    queryset = models.Vote.objects.all()
    serializer_class = serializers.VoteSerializer

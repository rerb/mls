from django.contrib.auth.models import User
from django.db import models
"""
;; serialized Comment:
{:id 1
 :source "..."
 :language "<url>"
 :commentary "Very pretty and artsy."
 :votes (int (rand 10))
 :tags [{:name "artsy"
         :url "http://www.example.com/tags/artsy"},
        {:name "pretty"
         :url "http://www.example.com/tags/pretty"}]
 :vote 0}
"""

API = "/items"  # returns items in default order, with vote for item for user

# let DRF worry about pagination


class Language(models.Model):

    name = models.CharField(max_length=8)

    def __unicode__(self):
        return self.name


class Tag(models.Model):

    name = models.CharField(max_length=16)

    def __unicode__(self):
        return self.name


class Comment(models.Model):

    source = models.TextField()
    language = models.ForeignKey(Language)
    commentary = models.TextField(blank=True, null=True)
    tags = models.ManyToManyField(Tag)

    def votes(self):
        total = 0
        for vote in Vote.objects.filter(comment=self):
            total += vote.weight
        return total


class Vote(models.Model):

    voter = models.ForeignKey(User, blank=True, null=True)
    comment = models.ForeignKey(Comment)
    weight = models.IntegerField()

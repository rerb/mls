# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('server', '0004_auto_20141225_0216'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='tags',
            field=models.ManyToManyField(to='server.Tag', null=True, blank=True),
            preserve_default=True,
        ),
    ]

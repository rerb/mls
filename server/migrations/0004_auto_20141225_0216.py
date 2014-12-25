# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('server', '0003_auto_20141225_0215'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vote',
            name='weight',
            field=models.IntegerField(),
            preserve_default=True,
        ),
    ]

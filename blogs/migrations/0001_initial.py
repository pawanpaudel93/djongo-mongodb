# Generated by Django 3.0.5 on 2021-04-29 04:57

import blogs.models
from django.db import migrations, models
import djongo.models.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('blog', djongo.models.fields.EmbeddedField(model_container=blogs.models.Blog)),
                ('meta_data', djongo.models.fields.EmbeddedField(model_container=blogs.models.MetaData)),
                ('headline', models.CharField(max_length=255)),
                ('body_text', models.TextField()),
                ('authors', djongo.models.fields.ArrayField(model_container=blogs.models.Author)),
                ('n_comments', models.IntegerField()),
            ],
        ),
    ]

# Generated by Django 4.0 on 2023-06-18 08:55

from django.db import migrations
import taggit.managers


class Migration(migrations.Migration):

    dependencies = [
        ('taggit', '0005_auto_20220424_2025'),
        ('artwork', '0019_remove_artworkpost_tags_delete_tag'),
    ]

    operations = [
        migrations.AddField(
            model_name='artworkpost',
            name='Tags',
            field=taggit.managers.TaggableManager(help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags'),
        ),
    ]
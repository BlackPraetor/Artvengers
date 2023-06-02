# Generated by Django 4.0 on 2023-06-02 06:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('artwork', '0014_carousel_tag_remove_artworkpost_tag_artworkpost_tags'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='name',
            new_name='artist_Name',
        ),
        migrations.AddField(
            model_name='profile',
            name='email',
            field=models.EmailField(default=1, max_length=254),
            preserve_default=False,
        ),
    ]

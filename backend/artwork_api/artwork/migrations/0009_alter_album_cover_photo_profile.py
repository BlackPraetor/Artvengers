# Generated by Django 4.0 on 2023-04-30 06:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('artwork', '0008_rename_title_album_album_title_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='Cover_Photo',
            field=models.ImageField(blank=True, null=True, upload_to='media/img/album_cover'),
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('social_media', models.TextField(blank=True)),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='auth.user')),
            ],
        ),
    ]

# Generated by Django 3.1.6 on 2021-08-21 20:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('reseau_artistes_app', '0002_auto_20210821_1837'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='comment_owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comment_owner', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='post',
            name='likes',
            field=models.ManyToManyField(default=None, related_name='likes', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='post',
            name='post_owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='post_owner', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='post',
            name='saves',
            field=models.ManyToManyField(default=None, related_name='saves', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='post',
            name='views',
            field=models.ManyToManyField(default=None, related_name='views', to=settings.AUTH_USER_MODEL),
        ),
        migrations.DeleteModel(
            name='Artist',
        ),
    ]

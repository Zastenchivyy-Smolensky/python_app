# Generated by Django 3.2.9 on 2021-11-27 11:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='group_owner', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField(max_length=100)),
                ('share_id', models.IntegerField(default=-1)),
                ('good_count', models.IntegerField(default=0)),
                ('share_count', models.IntegerField(default=0)),
                ('pub_date', models.DateTimeField(auto_now_add=True)),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sns.group')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='message_owner', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('-pub_date',),
            },
        ),
        migrations.CreateModel(
            name='Good',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='good_owner', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Friend',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sns.group')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='friend_onwner', to=settings.AUTH_USER_MODEL)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]

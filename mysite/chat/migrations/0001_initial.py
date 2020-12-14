# Generated by Django 3.1.4 on 2020-12-13 20:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ChatRoom',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('room_name', models.CharField(max_length=50)),
                ('room_create_time', models.DateTimeField(verbose_name='creation time')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=20)),
                ('chat_room', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='chat.chatroom')),
            ],
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message_text', models.CharField(max_length=200)),
                ('message_time', models.DateTimeField(verbose_name='message time')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='chat.user')),
            ],
        ),
    ]

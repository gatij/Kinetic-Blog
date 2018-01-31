# Generated by Django 2.0 on 2018-01-10 13:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Events',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(max_length=50)),
                ('fee', models.IntegerField(default=100)),
                ('maxteamsize', models.IntegerField(default=1)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bio', models.TextField(help_text='mention your year and course', max_length=500)),
                ('institute', models.CharField(default='myinstitute', max_length=50)),
                ('location', models.CharField(max_length=30)),
                ('birth_date', models.DateField(null=True)),
                ('phone_number', phonenumber_field.modelfields.PhoneNumberField(max_length=128, null=True, unique=True)),
                ('events', models.ManyToManyField(to='core.Events')),
            ],
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(max_length=25)),
                ('teamsize', models.IntegerField(default=1)),
                ('description', models.TextField(help_text='enter name(s) of your team')),
                ('event', models.ForeignKey(on_delete='models.CASCADE', to='core.Events')),
            ],
        ),
        migrations.AddField(
            model_name='profile',
            name='teams',
            field=models.ManyToManyField(to='core.Team'),
        ),
        migrations.AddField(
            model_name='profile',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]

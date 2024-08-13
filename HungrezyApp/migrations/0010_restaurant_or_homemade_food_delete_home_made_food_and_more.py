# Generated by Django 4.1.1 on 2022-10-23 02:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('HungrezyApp', '0009_alter_rider_contact_number'),
    ]

    operations = [
        migrations.CreateModel(
            name='restaurant_or_homemade_food',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=30)),
                ('address', models.TextField()),
                ('contact_number', models.CharField(max_length=11)),
                ('email', models.EmailField(max_length=30)),
                ('types', models.CharField(max_length=10)),
                ('rating', models.FloatField()),
                ('review', models.TextField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.DeleteModel(
            name='home_made_food',
        ),
        migrations.DeleteModel(
            name='restaurant',
        ),
    ]

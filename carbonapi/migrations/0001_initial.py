# Generated by Django 4.0.1 on 2022-03-07 10:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Usage_types',
            fields=[
                ('id', models.BigIntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('unit', models.CharField(max_length=100)),
                ('factor', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigIntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Usage',
            fields=[
                ('id', models.BigIntegerField(primary_key=True, serialize=False)),
                ('usage_type_id', models.BigIntegerField()),
                ('usage_at', models.DateTimeField()),
                ('date_created', models.DateField()),
                ('amount', models.FloatField()),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='carbonapi.user')),
            ],
        ),
    ]

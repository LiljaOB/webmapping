# Generated by Django 5.1.3 on 2024-11-09 15:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('world', '0002_profile'),
    ]

    operations = [
        migrations.CreateModel(
            name='CountryInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country', models.CharField(max_length=100)),
                ('region', models.CharField(max_length=100)),
                ('population', models.IntegerField()),
                ('area', models.IntegerField()),
                ('popDensity', models.IntegerField()),
                ('coastline', models.IntegerField()),
                ('migration', models.IntegerField()),
                ('infantMort', models.IntegerField()),
                ('gdp', models.IntegerField()),
                ('literacy', models.IntegerField()),
                ('phones', models.IntegerField()),
                ('arable', models.IntegerField()),
                ('crops', models.IntegerField()),
                ('other', models.IntegerField()),
                ('climate', models.IntegerField()),
                ('birthrate', models.IntegerField()),
                ('deathrate', models.IntegerField()),
                ('agriculture', models.IntegerField()),
                ('industry', models.IntegerField()),
                ('service', models.IntegerField()),
            ],
        ),
    ]

# Generated by Django 2.1.3 on 2019-02-03 08:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0005_delete_test'),
    ]

    operations = [
        migrations.CreateModel(
            name='Test',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('session', models.CharField(blank=True, default=None, max_length=128, null=True)),
            ],
        ),
    ]

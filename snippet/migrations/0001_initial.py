# Generated by Django 5.0.2 on 2024-03-01 13:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Snippet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('original_content', models.TextField()),
                ('encrypted_content', models.TextField(blank=True, null=True)),
                ('key', models.CharField(blank=True, max_length=255, null=True)),
            ],
        ),
    ]

# Generated by Django 4.2.6 on 2023-11-18 17:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_blog_contacts_remove_category_created_at'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Blog',
        ),
    ]
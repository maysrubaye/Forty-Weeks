# Generated by Django 2.2.9 on 2020-04-25 20:07

from django.db import migrations
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0012_homepage_scroll_text'),
    ]

    operations = [
        migrations.AddField(
            model_name='poem',
            name='semester_sent',
            field=wagtail.core.fields.RichTextField(blank=True),
        ),
    ]
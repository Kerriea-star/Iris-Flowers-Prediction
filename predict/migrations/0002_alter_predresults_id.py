# Generated by Django 4.1.5 on 2023-03-02 04:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("predict", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="predresults",
            name="id",
            field=models.BigAutoField(
                auto_created=True, primary_key=True, serialize=False, verbose_name="ID"
            ),
        ),
    ]

# Generated by Django 5.0.6 on 2025-02-10 05:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("organs", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="contact",
            old_name="sno",
            new_name="msg_id",
        ),
        migrations.RemoveField(
            model_name="contact",
            name="message",
        ),
        migrations.RemoveField(
            model_name="contact",
            name="timeStamp",
        ),
        migrations.AddField(
            model_name="contact",
            name="desc",
            field=models.CharField(default="", max_length=500),
        ),
        migrations.AlterField(
            model_name="contact",
            name="email",
            field=models.CharField(default="", max_length=70),
        ),
        migrations.AlterField(
            model_name="contact",
            name="name",
            field=models.CharField(max_length=70),
        ),
        migrations.AlterField(
            model_name="contact",
            name="phone",
            field=models.CharField(default="", max_length=70),
        ),
    ]

# Generated by Django 4.2.6 on 2024-08-22 07:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("quiz", "0002_question_main_category"),
    ]

    operations = [
        migrations.AddField(
            model_name="category",
            name="main_field_name",
            field=models.ForeignKey(
                default=2,
                on_delete=django.db.models.deletion.CASCADE,
                to="quiz.main_field",
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="sub_category",
            name="Main_field_name",
            field=models.ForeignKey(
                default=2,
                on_delete=django.db.models.deletion.CASCADE,
                to="quiz.main_field",
            ),
            preserve_default=False,
        ),
    ]

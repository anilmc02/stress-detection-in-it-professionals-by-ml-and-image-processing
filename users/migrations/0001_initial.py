# Generated by Django 4.2 on 2023-12-02 03:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="UserImagePredictinModel",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("username", models.CharField(max_length=100)),
                ("email", models.CharField(max_length=100)),
                ("loginid", models.CharField(max_length=100)),
                ("filename", models.CharField(max_length=100)),
                ("emotions", models.CharField(max_length=100000)),
                ("file", models.FileField(upload_to="files/")),
                ("cdate", models.DateTimeField(auto_now_add=True)),
            ],
            options={
                "db_table": "UserImageEmotions",
            },
        ),
        migrations.CreateModel(
            name="UserRegistrationModel",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=100)),
                ("loginid", models.CharField(max_length=100, unique=True)),
                ("password", models.CharField(max_length=100)),
                ("mobile", models.CharField(max_length=100, unique=True)),
                ("email", models.CharField(max_length=100, unique=True)),
                ("locality", models.CharField(max_length=100)),
                ("address", models.CharField(max_length=1000)),
                ("city", models.CharField(max_length=100)),
                ("state", models.CharField(max_length=100)),
                ("status", models.CharField(max_length=100)),
            ],
            options={
                "db_table": "UserRegistrations",
            },
        ),
        migrations.CreateModel(
            name="SurveyResponseModel",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "question1",
                    models.CharField(
                        choices=[
                            ("a", "Yes, frequently"),
                            ("b", "Sometimes"),
                            ("c", "Rarely"),
                            ("d", "Not at all"),
                        ],
                        max_length=100,
                    ),
                ),
                (
                    "question2",
                    models.CharField(
                        choices=[
                            ("a", "Yes, frequently"),
                            ("b", "Sometimes"),
                            ("c", "Rarely"),
                            ("d", "Not at all"),
                        ],
                        max_length=100,
                    ),
                ),
                (
                    "question3",
                    models.CharField(
                        choices=[
                            ("a", "Yes, frequently"),
                            ("b", "Sometimes"),
                            ("c", "Rarely"),
                            ("d", "Not at all"),
                        ],
                        max_length=100,
                    ),
                ),
                (
                    "question4",
                    models.CharField(
                        choices=[
                            ("a", "Yes, frequently"),
                            ("b", "Sometimes"),
                            ("c", "Rarely"),
                            ("d", "Not at all"),
                        ],
                        max_length=100,
                    ),
                ),
                (
                    "question5",
                    models.CharField(
                        choices=[
                            ("a", "Yes, frequently"),
                            ("b", "Sometimes"),
                            ("c", "Rarely"),
                            ("d", "Not at all"),
                        ],
                        max_length=100,
                    ),
                ),
                (
                    "question6",
                    models.CharField(
                        choices=[
                            ("a", "Yes, frequently"),
                            ("b", "Sometimes"),
                            ("c", "Rarely"),
                            ("d", "Not at all"),
                        ],
                        max_length=100,
                    ),
                ),
                (
                    "question7",
                    models.CharField(
                        choices=[
                            ("a", "Yes, frequently"),
                            ("b", "Sometimes"),
                            ("c", "Rarely"),
                            ("d", "Not at all"),
                        ],
                        max_length=100,
                    ),
                ),
                (
                    "question8",
                    models.CharField(
                        choices=[
                            ("a", "Yes, frequently"),
                            ("b", "Sometimes"),
                            ("c", "Rarely"),
                            ("d", "Not at all"),
                        ],
                        max_length=100,
                    ),
                ),
                (
                    "question9",
                    models.CharField(
                        choices=[
                            ("a", "Yes, frequently"),
                            ("b", "Sometimes"),
                            ("c", "Rarely"),
                            ("d", "Not at all"),
                        ],
                        max_length=100,
                    ),
                ),
                (
                    "question10",
                    models.CharField(
                        choices=[
                            ("a", "Yes, frequently"),
                            ("b", "Sometimes"),
                            ("c", "Rarely"),
                            ("d", "Not at all"),
                        ],
                        max_length=100,
                    ),
                ),
                (
                    "question11",
                    models.CharField(
                        choices=[
                            ("a", "Yes, frequently"),
                            ("b", "Sometimes"),
                            ("c", "Rarely"),
                            ("d", "Not at all"),
                        ],
                        max_length=100,
                    ),
                ),
                (
                    "question12",
                    models.CharField(
                        choices=[
                            ("a", "Yes, frequently"),
                            ("b", "Sometimes"),
                            ("c", "Rarely"),
                            ("d", "Not at all"),
                        ],
                        max_length=100,
                    ),
                ),
                (
                    "question13",
                    models.CharField(
                        choices=[
                            ("a", "Yes, frequently"),
                            ("b", "Sometimes"),
                            ("c", "Rarely"),
                            ("d", "Not at all"),
                        ],
                        max_length=100,
                    ),
                ),
                (
                    "question14",
                    models.CharField(
                        choices=[
                            ("a", "Yes, frequently"),
                            ("b", "Sometimes"),
                            ("c", "Rarely"),
                            ("d", "Not at all"),
                        ],
                        max_length=100,
                    ),
                ),
                (
                    "question15",
                    models.CharField(
                        choices=[
                            ("a", "Yes, frequently"),
                            ("b", "Sometimes"),
                            ("c", "Rarely"),
                            ("d", "Not at all"),
                        ],
                        max_length=100,
                    ),
                ),
                ("stress_level", models.CharField(max_length=100)),
                ("survey_score", models.IntegerField()),
                (
                    "user_prediction",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="users.userimagepredictinmodel",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="CombinedResultModel",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("stress_level_from_image", models.CharField(max_length=100)),
                ("emotion_from_image", models.CharField(max_length=100)),
                (
                    "survey_response",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="users.surveyresponsemodel",
                    ),
                ),
                (
                    "user_prediction",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="users.userimagepredictinmodel",
                    ),
                ),
            ],
            options={
                "db_table": "CombinedResults",
            },
        ),
    ]

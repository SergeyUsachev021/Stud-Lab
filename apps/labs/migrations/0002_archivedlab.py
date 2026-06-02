from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('labs', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ArchivedLab',
            fields=[
                (
                    'id',
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name='ID',
                    ),
                ),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                (
                    'lab',
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name='archive_items',
                        to='labs.lab',
                    ),
                ),
                (
                    'user',
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name='archived_labs',
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                'verbose_name': 'Лабораторная в архиве',
                'verbose_name_plural': 'Архив лабораторных',
                'ordering': ['-created_at'],
            },
        ),
        migrations.AddConstraint(
            model_name='archivedlab',
            constraint=models.UniqueConstraint(
                fields=('user', 'lab'),
                name='unique_archived_lab_per_user',
            ),
        ),
    ]
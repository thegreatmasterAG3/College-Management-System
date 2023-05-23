# Generated by Django 4.2 on 2023-05-15 02:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0010_staff_leave'),
    ]

    operations = [
        migrations.CreateModel(
            name='Staff_Feedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('feedback', models.TextField()),
                ('feedback_reply', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now_add=True)),
                ('staff_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.staff')),
            ],
        ),
    ]

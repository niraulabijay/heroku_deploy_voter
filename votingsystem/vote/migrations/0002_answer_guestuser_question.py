# Generated by Django 3.0.5 on 2020-04-29 14:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('vote', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='GuestUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ipaddress', models.GenericIPAddressField(unique=True)),
                ('latitude', models.CharField(blank=True, max_length=255, null=True)),
                ('longitude', models.CharField(blank=True, max_length=255, null=True)),
                ('status', models.CharField(blank=True, choices=[('Active', 'Active'), ('Inactive', 'Inactive'), ('Block', 'Block'), ('Suspended', 'Suspended')], max_length=20, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, unique=True)),
                ('slug', models.CharField(max_length=255, unique=True)),
                ('status', models.BooleanField(default=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='uploads/images/categories')),
                ('description', models.TextField(blank=True, null=True)),
                ('category_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='vote.Category')),
            ],
        ),
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, unique=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='uploads/images/categories')),
                ('description', models.TextField(blank=True, null=True)),
                ('question_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='vote.Question')),
            ],
        ),
    ]

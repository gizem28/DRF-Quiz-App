# Generated by Django 4.0.2 on 2022-03-09 20:16

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0004_alter_answer_is_right_alter_question_diffuculty_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='answer',
            name='choice1',
        ),
        migrations.RemoveField(
            model_name='answer',
            name='choice2',
        ),
        migrations.RemoveField(
            model_name='answer',
            name='choice3',
        ),
        migrations.RemoveField(
            model_name='answer',
            name='choice4',
        ),
        migrations.RemoveField(
            model_name='category',
            name='category',
        ),
        migrations.RemoveField(
            model_name='quiz',
            name='quiz',
        ),
        migrations.AddField(
            model_name='answer',
            name='answer',
            field=models.TextField(max_length=225, null=True),
        ),
        migrations.AddField(
            model_name='category',
            name='name',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='quiz',
            name='category',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, related_name='quiz', to='quiz.category'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='answer',
            name='is_right',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='answer',
            name='question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='answer', to='quiz.question'),
        ),
        migrations.AlterField(
            model_name='question',
            name='quiz',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='question', to='quiz.quiz'),
        ),
        migrations.AlterField(
            model_name='quiz',
            name='title',
            field=models.CharField(max_length=200),
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import model_utils.fields
from openedx.core.djangoapps.xmodule_django.models import CourseKeyField
import django.utils.timezone
from django.conf import settings


def reduce_duplicates(apps, schema_editor):
    """
    This will delete duplicate entries using a large number of small queries.

    This will help prevent blocking other access to the database.  There is a 
    race condition where new duplicates may be created while removing the first
    set of duplicates.  This is unavoidable, so the ADD UNIQUE INDEX operation 
    is written to expect and remove duplicates.  This operation is designed only 
    to reduce the amount of time the table will be locked.
    """

    CourseModuleCompletion = apps.get_model('progress', 'CourseModuleCompletion')
    tasks = CourseModuleCompletion.objects.values('course_id', 'content_id', 'user_id')
    tasks = tasks.annotate(count=models.Count('pk'), min_pk=models.Min('pk'))

    for task in tasks:
        if task['count'] > 1:
            qs = CourseModuleCompletion.objects.filter(
                user_id=task['user_id'],
                course_id=task['course_id'],
                content_id=task['content_id'],
            )
            qs = qs.exclude(pk=task['min_pk'])
            qs.delete()


class Migration(migrations.Migration):

    dependencies = [
        ('progress', '0001_initial')
    ]

    operations = [
        migrations.RunPython(
            code=reduce_duplicates,
            reverse_code=migrations.RunPython.noop,
        ),
        migrations.RunSQL(
            sql="ALTER IGNORE TABLE progress_coursemodulecompletion ADD UNIQUE INDEX course_content_user_uniq (course_id, content_id, user_id);",
            reverse_sql="ALTER TABLE progress_coursemodulecompletion DROP INDEX course_content_user_uniq;",
            state_operations=[
                migrations.AlterUniqueTogether(
                    name='coursemodulecompletion',
                    unique_together=set([('course_id', 'content_id', 'user')]),
                ),
            ],
        ),
    ]


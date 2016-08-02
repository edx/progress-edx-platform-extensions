"""
app configuration
"""
from django.apps import AppConfig


class SolutionsAppProgressConfig(AppConfig):

    name = 'progress'
    verbose_name = 'progress app'

    def ready(self):

        # import signal handlers
        import progress.signals  # pylint: disable=unused-import

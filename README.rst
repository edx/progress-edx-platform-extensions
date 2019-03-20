progress-edx-platform-extensions
================================

progress-edx-platform-extensions (``progress``) is a Django application responsible for
calculating and persisting user's progress in different modules of a course.
Progress application computes user's progress in a course on ``post_save`` signale of
``CourseModuleCompletion`` model.

.. note::

    This application is now deprecated, please use
    `edx-completion <https://pypi.org/project/edx-completion/>`_ instead.


Open edX Platform Integration
-----------------------------
1. Update the version of ``progress-edx-platform-extensions`` in the appropriate requirements file (e.g. ``requirements/edx/custom.txt``).
2. Add ``progress`` to the list of installed apps in ``common.py``.
3. Set these feature flag in ``common.py``

.. code-block:: bash

  'MARK_PROGRESS_ON_GRADING_EVENT': True,
  'STUDENT_PROGRESS': True

4. Install progress app via requirements file

.. code-block:: bash

  $ pip install -r requirements/edx/custom.txt

5. (Optional) Run tests:

.. code-block:: bash

   $ python manage.py lms --settings test test progress.tests



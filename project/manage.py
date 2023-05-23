# """Django's command-line utility for administrative tasks."""
# import os
# import sys
# import coverage


# def main():
#     """Run administrative tasks."""
#     os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')

#     # Run tests with coverage
#     if len(sys.argv) > 1 and sys.argv[1] == 'test':
#         cov = coverage.Coverage(source=['memories'])
#         cov.start()

#     try:
#         from django.core.management import execute_from_command_line
#     except ImportError as exc:
#         raise ImportError(
#             "Couldn't import Django. Are you sure it's installed and "
#             "available on your PYTHONPATH environment variable? Did you "
#             "forget to activate a virtual environment?"
#         ) from exc

#     execute_from_command_line(sys.argv)

#     # Stop coverage and generate report
#     if len(sys.argv) > 1 and sys.argv[1] == 'test':
#         cov.stop()
#         cov.save()
#         cov.report()


# if __name__ == '__main__':
#     main()

#!/usr/bin/env python


import os
import sys


def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()

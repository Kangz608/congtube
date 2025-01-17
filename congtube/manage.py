#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys


def main():
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
    os.environ.setdefault('DJANGO_CONFIGURATION', 'Dev')

    from configurations.management import execute_from_command_line
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()

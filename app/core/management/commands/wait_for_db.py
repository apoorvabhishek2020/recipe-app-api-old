"""
Django command to wait for the database to be available.
"""
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    """Django command to wait for database to be available."""

    def handle(self, *args, **options):
        """Django method to wait for database."""
        print("Wait for database command executed.")
from django.core.management.base import BaseCommand

from courses.management.commands.add_courses_to_db import readThroughNTNUCourses


class Command(BaseCommand):
    help = 'Adds all ntnu courses to db'

    def handle(self, *args, **options):
        readThroughNTNUCourses('courses/ntnu-fag.txt')
from django.core.management.base import BaseCommand, CommandError

from courses.add_courses_to_db import readThroughNTNUCourses
from courses.models import Course

class Command(BaseCommand):
    help = 'Adds all ntnu courses to db'

    def handle(self, *args, **options):
        readThroughNTNUCourses('courses/ntnu-fag.txt')
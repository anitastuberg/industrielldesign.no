from courses.models import Course


def createEntry(name, course_code, course_display_without_reviews):
    Course.objects.create(name=name, course_code=course_code, display_without_reviews=course_display_without_reviews)


def readThroughNTNUCourses(filename):
    f = open(filename, 'r')
    for line in f.readlines():
        course_info = line.split('/')
        course_code = course_info[0].rstrip()
        course_name = course_info[1].rstrip()
        course_display_without_reviews = False
        if "TPD" in course_code:
            course_display_without_reviews = True
        createEntry(course_name, course_code, course_display_without_reviews)
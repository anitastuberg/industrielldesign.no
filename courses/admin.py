from django.contrib import admin

from .models import Course, CourseReview


class CourseReviewAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'author', 'timestamp']
    fields = ('text', 'author')

    class Meta:
        model = CourseReview


class CourseAdmin(admin.ModelAdmin):
    list_display = ["__str__"]
    fields = ('name', 'course_code', 'class_year', 'reviews')
    filter_horizontal = ['reviews']

    class Meta:
        model = Course


admin.site.register(Course, CourseAdmin)
admin.site.register(CourseReview, CourseReviewAdmin)
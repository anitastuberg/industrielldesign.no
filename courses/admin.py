from django.contrib import admin

from .models import Course, CourseReview, CourseLink, CourseFilter


class CourseLinkAdmin(admin.ModelAdmin):
    list_display = ['url_title', 'url', 'course']
    fields = ('url_title', 'url_description', 'img_url', 'url', 'course')

    class Meta:
        model = CourseLink


class CourseFilterAdmin(admin.ModelAdmin):
    list_display = ['name', 'color']

    class Meta:
        model = CourseFilter


class CourseReviewAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'author', 'timestamp']
    fields = ('text', 'author')

    class Meta:
        model = CourseReview


class CourseAdmin(admin.ModelAdmin):
    list_display = ["__str__", 'display_without_reviews', 'review_count', 'filter']
    fields = ('name', 'course_code', 'class_year', 'reviews', 'filter', 'display_without_reviews')
    filter_horizontal = ['reviews']
    ordering = ('-display_without_reviews', '-reviews')

    def review_count(self, obj):
        return obj.reviews.all().count()

    class Meta:
        model = Course


admin.site.register(Course, CourseAdmin)
admin.site.register(CourseReview, CourseReviewAdmin)
admin.site.register(CourseLink, CourseLinkAdmin)
admin.site.register(CourseFilter, CourseFilterAdmin)
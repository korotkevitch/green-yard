from django.contrib import admin


from .models import Sphere
class SphereAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'prefix')
admin.site.register(Sphere, SphereAdmin)


from .models import Service
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('name', 'service_id', 'anchor', 'short_description', 'long_description', 'slogan', 'image_preview')
admin.site.register(Service, ServiceAdmin)


from .models import Project
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'prefix_filter', 'image_preview')
admin.site.register(Project, ProjectAdmin)


from .models import Testimonial
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ('name', 'testimonial', 'image_preview')
admin.site.register(Testimonial, TestimonialAdmin)


from .models import Feedback
class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'massage')
admin.site.register(Feedback, FeedbackAdmin)

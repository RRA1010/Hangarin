from django.contrib import admin

# Register your models here.
from .models import Priority, Category, Task, Note, SubTask

#admin.site.register(Priority)
#admin.site.register(Category)
#admin.site.register(Task)
#admin.site.register(Note)
#admin.site.register(SubTask)

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('title','status','deadline','priority','category')
    list_filter = ('status','priority','category')
    search_fields = ('title','description',)

@admin.register(SubTask)
class SubTaskAdmin(admin.ModelAdmin):
    list_display = ('title','status','parent_task_name')
    list_filter = ('status',)
    search_fields = ('title',)

    def parent_task_name(self,obj):
        try:
            parent = Task.objects.get(id=obj.id)
            return parent.title
        except Task.DoesNotExist:
            return None

@admin.register(Priority)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

@admin.register(Note)
class NoteAdmin(admin.ModelAdmin):
    list_display = ('task','content','created_at',)
    list_filter = ('created_at',)
    search_fields = ('content',)
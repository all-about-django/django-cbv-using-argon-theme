from django.contrib import admin


class AuditModelAdmin(admin.ModelAdmin):

    exclude = ('created_by', 'updated_by',)

    def save_model(self, request, obj, form, change):
        if not obj.id:
            obj.created_by = request.user
            obj.updated_by = request.user
        if change and obj.id:
            obj.updated_by = request.user
        obj.save()

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser
from django.utils.translation import gettext_lazy as _
from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from .models import Article


@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ['username', 'email', 'date_of_birth', 'is_staff']
    fieldsets = UserAdmin.fieldsets + (
        (_('Additional Info'), {
            'fields': ('date_of_birth', 'profile_photo'),
        }),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (_('Additional Info'), {
            'fields': ('date_of_birth', 'profile_photo'),
        }),
    )

admin.site.register(CustomUser, CustomUserAdmin)

class Command(BaseCommand):
    help = "Set up groups and assign permissions"

    def handle(self, *args, **kwargs):
        content_type = ContentType.objects.get_for_model(Article)

        perms = {
            "can_view": Permission.objects.get(codename="can_view", content_type=content_type),
            "can_create": Permission.objects.get(codename="can_create", content_type=content_type),
            "can_edit": Permission.objects.get(codename="can_edit", content_type=content_type),
            "can_delete": Permission.objects.get(codename="can_delete", content_type=content_type),
        }

        # Group: Viewers
        viewers, _ = Group.objects.get_or_create(name="Viewers")
        viewers.permissions.set([perms["can_view"]])

        # Group: Editors
        editors, _ = Group.objects.get_or_create(name="Editors")
        editors.permissions.set([perms["can_view"], perms["can_create"], perms["can_edit"]])

        # Group: Admins
        admins, _ = Group.objects.get_or_create(name="Admins")
        admins.permissions.set(perms.values())

        self.stdout.write(self.style.SUCCESS("Groups and permissions have been set up."))


class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_year')
    list_filter = ('publication_year',)
    search_fields = ('title', 'author')

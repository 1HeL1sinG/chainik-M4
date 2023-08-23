from django.contrib import admin
from .models import Advertisement

class Advert_Admin(admin.ModelAdmin):

    list_display = ['id', 'title', 'description', 'price', 'created_date', 'updated_date', 'auction']
    list_filter = ['created_at', 'auction']
    list_editable = ['title']
    actions = ['make_auction_as_false', 'make_auction_as_true']
    fieldsets = (
        ('Общее', {
            'fields': ('title','description')
        }),
        ('Финансы', {
            'fields': ('price','auction'),
            'classes': ['collapse']
        }),
    )
    @admin.action(description="убрать торг нахер")
    def make_auction_as_false(self, request, queryset):
        queryset.update(auction=False)

    @admin.action(description="ладно пусть торгуются")
    def make_auction_as_true(self, request, queryset):
        queryset.update(auction=True)
    
admin.site.register(Advertisement, Advert_Admin)
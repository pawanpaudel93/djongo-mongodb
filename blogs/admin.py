from django.contrib import admin
from django.contrib.admin.sites import AlreadyRegistered
from blogs.models import *
from django.apps import apps

def auto_register(model):
    # Get all fields from model, but exclude autocreated reverse relations1=
    field_list = [f.name for f in model._meta.get_fields() if f.auto_created is False]
    field_list.insert(0, 'id')
    search_fields = [f.name for f in model._meta.get_fields() if f.auto_created is False]

    # Dynamically create ModelAdmin class and register it.
    my_admin = type('MyAdmin', (admin.ModelAdmin,),
                    {'list_display': field_list, 'ordering': ['id', ],
                     'search_fields': search_fields,
                     'list_per_page': 50,
                     },
                    )

    try:
        admin.site.register(model, my_admin)
    except AlreadyRegistered:
        # This model is already registered
        pass


for model in apps.get_app_config('blogs').get_models():
    auto_register(model)
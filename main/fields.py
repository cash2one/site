# -*- coding: utf-8 -*-
from django.db.models import OneToOneField
from django.db.models.fields.related import SingleRelatedObjectDescriptor


class AutoSingleRelatedObjectDescriptor(SingleRelatedObjectDescriptor):
    def __get__(self, instance, instance_type=None):
        try:
            return super(AutoSingleRelatedObjectDescriptor, self).__get__(instance, instance_type)
        except self.related.model.DoesNotExist:
            obj = self.related.model(**{self.related.field.name: instance})
            obj.save()
            # Don't return obj directly, otherwise it won't be added
            # to Django's cache, and the first 2 calls to obj.relobj
            # will return 2 different in-memory objects
            return super(AutoSingleRelatedObjectDescriptor, self).__get__(instance, instance_type)


class AutoOneToOneField(OneToOneField):
    def contribute_to_related_class(self, cls, related):
        setattr(cls, related.get_accessor_name(), AutoSingleRelatedObjectDescriptor(related))

    def south_field_triple(self):
        from south.modelsinspector import introspector
        field_class = OneToOneField.__module__ + '.' + OneToOneField.__name__
        args, kwargs = introspector(self)
        return (field_class, args, kwargs)

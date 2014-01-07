from google.appengine.ext import ndb
from google.appengine.ext.ndb import polymodel
from protorpc import remote

from endpoints_proto_datastore.ndb import EndpointsModel
from endpoints_proto_datastore.ndb.model import _EndpointsQueryInfo


def _DowncastMessage(message, final_message_class):
  message_class = message.__class__

  downcasted_message = final_message_class()
  for field in final_message_class.all_fields():
    # KeyError allowed to happen, if the field is missing,
    # a downcast should be performed
    field_on_message = message_class.field_by_name(field.name)
    # Make sure fields are the same type
    if field_on_message.__class__ != field.__class__:
      raise TypeError('Downcasted field of the wrong type: %r. Should be %r.' %
                      (field_on_message.__class__, field.__class__))
    value = getattr(message, field.name)
    setattr(downcasted_message, field.name, value)
  return downcasted_message


class _PolyModelQueryInfo(_EndpointsQueryInfo):

  def _PopulateFilters(self):
    entity = self._entity
    for prop in entity._properties.itervalues():
      if isinstance(prop, polymodel._ClassKeyProperty):
        continue
      attr_name = prop._code_name
      current_value = getattr(entity, attr_name)

      # Only filter for non-null values
      if current_value is not None:
        self._AddFilter(prop == current_value)

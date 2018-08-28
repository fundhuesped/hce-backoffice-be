from dynamic_preferences.types import BooleanPreference
from dynamic_preferences.types import FilePreference
from dynamic_preferences.types import BaseSerializer 
from dynamic_preferences.types import string_types

from dynamic_preferences.preferences import Section
from dynamic_preferences.registries import global_preferences_registry

# we create some section objects to link related preferences together

general = Section('general')

# We start with a global preference
@global_preferences_registry.register
class PrescriptionHeaderImage(FilePreference):
    section = general
    name = 'prescription_header_image'


from django.forms import ModelChoiceField


class FirstAndLastNameChoiceField(ModelChoiceField):
    """Display first and last name for user dropdown.
    """
    def label_from_instance(self, obj):
        return ' '.join([obj.userprofile.first_name, obj.userprofile.last_name])

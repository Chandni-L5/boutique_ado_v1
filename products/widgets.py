from django.forms.widgets import ClearableFileInput
from django.utils.translation import gettext_lazy as _


class CustomClearableFileInput(ClearableFileInput):
    """ Custom clearable file input that uses Bootstrap classes. """

    clear_checkbox_label = _('Remove')
    initial_text = _('Current Image')
    input_text = _('Change Image')
    template_name = 'products/custom_widget_templates/custom_clearable_file_input.html'
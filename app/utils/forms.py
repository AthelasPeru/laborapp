# coding: utf-8
"""
General usage forms
"""
from wtforms import SelectMultipleField, widgets, TextField
from flask_wtf import Form
from wtforms.validators import Required


class MultiCheckboxField(SelectMultipleField):
    """Base for Multicheckbox forms"""

    widget = widgets.ListWidget(prefix_label=False)
    option_widget = widgets.CheckboxInput()
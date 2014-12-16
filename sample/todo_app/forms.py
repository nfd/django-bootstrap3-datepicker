from django import forms

from bootstrap3_datepicker.fields import DatePickerField
from bootstrap3_datepicker.widgets import DatePickerInput


class ToDoForm(forms.Form):
    # normal date field with no picker
    date_1 = forms.DateField()

    # date field with default picker, uses locale default date format for display and decode
    date_2 = forms.DateField(widget=DatePickerInput())

    # date field with picker, uses specified format for display, decode is via locale default input_formats so format
    # specified must match one
    date_3 = forms.DateField(widget=DatePickerInput(format="%Y-%m-%d"))

    # date field with picker, uses specified format for display and input_formats for decode
    date_4 = forms.DateField(input_formats=["%B %Y"],
                             widget=DatePickerInput(format="%B %Y",
                                                    attrs={"placeholder": "Placeholder text"},
                                                    options={"minViewMode": "months"}))

    # date picker field, uses locale default date format for display and decode, same as date_2
    date_5 = DatePickerField()

    # date field with picker, uses specified format for display and decode, same as date_3
    date_6 = DatePickerField(input_formats=["%Y-%m-%d"])

    # custom format with picker options specified, uses specified format for display and decode, same as date_4
    date_7 = DatePickerField(input_formats=["%B %Y"],
                             widget_attrs={"placeholder": "Placeholder text"},
                             widget_options={"minViewMode": "months"})

    # just to prove a point, pass in a different widget (if you do this you've missed the point)
    date_8 = DatePickerField(input_formats=["%d %B %Y"],
                             widget=forms.TextInput())

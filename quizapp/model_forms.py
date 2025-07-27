from django import forms
from .models import Survey

FIELD_TYPE_MAP = {
    "text": forms.CharField,
    "email": forms.EmailField,
    "integer": forms.IntegerField,
    "boolean": forms.BooleanField,
}

class DynamicSurveyForm(forms.ModelForm):
    class Meta:
        model = Survey
        fields = []  

    def __init__(self, *args, **kwargs):
        survey_instance = kwargs.pop('survey_instance', None)
        super().__init__(*args, **kwargs)

        if survey_instance and survey_instance.questions_json:
            for question in survey_instance.questions_json:
                field_type = FIELD_TYPE_MAP.get(question.get("type"), forms.CharField)
                field_name = question.get("name")
                label = question.get("label", field_name)

                self.fields[field_name] = field_type(label=label, required=False)

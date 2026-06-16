from django import forms

class AIQueryForm(forms.Form):
    symptoms = forms.CharField(
        widget=forms.Textarea(attrs={
            'class': 'form-control',
            'rows': 5,
            'placeholder': 'Describe symptoms or health situation... (e.g., I have a headache, fever, and sore throat)',
            'id': 'symptoms-input'
        }),
        label='Describe Your Symptoms',
        max_length=2000
    )

    def clean_symptoms(self):
        symptoms = self.cleaned_data.get('symptoms', '').strip()
        if len(symptoms) < 10:
            raise forms.ValidationError('Please provide a more detailed description (at least 10 characters).')
        return symptoms

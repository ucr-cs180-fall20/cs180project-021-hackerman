from django import forms

class USForm(forms.Form):
	channel_title = forms.CharField(required=True, label='Channel name:')
	video_id = forms.CharField(required=False, label='Video ID:')
	publish_date = forms.DateField(required=False, label='Publish Date:')
	category_id = forms.IntegerField(required=False, label='Category ID:')
	tags = forms.CharField(required=False, label='Tags:')

COUNTRIES = [
  ('GB', 'Great Britain'),
  ('CA', 'Canada'),
  ('DE', 'Germany'),
  ('US', 'United States')
]

class countriesForm(forms.Form):
	country = forms.CharField(required=True, label='Country')
	channel_title = forms.CharField(required=False, label='Channel name:')
	video_id = forms.CharField(required=False, label='Video ID:')
	publish_date = forms.DateField(required=False, label='Publish Date:')
	category_id = forms.IntegerField(required=False, label='Category ID:')
	tags = forms.CharField(required=False, label='Tags:')
	country= forms.CharField(label='Choose a country', widget=forms.Select(choices=COUNTRIES))
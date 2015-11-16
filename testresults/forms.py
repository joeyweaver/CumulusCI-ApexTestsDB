from django import forms

class TestResultUploadForm(forms.Form):
    package = forms.CharField(max_length=255)
    repository_url = forms.CharField(max_length=255)
    branch_name = forms.CharField(max_length=255)
    commit_sha = forms.CharField(max_length=255)
    execution_name = forms.CharField(max_length=255)
    execution_url = forms.CharField(max_length=255)
    environment_name = forms.CharField(max_length=255)
    results_file_url = forms.URLField(max_length=255)

from django import forms

from assignment.models import AssignmentAns


class assignsol(forms.ModelForm):
    class Meta:
        model = AssignmentAns
        fields = [ 'Paper', 'Title','sub','Solution','Attachment',]
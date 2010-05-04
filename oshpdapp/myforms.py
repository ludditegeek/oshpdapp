#myforms.py
# contains some manually layed out forms

from django import forms

class TForm (forms.Form):
    # need template for this form
    name = forms.CharField(max_length=12, label = 'name', initial='name')
    c1 = forms.BooleanField(required=False, label = 'C1', initial = True)    
    c2 = forms.BooleanField(required=False, label = 'C2')
    c3 = forms.BooleanField(required=False, label = 'C3',  initial = True)
    c4 = forms.BooleanField(required=False, label = 'C4')
    
 
    
    


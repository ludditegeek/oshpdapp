from django import forms
from oshpdapp.models import *
from django.forms import ModelForm
from models import *

class   PrescreenForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        #define some read only fields on this form
        super(PrescreenForm, self).__init__(*args, **kwargs)
        instance = getattr(self, 'instance', None)
        if instance and instance.id:
            self.fields['absstatus'].widget.attrs['disabled'] = 'disabled'
            self.fields['ssn'].widget.attrs['readonly'] = True
            self.fields['bthdate'].widget.attrs['readonly'] = True
            self.fields['hospid'].widget.attrs['readonly'] = True
            self.fields['hospname'].widget.attrs['readonly'] = True
            self.fields['hospname'].widget.attrs['readonly'] = True
            self.fields['admtdate'].widget.attrs['readonly'] = True            
            self.fields['dschdate'].widget.attrs['readonly'] = True

    def clean_absstatus(self):
        # Save and restore value for FK items/dropdowns
        # see link: http://stackoverflow.com/questions/324477/in-a-django-form-how-to-make-a-field-readonly-or-disabled-so-that-it-cannot-be
        instance = getattr(self, 'instance', None)
        if instance:
            return instance.absstatus
        else:
            return self.cleaned_data.get('absstatus', None)

    #ADM_CHOICES= (('M', 'Male'),('F', 'Female'), ('U', 'Ukn'))

    memo = forms.CharField(max_length=255,  widget=forms.Textarea)
    # Display Date (w/out time)
    bthdate = forms.DateField(label = 'Date of Birth')    
    admtdate = forms.DateField(label = 'Admission Date')
    dschdate = forms.DateField(label = 'Discharge Date')

    srcpapermr =forms.BooleanField(label ='Paper MR', required=False)
    srcemr =forms.BooleanField(label ='Electronic MR', required=False)
    srcmicrofiche =forms.BooleanField(label ='Microfiche', required=False)
    srcscanned = forms.BooleanField(label = 'Scanned', required=False)
     
    # Admission Source
    #admsource = forms.CharField(widget=forms.Select(choices=ADM_CHOICES))
       
    class Meta:
        model = Ptmaster 
        # specify subset of fields on this form - fields are displayed in the order specified
        fields = ('absstatus', 'ssn', 'bthdate', 'hospid', 'hospname',  
                'admtdate', 'dschdate', 
                'ssncrct', 'bthdatecrct',
                'admsource', 'source2',                               
                'disp', 'memo'
                ) 
                
class   AbstractionForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        # define any read only fields on this form
        super(AbstractionForm, self).__init__(*args, **kwargs)
        instance = getattr(self, 'instance', None)
        if instance and instance.id:
            self.fields['absstatus'].widget.attrs['disabled'] = 'disabled'
            self.fields['ssn'].widget.attrs['readonly'] = True
            self.fields['bthdate'].widget.attrs['readonly'] = True
            
    ynchoices = Codetbl.get_code_choices('YESNO')
    # Define required fields here        
    memo = forms.CharField(max_length=255,  widget=forms.Textarea,
            required=True, error_messages={'required':'Memo Field cannot be empty'})
    abstrec = forms.CharField(max_length=255,  widget=forms.TextInput,
              required=True, error_messages={'required':'Patient MRN field is required'})
    patzip = forms.CharField(max_length=255,  widget=forms.TextInput,
              required=True, error_messages={'required':'ZIP Code field is required'})
    #codestatus = forms.CharField(max_length=255,  widget=forms.Select(choices=cstatchoices))
    dnrad = forms.CharField(max_length=255,  widget=forms.Select (choices=ynchoices),
            required=True, error_messages={'required':'DNR Order at Admission field is required'})

    bthdate = forms.DateField(label = 'Date of Birth')    
        
    def clean_absstatus(self):
        # Save and restore value for FK items/dropdowns - otherwise these get zapped
        # see link: http://stackoverflow.com/questions/324477/in-a-django-form-how-to-make-a-field-readonly-or-disabled-so-that-it-cannot-be
        instance = getattr(self, 'instance', None)
        if instance:
            return instance.absstatus
        else:
            return self.cleaned_data.get('absstatus', None)    
            

    class Meta:
        model = Ptmaster 
        # specify subset of fields on this form - fields are displayed in the order specified
        fields = ('absstatus', 'ssn', 'bthdate', 'patzip' , 'abstrec', 'sex', 'admtype' , 
                  'dnrad', 'crosswalk', 'hospracecode',
                  'racewht', 'raceblk', 'racena', 
                  'raceapi', 'raceoth', 'raceunk' ,
                  'ethncty', 'memo'
                  ) 

        #fields = ('absstatus', 'ssn', 'bthdate', 'hospid', 'hospname')  
#        fields = ('absstatus', 'ssn', 'bthdate', 'patzip' , 'abstrec', 'sex', 'admtype',
#                  'dnrad', 'crosswalk', 'hospracecode'                
#                  )
 

class   DxForm(forms.ModelForm):

#    def __init__(self, *args, **kwargs):
#        define some read only fields on this form
#        super(DxForm, self).__init__(*args, **kwargs)
#        instance = getattr(self, 'instance', None)
#        
#        if instance and instance.id:
#            self.fields['absstatus'].widget.attrs['disabled'] = 'disabled'

    dxseq = forms.CharField(max_length=12)


    class Meta:
        model = Ptdx 
        # specify subset of fields on this form - fields are displayed in the order specified                      
        #fields = ('id', 'studyid', 'dxseq'
        #          )

        fields = ('dxseq', 'dxtype',
                 'dxcodeicd9oshpd', 'dxcodeicd9',                  
                 'dxcodeicd9dscr','dxcrct'
                  )
                                                      
 
class   DtlsForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        #define read only fields on this form
	super(DtlsForm, self).__init__(*args, **kwargs)
	instance = getattr(self, 'instance', None)
	if instance and instance.id:
	    #self.fields['icd9codedscr'].widget.attrs['disabled'] = 'disabled'
	    #self.fields['icd9codedscr'].widget.attrs['readonly'] = True
	    pass
	    
	    
    # Define choices based on codetable entries
    # Code Type Choices (Diag/Pcode/Ecode)
    ctypechoices = Codetbl.get_code_choices('CODETYPE')            
    # Code Status Choices
    cstatchoices = Codetbl.get_code_choices('CODESTATUS')    
    # Condition Present At Admission
    cpaachoices = Codetbl.get_code_choices('CPAATYPE')    
    
    # Code Status Choices
    codetype = forms.CharField(max_length=255,  widget=forms.Select(choices=ctypechoices))            
    codestatus = forms.CharField(max_length=255,  widget=forms.Select(choices=cstatchoices))
    diagcpaa = forms.CharField(max_length=255, widget=forms.Select(choices=cpaachoices), required=True) 

    diagcodeicd9 = forms.CharField(max_length=12,  widget=forms.TextInput,
                              error_messages={'required':'ICD9 Code is required - select from list'}) 

    # Form to collect patient details/dx code info
    # Specify custom error validation message text
    memo = forms.CharField(max_length=255,  widget=forms.Textarea,
            required=True, error_messages={'required':'Memo Field cannot be empty'})

    # Define validation rules
    # Rqd fields are: ICD9 code (via lookup); Memo Field 
    # these are defined in the form class = *Not in the View*
    def clean(self):
        # (We only get here if no prior error found

        cleaned_data = self.cleaned_data
        memo = cleaned_data.get('memo')

        icd9 = cleaned_data.get('diagcodeicd9')

        errstr =''
        if memo == None or memo=='':
            errstr +=  ' Memoxxx field is required'
            #self.errors.append('Memo field is required')
            #raise forms.ValidationError ("Memo field is required")

        if icd9 == None or icd9=='':
            errstr +=  ', ICD9xxx field is required'
                #self.errors.append('ICD9 code is required')
                #raise forms.ValidationError ("ICD9 code is required")

        if errstr!='':
            pass
            #raise forms.ValidationError (errstr)

        return self.cleaned_data


    class Meta:
        model = Ptdx 
        
        # specify subset of fields on this form - fields are displayed in the order specified                      
        
        fields = ('codetype', 'codestatus', 'diagcpaa',
                 'diagcodeicd9',                   
                 'icd9codedscr','memo'
                  )
                    
# *****************  Redundant - use Dtls form instead *******************        
class   CstmDtlsForm(forms.Form):
    # Custom Form for dtls entry - 
    # Note does not use forms.ModelForm as we need to customize this
    # Identify fields and corresponding display widgets

    def __init__(self, *args, **kwargs):
        #define read only fields on this form
	super(CstmDtlsForm, self).__init__(*args, **kwargs)
	instance = getattr(self, 'instance', None)
	if instance and instance.id:
	    self.fields['icd9codedscr'].widget.attrs['disabled'] = 'disabled'
	    self.fields['icd9codedscr'].widget.attrs['readonly'] = True
	  
    # Define choices based on codetable entries
    # Code Type Choices (Diag/Pcode/Ecode)
    ctypechoices = Codetbl.get_code_choices('CODETYPE')            
    # Code Status Choices
    cstatchoices = Codetbl.get_code_choices('CODESTATUS')    
    # Condition Present At Admission
    cpaachoices = Codetbl.get_code_choices('CPAATYPE')    
    
    # Code Status Choices
    codetype = forms.CharField(max_length=255,  widget=forms.Select(choices=ctypechoices))            
    codestatus = forms.CharField(max_length=255,  widget=forms.Select(choices=cstatchoices))
    diagcpaa = forms.CharField(max_length=255, widget=forms.Select(choices=cpaachoices)) 
   
    # Display Field - populated via lookup
   # diagcodeicd9 = forms.CharField(max_length=255, widget=forms.TextInput(attrs={'size': '35'}))
   # memo = forms.CharField(max_length=255,  widget=forms.TextInput)
                                
class   SearchForm(forms.Form):
    # Create a Search Form
    query = forms.CharField(
    label=u'Search by Patient SSN ',
    widget=forms.TextInput(attrs={'size': 32})
    )
                    

# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#     * Rearrange models' order
#     * Make sure each model has one field with primary_key=True
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin.py sqlcustom [appname]'
# into your database.

from django.db import models

#from utils import *

class Codetbl(models.Model):
    id = models.IntegerField(primary_key=True)
    #id = models.AutoField(primary_key=True)
    dspseq = models.IntegerField(null=True, blank=True)
    codetype = models.TextField(blank=False)
    codesubtype = models.TextField(blank=True)
    codeval = models.TextField(blank=False)
    codedscr = models.TextField(blank=False)
    class Meta:
        db_table = u'codetbl'
        
    def __unicode__(self):
            return self.codetype
            
    #@staticmethod   
    @classmethod   
    # define class method here -      
    def get_code_choices(cls,codetype):
        
        clist = []
        #clist =( Codetbl.objects.filter(codetype=codetype).order_by('dspseq'))
        clist =( cls.objects.filter(codetype=codetype).order_by('dspseq'))
                
        ec  = []    # entity choices
        for i in range(len(clist)):
            x = (clist[i].codeval, clist[i].codedscr)
            ec.append(x)
        # build a list of tuples
        choices = tuple(ec)
        return choices              

class Icd9Base(models.Model):
    id = models.IntegerField(primary_key=True)
    icd9cm_code = models.CharField(max_length=12, db_column=u'ICD9CM_CODE', blank=True)
    validity = models.CharField(max_length=255, db_column=u'VALIDITY', blank=True)
    short_description = models.CharField(max_length=255, db_column=u'SHORT_DESCRIPTION', blank=True)
    long_description = models.CharField(max_length=255, db_column=u'LONG_DESCRIPTION', blank=True)
    full_description = models.CharField(max_length=255, db_column=u'FULL_DESCRIPTION', blank=True)
    status = models.CharField(max_length=255, db_column=u'STATUS', blank=True)
    type = models.IntegerField(null=True, db_column=u'TYPE', blank=True)
    class Meta:
        db_table = u'icd9base'
    
    @classmethod    
    # get results for selected code lookup value
    def get_icd9_info(cls, codeval):
        res = cls.objects.filter(icd9cm_code=codeval)
        # return list of matching values
        return res
    

class OshdUsers(models.Model):
    id = models.IntegerField(primary_key=True)
    userid = models.CharField(max_length=12, db_column=u'UserID', blank=True)
    password = models.CharField(max_length=8, db_column=u'Password', blank=True)
    lname = models.CharField(max_length=25, db_column=u'Lname', blank=True)
    fname = models.CharField(max_length=25, db_column=u'Fname', blank=True)
    lastlogon = models.DateTimeField(null=True, db_column=u'LastLogon', blank=True)
    lastlogoff = models.DateTimeField(null=True, db_column=u'LastLogoff', blank=True)
    loggedon = models.SmallIntegerField(db_column=u'LoggedOn')
    class Meta:
        db_table = u'oshd_users'

class Ptdetails(models.Model):

    # URL def for object - where to return to after add/update
    @models.permalink
    def get_absolute_url(self):
#        return "/ptdtls/%i/" %self.id
#        return ("/ptdtls/%i/", [str(self.id)])
        return ('ptdtls_edit', [str(self.id)])

    # Define choices based on codetable entries
    # Code Status Choices
    cstatchoices = Codetbl.get_code_choices('CODESTATUS')
    # Condition Present At Admission
    cpaachoices = Codetbl.get_code_choices('CPAATYPE')
    # Code Type Choices (Diag/Pcode/Ecode)
    ctypechoices = Codetbl.get_code_choices('CODETYPE')

    id = models.IntegerField(primary_key=True)
    studyid = models.IntegerField(null=True, db_column=u'StudyId', blank=True)
    codetype = models.CharField(choices= ctypechoices, max_length=12, db_column=u'CodeType', blank=True)
    codevalue = models.CharField(max_length=12, db_column=u'CodeValue', blank=True)
    codestatus = models.CharField(choices= cstatchoices, max_length=12, db_column=u'CodeStatus', blank=True, verbose_name='Principal/Other')
    diagcodeicd9 = models.CharField(max_length=12, db_column=u'DiagCodeICD9', blank=True, verbose_name='ICD9 Code')
    icd9codedscr = models.CharField(max_length=255, db_column=u'ICD9CodeDscr', blank=True, verbose_name='ICD9 Description')
    diagcpaa = models.CharField(choices= cpaachoices, max_length=12, db_column=u'DiagCPAA', blank=True, verbose_name='Condition Present at Admission')
    proccodeicd9 = models.CharField(max_length=12, db_column=u'ProcCodeICD9', blank=True)
    procdate = models.DateTimeField(null=True, db_column=u'ProcDate', blank=True)
    ecodeicd9 = models.CharField(max_length=12, db_column=u'ECodeICD9', blank=True)
    datacomplete = models.CharField(max_length=12, db_column=u'DataComplete', blank=True)
    memo = models.CharField(max_length=255, db_column=u'Memo', blank=True)
    diagdatacomplete = models.CharField(max_length=12, db_column=u'DiagDataComplete', blank=True)
    physiciannote = models.SmallIntegerField(null=True, db_column=u'PhysicianNote', blank=True)
    physiciannotedate = models.DateTimeField(null=True, db_column=u'PhysicianNoteDate', blank=True)
    nursenote = models.SmallIntegerField(null=True, db_column=u'NurseNote', blank=True)
    nursenotedate = models.DateTimeField(null=True, db_column=u'NurseNoteDate', blank=True)
    otherhpnote = models.SmallIntegerField(null=True, db_column=u'OtherHPNote', blank=True)
    otherhpnotedate = models.DateTimeField(null=True, db_column=u'OtherHPNoteDate', blank=True)
    paramedicnote = models.SmallIntegerField(null=True, db_column=u'ParamedicNote', blank=True)
    paramedicnotedate = models.DateTimeField(null=True, db_column=u'ParamedicNoteDate', blank=True)
    othernote = models.SmallIntegerField(null=True, db_column=u'OtherNote', blank=True)
    othernotedate = models.DateTimeField(null=True, db_column=u'OtherNoteDate', blank=True)
    poaukncode = models.CharField(max_length=12, db_column=u'POAUknCode', blank=True)
    createdate = models.DateTimeField(null=True, db_column=u'CreateDate', blank=True)
    createuid = models.CharField(max_length=12, db_column=u'CreateUID', blank=True)
    modifydate = models.DateTimeField(null=True, db_column=u'ModifyDate', blank=True)
    modifyuid = models.CharField(max_length=12, db_column=u'ModifyUID', blank=True)
    class Meta:
        db_table = u'ptdetails'

class Ptdiagnoses(models.Model):
    id = models.IntegerField(primary_key=True)
    studyid = models.IntegerField(null=True, db_column=u'StudyID', blank=True)
    diagseq = models.SmallIntegerField(null=True, db_column=u'DiagSeq', blank=True)
    diagtype = models.CharField(max_length=12, db_column=u'DiagType', blank=True)
    diagcodeicd9oshpd = models.CharField(max_length=12, db_column=u'DiagCodeICD9OSHPD', blank=True)
    diagcodeicd9 = models.CharField(max_length=12, db_column=u'DiagCodeICD9', blank=True)
    diagcodeicd9dscr = models.CharField(max_length=255, db_column=u'DiagCodeICD9Dscr', blank=True)
    diagcrct = models.CharField(max_length=12, db_column=u'Diagcrct', blank=True)
    cpaa = models.CharField(max_length=12, blank=True)
    cpaacategory = models.CharField(max_length=12, db_column=u'cpaaCategory', blank=True)
    cpaatype = models.CharField(max_length=12, db_column=u'cpaaType', blank=True)
    cpaatypeunc = models.SmallIntegerField(null=True, db_column=u'cpaaTypeUnc', blank=True)
    diagsrc = models.CharField(max_length=12, blank=True)
    diagdoc = models.CharField(max_length=12, blank=True)
    diagdate = models.DateTimeField(null=True, blank=True)
    cpoa_oshpd = models.CharField(max_length=2, db_column=u'cpoa_OSHPD', blank=True)
    diagdatacomplete = models.CharField(max_length=12, db_column=u'DiagDataComplete', blank=True)
    physiciannote = models.SmallIntegerField(null=True, db_column=u'PhysicianNote', blank=True)
    physiciannotedate = models.DateTimeField(null=True, db_column=u'PhysicianNoteDate', blank=True)
    nursenote = models.SmallIntegerField(null=True, db_column=u'NurseNote', blank=True)
    nursenotedate = models.DateTimeField(null=True, db_column=u'NurseNoteDate', blank=True)
    otherhpnote = models.SmallIntegerField(null=True, db_column=u'OtherHPNote', blank=True)
    otherhpnotedate = models.DateTimeField(null=True, db_column=u'OtherHPNoteDate', blank=True)
    labvaluenote = models.SmallIntegerField(null=True, db_column=u'LabValueNote', blank=True)
    labvaluenotedate = models.DateTimeField(null=True, db_column=u'LabValueNoteDate', blank=True)
    imagingnote = models.SmallIntegerField(null=True, db_column=u'ImagingNote', blank=True)
    imagingnotedate = models.DateTimeField(null=True, db_column=u'ImagingNoteDate', blank=True)
    othernote = models.SmallIntegerField(null=True, db_column=u'OtherNote', blank=True)
    othernotedate = models.DateTimeField(null=True, db_column=u'OtherNoteDate', blank=True)
    memo = models.CharField(max_length=255, db_column=u'Memo', blank=True)
    createdate = models.DateTimeField(null=True, db_column=u'CreateDate', blank=True)
    createuid = models.CharField(max_length=12, db_column=u'CreateUID', blank=True)
    modifydate = models.DateTimeField(null=True, db_column=u'ModifyDate', blank=True)
    modifyuid = models.CharField(max_length=12, db_column=u'ModifyUID', blank=True)
    class Meta:
        db_table = u'ptdiagnoses'

class Ptexclusions(models.Model):
    id = models.IntegerField(primary_key=True)
    los = models.SmallIntegerField(null=True, blank=True)
    preg = models.CharField(max_length=12, blank=True)
    transinjry = models.CharField(max_length=12, blank=True)
    orgn = models.CharField(max_length=12, blank=True)
    hiv = models.CharField(max_length=12, blank=True)
    cf = models.CharField(max_length=12, blank=True)
    tb = models.CharField(max_length=12, blank=True)
    postop = models.SmallIntegerField(null=True, blank=True)
    cand = models.SmallIntegerField(null=True, blank=True)
    cocc = models.SmallIntegerField(null=True, blank=True)
    histo = models.SmallIntegerField(null=True, blank=True)
    aspg = models.SmallIntegerField(null=True, blank=True)
    mycs = models.SmallIntegerField(null=True, blank=True)
    carin = models.SmallIntegerField(null=True, blank=True)
    cyto = models.SmallIntegerField(null=True, blank=True)
    whp = models.SmallIntegerField(null=True, blank=True)
    anrx = models.SmallIntegerField(null=True, blank=True)
    othid = models.SmallIntegerField(null=True, blank=True)
    ornith = models.SmallIntegerField(null=True, blank=True)
    act = models.SmallIntegerField(null=True, blank=True)
    meas = models.SmallIntegerField(null=True, blank=True)
    sal = models.SmallIntegerField(null=True, blank=True)
    tox = models.SmallIntegerField(null=True, blank=True)
    tul = models.SmallIntegerField(null=True, blank=True)
    var = models.SmallIntegerField(null=True, blank=True)
    createdate = models.DateTimeField(null=True, db_column=u'CreateDate', blank=True)
    createuid = models.CharField(max_length=12, db_column=u'CreateUID', blank=True)
    modifydate = models.DateTimeField(null=True, db_column=u'ModifyDate', blank=True)
    modifyuid = models.CharField(max_length=12, db_column=u'ModifyUID', blank=True)
    class Meta:
        db_table = u'ptexclusions'

class Ptmaster(models.Model):

    # define choice lists here for all lookup values (from lookup table)
    # create helper method to extract/create list
    
 #   def __init__(self,*args, **kwargs):
        # build dd lists
#        super(Ptmaster,self).__init__(*args, **kwargs)
        #admsrcchoices = getchoices('ADMSOURCE')
     
    
#    def getchoices(codetype):
#        
#        clist = []
#        clist =( Codetbl.objects.filter(codetype=codetype).order_by('dspseq'))
#            
#        ec  = []    # entity choices
#        for i in range(len(clist)):
#            x = (clist[i].codeval, clist[i].codedscr)
#            ec.append(x)
#        choices = tuple(ec)
#        return choices        
#            
    # Yes/No/Missing
    ynmchoices = Codetbl.get_code_choices('YESNOMISS')
        
    # Yes/No/Missing
    #ynchoices = getchoices('YESNO')
    ynchoices = Codetbl.get_code_choices('YESNO')
    
    #ynchoices= (('M', 'Male'),('F', 'Female'), ('U', 'Ukn'))
      
    # Admission Source
    admsrcchoices =  Codetbl.get_code_choices('ADMSOURCE')
    
    # License Source
    lictypechoices =  Codetbl.get_code_choices('LICENSETYPE')

    # Discharge Disposition Destination Choices   
    dispchoices =  Codetbl.get_code_choices('DISPOSITION')
    
    # Abstraction Status
    abschoices =  Codetbl.get_code_choices('ABSTATUS')
    
    # Ehtnicity Choices
    ethchoices = Codetbl.get_code_choices('ETHNCTY') 

    # Crosswalk Choices
    xwalkchoices =  Codetbl.get_code_choices('CROSSWALK') 
    
    # Admission Type Choices   
    admtypechoices =  Codetbl.get_code_choices('ADMTYPE')
    
    sexchoices= Codetbl.get_code_choices('SEX')
                
    id = models.IntegerField(primary_key=True)
    hospid = models.CharField(max_length=20, blank=True, verbose_name='Hospital ID')
    hospname = models.CharField(max_length=50, blank=True, verbose_name='Hospital Name')
    ssncrct = models.CharField( choices= ynchoices, max_length=12, blank=True, verbose_name='SSN Correct')
    bthdate = models.DateTimeField(null=True, blank=True, verbose_name='Date of Birth')
    bthdatecrct = models.CharField( choices= ynchoices, max_length=12, blank=True, verbose_name='DOB Correct')
    ursamp = models.CharField(max_length=12, blank=True)
    absstatus = models.CharField(choices= abschoices, max_length=12, blank=True, verbose_name='Abstraction Status')
    start = models.DateTimeField(null=True, blank=True)
    absdate = models.DateTimeField(null=True, blank=True)
    absid = models.IntegerField(null=True, blank=True)
    typcare = models.CharField(max_length=50, blank=True)
    oshpdid = models.IntegerField(null=True, blank=True)
    ageyrsa = models.CharField(max_length=50, blank=True)
    sex = models.CharField(choices=sexchoices, max_length=50, blank=True)
    ethncty = models.CharField( choices=ethchoices, max_length=50, verbose_name='Ethnicity')
    racewht = models.BooleanField(verbose_name='White')
    raceblk = models.BooleanField(verbose_name='Black')
    racena = models.BooleanField(verbose_name='Native American/Eskimo')
    raceapi = models.BooleanField(verbose_name='Asian/Pacific Islander')
    raceoth = models.BooleanField(verbose_name='Other')
    raceunk = models.BooleanField(verbose_name='Unknown')
    englishlang = models.CharField(max_length=12, blank=True)
    lang = models.CharField(max_length=12, blank=True)
    intrp = models.CharField(max_length=50, blank=True)
    intrptype = models.CharField(max_length=50, blank=True)
    patzip = models.CharField(max_length=5, blank=True)
    abstrec = models.CharField(max_length=12, blank=True, verbose_name='MRN')
    admtdate = models.DateTimeField(null=True, blank=True, verbose_name='Admission Date')
    absadmtdate = models.DateTimeField(null=True, blank=True)
    admtdatecrct = models.CharField(max_length=50, blank=True)
    admttime = models.DateTimeField(null=True, blank=True)
    admsource = models.CharField(choices=admsrcchoices, max_length=12, blank=True, verbose_name='Admission Source')
    source2 = models.CharField(choices=lictypechoices, max_length=50, blank=True, verbose_name='Licensing Site for Patient')
    source3 = models.CharField(max_length=50, blank=True, verbose_name='Admision via ER')
    admtype = models.CharField(choices=admtypechoices, max_length=50, blank=True, verbose_name='Admission Type')
    stop = models.CharField(max_length=50, blank=True)
    miss = models.CharField(max_length=50, blank=True)
    ilgble = models.CharField(max_length=50, blank=True)
    dnrad = models.CharField(choices=ynchoices, max_length=50, blank=True, verbose_name='DNR order at Admission')
    dnrdis = models.CharField(max_length=50, blank=True)
    dnrdate = models.DateTimeField(null=True, blank=True)
    dnrtime = models.DateTimeField(null=True, blank=True)
    dnrfam = models.CharField(max_length=50, blank=True)
    dnrout = models.CharField(max_length=50, blank=True)
    dschdate = models.DateTimeField(null=True, blank=True, verbose_name='Discharge Date')
    absdschdate = models.DateTimeField(null=True, blank=True)
    dschdatecrct = models.CharField(max_length=50, blank=True)
    dschtime = models.DateTimeField(null=True, blank=True)
    disp = models.CharField(choices= dispchoices, max_length=12, blank=True, verbose_name='Destination on Discharge')
    dthdate = models.DateTimeField(null=True, blank=True)
    memo = models.CharField(max_length=255, blank=True)
    amicase = models.SmallIntegerField(null=True, blank=True)
    capcase = models.SmallIntegerField(null=True, blank=True)
    chfcase = models.SmallIntegerField(null=True, blank=True)
    hipcase = models.SmallIntegerField(null=True, blank=True)
    ptcacase = models.SmallIntegerField(null=True, blank=True)
    ecd849 = models.SmallIntegerField(null=True, blank=True)
    crosswalk = models.CharField(choices=ynchoices, max_length=12, verbose_name='Crosswalk')
    hospracecode = models.CharField(max_length=50, blank=True, verbose_name='Hospital Race Code')
    #srcpapermr = models.SmallIntegerField(null=True, blank=True, widget=forms.Checkboxinput)
    #srcpapermr = models.SmallIntegerField(null=True, blank=True, verbose_name='Paper MR')
    srcpapermr = models.BooleanField(verbose_name='Paper MR')
    srcemr = models.BooleanField( verbose_name='Electronic MR')
    srcmicrofiche = models.BooleanField(verbose_name='Microfiche')
    srcscanned = models.BooleanField(verbose_name='Scanned')
    createdate = models.DateTimeField(null=True, blank=True)
    createuser = models.CharField(max_length=20, blank=True)
    modifydate = models.DateTimeField(null=True, blank=True)
    modifyuser = models.CharField(max_length=20, blank=True)
    ssn = models.CharField(max_length=9, blank=True, verbose_name='Patient SSN')
    class Meta:
        db_table = u'ptmaster'

class Zlkpcode(models.Model):
    id = models.IntegerField(primary_key=True)
    codedispseq = models.SmallIntegerField(null=True, db_column=u'CodeDispSeq', blank=True)
    codetype = models.CharField(max_length=12, db_column=u'CodeType', blank=True)
    codesubtype = models.CharField(max_length=12, db_column=u'CodeSubType', blank=True)
    codeval = models.CharField(max_length=12, db_column=u'CodeVal', blank=True)
    codedscr = models.CharField(max_length=80, db_column=u'CodeDscr', blank=True)
    active = models.SmallIntegerField(db_column=u'Active')
    class Meta:
        db_table = u'zlkpcode'

class Zlogupdates(models.Model):
    id = models.IntegerField(primary_key=True)
    patientid = models.IntegerField(null=True, db_column=u'PatientID', blank=True)
    updatetype = models.CharField(max_length=1, db_column=u'UpdateType', blank=True)
    tablename = models.CharField(max_length=12, db_column=u'TableName', blank=True)
    tablerecid = models.IntegerField(null=True, db_column=u'TableRecID', blank=True)
    uid = models.CharField(max_length=12, db_column=u'UID', blank=True)
    updatedate = models.DateTimeField(null=True, db_column=u'UpdateDate', blank=True)
    class Meta:
        db_table = u'zlogupdates'
        

# Pt Diagnosis Model - has 12many rel with PtMaster        
class Ptdx(models.Model):
    ptmaster = models.ForeignKey('ptmaster')
    id = models.IntegerField(primary_key=True)
    studyid = models.IntegerField(null=True,  blank=True)
    dxseq = models.SmallIntegerField(null=True,  blank=True)
    codetype = models.CharField(max_length=12,  blank=True)
    codestatus = models.CharField(max_length=12,  blank=True)
    diagcodeicd9 = models.CharField(max_length=12,  blank=False)
    icd9codedscr = models.CharField(max_length=255,  blank=False)
    diagcpaa = models.CharField(max_length=30,  blank=True)
    memo = models.CharField(max_length=255, db_column=u'Memo', blank=False)
    createdate = models.DateTimeField(null=True, blank=True)
    createuser = models.CharField(max_length=20, blank=True)
    modifydate = models.DateTimeField(null=True, blank=True)
    modifyuser = models.CharField(max_length=20, blank=True)
        
    class Meta:
        db_table = u'ptdx'

# Dx Test Class - to test auto complete 
class Dxtst(models.Model):
    id = models.IntegerField(primary_key=True)
    icd9code = models.CharField(max_length=12, blank=True)
    icd9dscr = models.CharField(max_length=255, blank=True)
    class Meta:
        db_table = u'dxtst'


        


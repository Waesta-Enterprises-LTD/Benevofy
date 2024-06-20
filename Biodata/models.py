from django.db import models

class Biodata(models.Model):
    member = models.OneToOneField('Members.Member', on_delete=models.CASCADE, related_name='biodata_member')
    date_of_birth = models.DateField(null=True, blank=True)
    address = models.CharField(max_length=100, null=True, blank=True)
    dependents = models.ManyToManyField('Dependent', related_name='biodata_dependents', blank=True)
    marital_status = models.CharField(max_length=100, choices=[('Single', 'Single'), ('Married', 'Married'), ('Divorced', 'Divorced')], null=True, blank=True)
    nationality = models.CharField(max_length=100, null=True, blank=True)
    company_or_business = models.CharField(max_length=100, null=True, blank=True)
    work_address = models.CharField(max_length=100, null=True, blank=True)
    job_title = models.CharField(max_length=100, null=True, blank=True)
    work_contact = models.CharField(max_length=100, null=True, blank=True)
    employment_status = models.CharField(max_length=100, choices=[('Employed', 'Employed'), ('Unemployed', 'Unemployed'), ('Self-Employed', 'Self-Employed')], null=True, blank=True)
    next_of_kin = models.CharField(max_length=100, null=True, blank=True)
    next_of_kin_address = models.CharField(max_length=100, null=True, blank=True)
    next_of_kin_contact = models.CharField(max_length=100, null=True, blank=True)



class Dependent(models.Model):
    first_name = models.CharField(max_length=100, null=True, blank=True)
    last_name = models.CharField(max_length=100, null=True, blank=True)
    date_of_birth = models.DateField(null=True, blank=True)
    gender = models.CharField(max_length=100, choices=[('Male', 'Male'), ('Female', 'Female')], null=True, blank=True)
    picture = models.ImageField(upload_to='Biodata/dependents', null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    phone = models.CharField(max_length=100, null=True, blank=True)
    dependent_to = models.ForeignKey('Members.Member', on_delete=models.CASCADE, related_name='dependent_to')
    biodata = models.ForeignKey('Biodata', on_delete=models.CASCADE)
    relationship = models.CharField(max_length=100, choices=[('Spouse', 'Spouse'), ('Child', 'Child'), ('Sibling', 'Sibling'), ('Parent', 'Parent'), ('Parent-in-law', 'Parent-in-law')], null=True, blank=True)



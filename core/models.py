from django.db import models

# from django.db.models.signals import post_save
# from django.contrib.auth.models import Group

# Create your models here.

# from django.contrib.auth import get_user_model
# User = get_user_model()

from users_app.models import NewUser



class EnquiriesModel(models.Model):
    First_Name =models.CharField(max_length=250)
    Last_Name = models.CharField(max_length =250)
    Email = models.EmailField(max_length =250)
    Subject = models.CharField(max_length =500)
    message_text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"  {self.First_Name}  {self.Last_Name} {self.Subject}"  



class ComplaintsModel(models.Model):
    First_Name =models.CharField(max_length=250)
    Last_Name = models.CharField(max_length =250)
    Email = models.EmailField(max_length =250)
    Subject = models.CharField(max_length =500)
    message_text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"  {self.First_Name}  {self.Last_Name} {self.Subject}"



class Missing_personsModel(models.Model):
    Name =models.CharField(max_length=250)
    Location = models.CharField(max_length =250)
    State_location = models.CharField(max_length =250)
    Email = models.EmailField(max_length =250)
    Subject = models.CharField(max_length =500)
    reporter_name = models.CharField(max_length =500)
    Other_information = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"  {self.reporter_name} =>> {self.Name} =>> {self.Subject}"



gender =(
    ('male','Male'),
    ('female','Female')
)

STATUS = (
			('Pending', 'Pending'),
			('active', 'active'),
			('found', 'found'),
			)

class REALMissing(models.Model):
    # user = models.OneToOneField(User, on_delete=models.CASCADE )# null=True, blank=True,
    user = models.CharField(max_length=250)
    missing_firstname = models.CharField(max_length=250)
    
    missing_lastname = models.CharField(max_length = 250)
    missing_other_name = models.CharField(max_length=250, null=True, blank=True)
    missing_AKA = models.CharField(max_length=250, null=True, blank=True)
    missing_sex=models.CharField(max_length=10,choices=gender,blank=True,)
    missing_Age = models.CharField(max_length=240)
    missing_hight = models.CharField(max_length=300)
    missing_date = models.DateField()
    missing_image = models.ImageField(upload_to="missing_profile", blank=True,  null=True,)

    # lastKnowLocatomn
    Last_Address = models.CharField(max_length=1000)
    Last_Area = models.CharField(max_length=1000)
    Last_State = models.CharField(max_length=50)#choices= states)
    Last_city = models.CharField(max_length=50)

    # contact person
    ContactName = models.CharField(max_length=250)
    ContactPhone = models.CharField(max_length=250)
    ContactEmail = models.EmailField(max_length=250)
    ContactAddress = models.CharField(max_length = 500)
    status = models.CharField(max_length=200, null=True, choices=STATUS, default="Pending")

    def __str__(self):
        return self.user.username

    




# # class test(models.Model):

# #     missing_date = models.DateField(blank=True ,null=True)






# class UserProfile(models.Model):
#     user = models.OneToOneField(NewUser, on_delete=models.CASCADE related_name="user_profile")

#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)
    

#     def __str__(self):
#         return self.user


# def post_user_created_signal(sender, instance, created, **kwargs):
#     if created:
#         # group  = Group.objects.get(name='User')
#         # instance.groups.add(group)
#         UserProfile.objects.create(user=instance)


# post_save.connect(post_user_created_signal, sender=CustomUser)


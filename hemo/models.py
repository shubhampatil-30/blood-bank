from django.db import models

# Create your models here.
class user(models.Model):
    name= models.CharField(max_length=50)
    age = models.BigIntegerField()
    gender = (('Male','male'),('Female','female'),('Other','other'))
    gender = models.CharField(max_length=20, choices=gender)
    phoneno= models.BigIntegerField()
    address = models.TextField(max_length=200)
    state = (
        ('Andhra Pradesh', 'Andhra Pradesh'),
        ('Arunachal Pradesh', 'Arunachal Pradesh'),
        ('Assam', 'Assam'),
        ('Bihar', 'Bihar'),
        ('Chhattisgarh', 'Chhattisgarh'),
        ('Goa', 'Goa'),
        ('Gujarat', 'Gujarat'),
        ('Haryana', 'Haryana'),
        ('Himachal Pradesh', 'Himachal Pradesh'),
        ('Jharkhand', 'Jharkhand'),
        ('Karnataka', 'Karnataka'),
        ('Kerala', 'Kerala'),
        ('Madhya Pradesh', 'Madhya Pradesh'),
        ('Maharashtra', 'Maharashtra'),
        ('Manipur', 'Manipur'),
        ('Meghalaya', 'Meghalaya'),
        ('Mizoram', 'Mizoram'),
        ('Nagaland', 'Nagaland'),
        ('Odisha', 'Odisha'),
        ('Punjab', 'Punjab'),
        ('Rajasthan', 'Rajasthan'),
        ('Sikkim', 'Sikkim'),
        ('Tamil Nadu', 'Tamil Nadu'),
        ('Telangana', 'Telangana'),
        ('Tripura', 'Tripura'),
        ('Uttar Pradesh', 'Uttar Pradesh'),
        ('Uttarakhand', 'Uttarakhand'),
        ('West Bengal', 'West Bengal'),
        ('Andaman and Nicobar Islands', 'Andaman and Nicobar Islands'),
        ('Chandigarh', 'Chandigarh'),
        ('Dadra and Nagar Haveli and Daman and Diu', 'Dadra and Nagar Haveli and Daman and Diu'),
        ('Delhi', 'Delhi'),
        ('Lakshadweep', 'Lakshadweep'),
        ('Puducherry', 'Puducherry'),
        ('Ladakh', 'Ladakh'),
        ('Jammu and Kashmir', 'Jammu and Kashmir'),
    )
    state = models.CharField(max_length=100, choices=state)
    district= models.CharField(max_length=50)
    pincode = models.BigIntegerField()
    email = models.EmailField()
    password = models.CharField(max_length=100)

    class Meta:
        db_table= 'user'

class donor(models.Model):
    name= models.CharField(max_length=100)
    img=models.ImageField(upload_to='media')
    age = models.BigIntegerField()
    gender = (('Male','male'),('Female','female'),('Other','other'))
    gender = models.CharField(max_length=20, choices=gender)
    bloodgroup = [
        ('A+', 'A+'),
        ('A-', 'A-'),
        ('B+', 'B+'),
        ('B-', 'B-'),
        ('AB+', 'AB+'),
        ('AB-', 'AB-'),
        ('O+', 'O+'),
        ('O-', 'O-'),
    ]
    bloodgroup= models.CharField(max_length=5,choices=bloodgroup)
    address = models.TextField(max_length=200)
    phoneno= models.BigIntegerField()
    state = (
        ('Andhra Pradesh', 'Andhra Pradesh'),
        ('Arunachal Pradesh', 'Arunachal Pradesh'),
        ('Assam', 'Assam'),
        ('Bihar', 'Bihar'),
        ('Chhattisgarh', 'Chhattisgarh'),
        ('Goa', 'Goa'),
        ('Gujarat', 'Gujarat'),
        ('Haryana', 'Haryana'),
        ('Himachal Pradesh', 'Himachal Pradesh'),
        ('Jharkhand', 'Jharkhand'),
        ('Karnataka', 'Karnataka'),
        ('Kerala', 'Kerala'),
        ('Madhya Pradesh', 'Madhya Pradesh'),
        ('Maharashtra', 'Maharashtra'),
        ('Manipur', 'Manipur'),
        ('Meghalaya', 'Meghalaya'),
        ('Mizoram', 'Mizoram'),
        ('Nagaland', 'Nagaland'),
        ('Odisha', 'Odisha'),
        ('Punjab', 'Punjab'),
        ('Rajasthan', 'Rajasthan'),
        ('Sikkim', 'Sikkim'),
        ('Tamil Nadu', 'Tamil Nadu'),
        ('Telangana', 'Telangana'),
        ('Tripura', 'Tripura'),
        ('Uttar Pradesh', 'Uttar Pradesh'),
        ('Uttarakhand', 'Uttarakhand'),
        ('West Bengal', 'West Bengal'),
        ('Andaman and Nicobar Islands', 'Andaman and Nicobar Islands'),
        ('Chandigarh', 'Chandigarh'),
        ('Dadra and Nagar Haveli and Daman and Diu', 'Dadra and Nagar Haveli and Daman and Diu'),
        ('Delhi', 'Delhi'),
        ('Lakshadweep', 'Lakshadweep'),
        ('Puducherry', 'Puducherry'),
        ('Ladakh', 'Ladakh'),
        ('Jammu and Kashmir', 'Jammu and Kashmir'),
    )
    state = models.CharField(max_length=100, choices=state)
    city= models.CharField(max_length=50)
    password = models.CharField(max_length=200)

    class Meta:
        db_table='donor'

class bank(models.Model):
    name= models.CharField(max_length=100)
    phoneno= models.BigIntegerField()
    address = models.TextField(max_length=200)
    state = (
        ('Andhra Pradesh', 'Andhra Pradesh'),
        ('Arunachal Pradesh', 'Arunachal Pradesh'),
        ('Assam', 'Assam'),
        ('Bihar', 'Bihar'),
        ('Chhattisgarh', 'Chhattisgarh'),
        ('Goa', 'Goa'),
        ('Gujarat', 'Gujarat'),
        ('Haryana', 'Haryana'),
        ('Himachal Pradesh', 'Himachal Pradesh'),
        ('Jharkhand', 'Jharkhand'),
        ('Karnataka', 'Karnataka'),
        ('Kerala', 'Kerala'),
        ('Madhya Pradesh', 'Madhya Pradesh'),
        ('Maharashtra', 'Maharashtra'),
        ('Manipur', 'Manipur'),
        ('Meghalaya', 'Meghalaya'),
        ('Mizoram', 'Mizoram'),
        ('Nagaland', 'Nagaland'),
        ('Odisha', 'Odisha'),
        ('Punjab', 'Punjab'),
        ('Rajasthan', 'Rajasthan'),
        ('Sikkim', 'Sikkim'),
        ('Tamil Nadu', 'Tamil Nadu'),
        ('Telangana', 'Telangana'),
        ('Tripura', 'Tripura'),
        ('Uttar Pradesh', 'Uttar Pradesh'),
        ('Uttarakhand', 'Uttarakhand'),
        ('West Bengal', 'West Bengal'),
        ('Andaman and Nicobar Islands', 'Andaman and Nicobar Islands'),
        ('Chandigarh', 'Chandigarh'),
        ('Dadra and Nagar Haveli and Daman and Diu', 'Dadra and Nagar Haveli and Daman and Diu'),
        ('Delhi', 'Delhi'),
        ('Lakshadweep', 'Lakshadweep'),
        ('Puducherry', 'Puducherry'),
        ('Ladakh', 'Ladakh'),
        ('Jammu and Kashmir', 'Jammu and Kashmir'),
    )
    state = models.CharField(max_length=100, choices=state)
    city= models.CharField(max_length=50)
    username=models.CharField(max_length=50)
    password=models.CharField(max_length=200)

    class Meta:
        db_table='bank'

class blooddonate(models.Model):
    donorid=models.ForeignKey(donor,on_delete=models.CASCADE)
    bankid=models.ForeignKey(bank,on_delete=models.CASCADE)
    age=models.IntegerField()
    disease=models.TextField(max_length=200)
    unit=models.BigIntegerField()
    status=models.CharField(max_length=20)
    date=models.DateField(auto_now_add=True)

    class Meta:
        db_table='blooddonate'

class recipient(models.Model):
    name= models.CharField(max_length=100)
    img=models.ImageField(upload_to='media')
    age = models.BigIntegerField()
    gender = (('Male','male'),('Female','female'),('Other','other'))
    gender = models.CharField(max_length=20, choices=gender)
    bloodgroup = [
        ('A+', 'A+'),
        ('A-', 'A-'),
        ('B+', 'B+'),
        ('B-', 'B-'),
        ('AB+', 'AB+'),
        ('AB-', 'AB-'),
        ('O+', 'O+'),
        ('O-', 'O-'),
    ]
    bloodgroup= models.CharField(max_length=5,choices=bloodgroup)
    address = models.TextField(max_length=200)
    phoneno= models.BigIntegerField()
    state = (
        ('Andhra Pradesh', 'Andhra Pradesh'),
        ('Arunachal Pradesh', 'Arunachal Pradesh'),
        ('Assam', 'Assam'),
        ('Bihar', 'Bihar'),
        ('Chhattisgarh', 'Chhattisgarh'),
        ('Goa', 'Goa'),
        ('Gujarat', 'Gujarat'),
        ('Haryana', 'Haryana'),
        ('Himachal Pradesh', 'Himachal Pradesh'),
        ('Jharkhand', 'Jharkhand'),
        ('Karnataka', 'Karnataka'),
        ('Kerala', 'Kerala'),
        ('Madhya Pradesh', 'Madhya Pradesh'),
        ('Maharashtra', 'Maharashtra'),
        ('Manipur', 'Manipur'),
        ('Meghalaya', 'Meghalaya'),
        ('Mizoram', 'Mizoram'),
        ('Nagaland', 'Nagaland'),
        ('Odisha', 'Odisha'),
        ('Punjab', 'Punjab'),
        ('Rajasthan', 'Rajasthan'),
        ('Sikkim', 'Sikkim'),
        ('Tamil Nadu', 'Tamil Nadu'),
        ('Telangana', 'Telangana'),
        ('Tripura', 'Tripura'),
        ('Uttar Pradesh', 'Uttar Pradesh'),
        ('Uttarakhand', 'Uttarakhand'),
        ('West Bengal', 'West Bengal'),
        ('Andaman and Nicobar Islands', 'Andaman and Nicobar Islands'),
        ('Chandigarh', 'Chandigarh'),
        ('Dadra and Nagar Haveli and Daman and Diu', 'Dadra and Nagar Haveli and Daman and Diu'),
        ('Delhi', 'Delhi'),
        ('Lakshadweep', 'Lakshadweep'),
        ('Puducherry', 'Puducherry'),
        ('Ladakh', 'Ladakh'),
        ('Jammu and Kashmir', 'Jammu and Kashmir'),
    )
    state = models.CharField(max_length=100, choices=state)
    city= models.CharField(max_length=50)
    password = models.CharField(max_length=200)

    class Meta:
        db_table='recipient'

class bloodrequest(models.Model):
    recipientid=models.ForeignKey(recipient,on_delete=models.CASCADE)
    bankid=models.ForeignKey(bank,on_delete=models.CASCADE)
    age=models.IntegerField()
    reason=models.TextField(max_length=500)
    unit=models.BigIntegerField()
    status=models.CharField(max_length=10)
    date=models.DateField(auto_now_add=True)

    class Meta:
        db_table='bloodrequest'


class hospital(models.Model):
    name= models.CharField(max_length=100)
    phoneno= models.BigIntegerField()
    address = models.TextField(max_length=200)
    state = (
        ('Andhra Pradesh', 'Andhra Pradesh'),
        ('Arunachal Pradesh', 'Arunachal Pradesh'),
        ('Assam', 'Assam'),
        ('Bihar', 'Bihar'),
        ('Chhattisgarh', 'Chhattisgarh'),
        ('Goa', 'Goa'),
        ('Gujarat', 'Gujarat'),
        ('Haryana', 'Haryana'),
        ('Himachal Pradesh', 'Himachal Pradesh'),
        ('Jharkhand', 'Jharkhand'),
        ('Karnataka', 'Karnataka'),
        ('Kerala', 'Kerala'),
        ('Madhya Pradesh', 'Madhya Pradesh'),
        ('Maharashtra', 'Maharashtra'),
        ('Manipur', 'Manipur'),
        ('Meghalaya', 'Meghalaya'),
        ('Mizoram', 'Mizoram'),
        ('Nagaland', 'Nagaland'),
        ('Odisha', 'Odisha'),
        ('Punjab', 'Punjab'),
        ('Rajasthan', 'Rajasthan'),
        ('Sikkim', 'Sikkim'),
        ('Tamil Nadu', 'Tamil Nadu'),
        ('Telangana', 'Telangana'),
        ('Tripura', 'Tripura'),
        ('Uttar Pradesh', 'Uttar Pradesh'),
        ('Uttarakhand', 'Uttarakhand'),
        ('West Bengal', 'West Bengal'),
        ('Andaman and Nicobar Islands', 'Andaman and Nicobar Islands'),
        ('Chandigarh', 'Chandigarh'),
        ('Dadra and Nagar Haveli and Daman and Diu', 'Dadra and Nagar Haveli and Daman and Diu'),
        ('Delhi', 'Delhi'),
        ('Lakshadweep', 'Lakshadweep'),
        ('Puducherry', 'Puducherry'),
        ('Ladakh', 'Ladakh'),
        ('Jammu and Kashmir', 'Jammu and Kashmir'),
    )
    state = models.CharField(max_length=100, choices=state)
    city= models.CharField(max_length=50)
    username=models.CharField(max_length=50)
    password=models.CharField(max_length=200)

    class Meta:
        db_table='Hospital'

class stock(models.Model):
    bankid=models.ForeignKey(bank,on_delete=models.CASCADE)
    bloodgroup = [
        ('A+', 'A+'),
        ('A-', 'A-'),
        ('B+', 'B+'),
        ('B-', 'B-'),
        ('AB+', 'AB+'),
        ('AB-', 'AB-'),
        ('O+', 'O+'),
        ('O-', 'O-'),
    ]
    bloodgroup= models.CharField(max_length=5,choices=bloodgroup,default='Empty')
    unit=models.PositiveIntegerField(default=0)
    price=models.BigIntegerField(default=0)

    class Meta:
        db_table='stock'

class cart(models.Model):
    hid=models.ForeignKey(hospital,on_delete=models.CASCADE)
    sid=models.ForeignKey(stock,on_delete=models.CASCADE)
    quantity=models.BigIntegerField()
    total=models.FloatField()

    class Meta:
        db_table='cart'

class order(models.Model):
    ordernumber = models.CharField(max_length=100)
    orderdate = models.DateField()
    name = models.CharField(max_length=50)
    phoneno = models.BigIntegerField()
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=30)
    state = models.CharField(max_length=30)
    pincode = models.BigIntegerField()
    orderstatus = models.CharField(max_length=20)

    class Meta:
        db_table='order'

class payment(models.Model):
    hid = models.ForeignKey(hospital,on_delete=models.CASCADE)
    oid = models.ForeignKey(order,on_delete=models.CASCADE)
    paymentstatus= models.CharField(max_length=20,default='pending')
    transactionid=models.CharField(max_length=200)
    paymentmode=models.CharField(max_length=50,default='Razorpay')

    class Meta:
        db_table='payment'

class orderdetail(models.Model):
    ordernumber=models.CharField(max_length=100)
    hid=models.ForeignKey(hospital,on_delete=models.CASCADE)
    sid=models.ForeignKey(stock,on_delete=models.CASCADE)
    quantity=models.BigIntegerField()
    totalprice=models.BigIntegerField()
    paymentid=models.ForeignKey(payment,on_delete=models.CASCADE)
    created_at=models.DateField(auto_now=True)
    updated_at=models.DateField(auto_now=True)

    class Meta:
        db_table='orderdetail'




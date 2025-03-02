from django.db import models



class Employee(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15, null=True, blank=True)
    role = models.ForeignKey('Role', on_delete=models.SET_NULL, null=True)
    department = models.ForeignKey('Department', on_delete=models.SET_NULL, null=True)
    
    manager = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True, related_name="subordinates")
    
    profile_pic = models.URLField(null=True, blank=True)
    date_joined = models.DateField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)

    class Meta:
        indexes = [
            models.Index(fields=['manager']),  # Speeds up hierarchy queries
            models.Index(fields=['department'])
        ]

    def __str__(self):
        return self.name


class Role(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100, unique=True)
    access_level = models.IntegerField(default=1)  # Higher numbers indicate more access

    def __str__(self):
        return self.title


class Department(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name


class AuditLog(models.Model):
    id = models.AutoField(primary_key=True)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    action = models.CharField(max_length=100)  # "Promoted", "Transferred", "Fired"
    old_manager = models.ForeignKey(Employee, null=True, blank=True, on_delete=models.SET_NULL, related_name="old_manager")
    new_manager = models.ForeignKey(Employee, null=True, blank=True, on_delete=models.SET_NULL, related_name="new_manager")
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.employee.name} - {self.action}"

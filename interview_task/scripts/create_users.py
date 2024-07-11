from blog.models import User

print("start creating users.")
for i in range(2,100):
    
    User.objects.create_user(f"user{i}",password="1234")
    
print("creating users is done.")

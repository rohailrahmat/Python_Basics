password = "rohai"
password_len = len(password)
if len(password) < 6:
    strenght = 'weak'
elif len(password) <= 8:
    strenght = "Medium"
else :
      strenght = "Strong"

print("Your Password is:",strenght)
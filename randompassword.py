import random
import string
def generate_password(lenght=12):
    lower=string.ascii_lowercase
    upper=string.ascii_uppercase
    digits=string.digits

    all_chars=lower+upper+digits
    password=[
        random.choice(lower),
        random.choice(upper),
        random.choice(digits)
    ]
    password +=random.choices(all_chars,k=lenght-3)
    random.shuffle(password)
    return''.join(password)
print("Your random password is:",generate_password())
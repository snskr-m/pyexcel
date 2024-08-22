import pandas as pd
import re

path="C:/Users/Admin/Documents/doctors_spain.xlsx"

df=pd.read_excel(path)

df=df.drop_duplicates()

#name
def to_proper_case(name):
    return name.strip().title()

df['Name']=df['Name'].apply(to_proper_case)

#address
df['Address']=df['Address'].fillna('NA')

#phone
def standardize_phone_number(phone):
    if not phone or pd.isna(phone):
       return 'NA'
    phone=re.sub(r'\D', '', str(phone))
    phone=phone[-9:]
    if len(phone)==9:
        return f'({phone[:3]}) {phone[3:6]}-{phone[6:]}'
    else:
        return f'Invalid Number:{phone}'

df['Contact']=df['Contact'].apply(standardize_phone_number)

#emails
def validate_email(email):
    if not email or pd.isna(email):
       return 'NA'
    email_regex=r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    if re.match(email_regex, str(email)):
        return email
    else:
        return f'Invalid Email:{email}'

df['Email']=df['Email'].apply(validate_email)


df.to_excel('C:/Users/Admin/Documents/doctors_spain_clean.xlsx', index=False)

print(f"{path} cleaned and validated.")

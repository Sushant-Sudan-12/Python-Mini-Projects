import smtplib

my_email = "sushantsudan3075@gmail.com"
my_pass = "sudan3075"
msg = """Subject: Hello

Hello World
"""

with smtplib.SMTP('smtp-mail.outlook.com', 587) as connection:
    connection.starttls()
    connection.login(user = my_email,password = my_pass)
    connection.sendmail(from_addr=my_email,to_addrs="sushantsudan3075@gmail.com",msg = msg)



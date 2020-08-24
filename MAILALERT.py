import smtplib

gmailaddress = "creatorshack2020@gmail.com"
gmailpassword = "adesh0007"


mailto = "creatorshack2020@gmail.com"

msg = "A visually impaired person is sick at coordinates(x,y). Urgent help is required. "

mailServer = smtplib.SMTP('smtp.gmail.com' , 587)

mailServer.starttls()

mailServer.login(gmailaddress , gmailpassword)

mailServer.sendmail(gmailaddress, mailto , msg)

print(" \n Sent!")


mailServer.quit()



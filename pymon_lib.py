#!/usr/bin/python
import datetime

#sendmail 
#This function will be used for sending email notifications
def sendmail(message):
        from smtplib import SMTP

        debuglevel = 0

        smtp = SMTP()
        smtp.set_debuglevel(debuglevel)
        smtp.connect('mail.domain.com', 25)
        smtp.ehlo()
        smtp.starttls()
        smtp.ehlo()
        smtp.login('email@domain.com', 'password')

        from_addr = "Andrea Del Monaco <andrea.delmonaco@technosec.net>"
        to_addr = "dest-email@domain.com"

        subj = "hello"
        date = datetime.datetime.now().strftime( "%d/%m/%Y %H:%M" )

        message_text = "Hello\nThis is a mail from your server\n\nBye\n"

        msg = "From: %s\nTo: %s\nSubject: %s\nDate: %s\n\n%s" % ( from_addr, to_addr, subj, date, message_text )

        smtp.sendmail(from_addr, to_addr, msg)
        smtp.quit()


#get_tempC
#Using this method in order to get the temperature because with this i'll not need root privileges
def get_tempC():
        try:
          tFile = open('/sys/class/thermal/thermal_zone0/temp')
          temp = float(tFile.read())
          tempC = temp/1000
          tempC = round(tempC, 1)

        except:
            tFile.close()
            exit

        return tempC;


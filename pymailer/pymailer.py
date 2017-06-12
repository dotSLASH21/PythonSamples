"""
This is a small and quick E-mail sending Python program which reduces the hassle
to open slow mail client or web browser to send small mails, this program is
developed as a module for use by other programs such as automated notification sender
or Time mail sender, as well as a stand alone program.

Any Error reporting, Suggestions or improvements are welcome at
https://github.com/dotSLASH21/PythonSamples

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NON-INFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE. ;)

"""

__author__ = "Arunangshu Biswas"
__credits__ = ["Arunangshu Biswas"]
__license__ = "GPL"
__version__ = "alpha"
__maintainer__ = "Arunangshu Biswas"
__email__ = "arunangshubsws@gmail.com"
__status__ = "Developmental"
__date__ = "12-06-2017"

import smtplib
import sys
import re
import os
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


def get_config(mail_service):
    
    '''
    I wanted the program to read from the file 'smtpConfig.txt' which stored the configurations, but I commented out
    those lines because I want you to run the program without any hassle and any dependency issues.
    '''
    
    #file = open("smtpConfig.txt", "r")
    #lines = file.read().split('\n')
    lines = ['Gmail|smtp.gmail.com:587', 'Yahoo|smtp.mail.yahoo.com:465', 'Outlook|smtp.live.com:587']
    for line in lines:
        index = line.find('|')
        if line[0:index].lower() == mail_service.lower():
            return line[(index+1):]
        
    print('Specified Mail service Provider not found! Manually enter Settings...')
    return input('Enter SMTP server with port number (e.g. smtp.example.com:587): ')


def validate_email(email):
    pattern = r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)"
    match = re.search(pattern, email)
    if match:
        return True
    else:
        return False


def send_mail(domain, port_num, uname, pswrd, to_address, message):
    server = smtplib.SMTP(domain, port_num)
    
    print('logging in please wait... ', end='')
    server.ehlo()
    server.starttls()
    server.login(uname, pswrd)
    print('Done!')

    print("Sending message please wait...", end="")
    server.sendmail(uname, to_address, message)
    server.quit()
    print("Done! :)")


def main():
    print('================(login Details)====================')
    mail_service = input("Enter your mail server: ")
    while True:
        username = input("Enter your username (e.g. johndoe322@gmail.com): ")
        password = input("Enter your password: ")
        if validate_email(username):
            break
        else:
            print('Invalid E-mail! try again!')
        
    print('===================================================\n')
    
    srvr = get_config(mail_service)
    serverDomain = srvr[0:(srvr.index(':'))]  # Get the domain part
    port = srvr[(srvr.index(':') + 1):len(srvr)]  # Get the port

    print('================(Write Message)====================')
    # Prepare email headers
    while True:
        toaddress = input('Enter recipient: ')
        if validate_email(toaddress):
            break
        else:
            print('Invalid E-mail! try again!')

    msg = MIMEMultipart()
    msg['From'] = username
    msg['To'] = toaddress
    msg['Subject'] = input('Enter subject: ')
    msgBody = input('Enter the e-mail content: ')
    msg.attach(MIMEText(msgBody, 'plain'))
    plain_msg = msg.as_string()
    print('===================================================\n')

    send_mail(serverDomain, port, username, password, toaddress, plain_msg)


if __name__ == "__main__":
    main()

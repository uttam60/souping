import mechanize
from bs4 import BeautifulSoup as bs
import smtplib
from email.message import EmailMessage


agent_dic = {
    'Chrome' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36', 
    'Firefox' : 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:40.0) Gecko/20100101 Firefox/40.1'
    }

def read_url(url, agent_name):

    agent = agent_dic[agent_name]
    br = mechanize.Browser()
    br.set_handle_robots(False)   # ignore robots
    br.set_handle_refresh(False)  # can sometimes hang without this
    br.addheaders = [('User-agent', agent)] 	  
    mc = br.open(url)
    page = mc.read().decode()

    return page

def souping(page):

    soup = bs(page, "html.parser")
    extract = soup.find_all("a", class_="boxAlign-jc--all-c space--h-3 width--all-12 btn btn--mode-primary")
    return True if len(extract) > 0 else False

def email_alerts(sender_email, sender_password, destination_email):

    # create email
    msg = EmailMessage()
    msg['Subject'] = "You have a chance for a PS5 on Dealabs"
    msg['From'] = sender_email
    msg['To'] = destination_email
    msg.set_content("Act quick, there is a PS5 available")

  
    # send email
    with smtplib.SMTP_SSL('smtp.mail.com', 465) as smtp:
        smtp.login(email_address, email_password)
        smtp.send_message(msg)

    return True


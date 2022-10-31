from lib.functions import read_url, souping, email_alerts
from creds import user, pas



url = "https://www.dealabs.com/groupe/playstation-5"
agent = "Chrome"
page = read_url(url, agent)


has_ps5 = souping(page)

if has_ps5 is not True:
    receiver = 'uttam.paila@gmail.com'
    email_alerts(user, pas, receiver)



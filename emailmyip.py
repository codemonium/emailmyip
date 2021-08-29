import os
import requests
from postmarker.core import PostmarkClient

response = requests.get("https://checkip.amazonaws.com")
ip_address = response.text.strip()

postmark = PostmarkClient(server_token=os.environ['POSTMARK_API_KEY'])
postmark.emails.send(
  From=os.environ['FROM'],
  To=os.environ['TO'],
  Subject='Current IP Address',
  HtmlBody=ip_address
)

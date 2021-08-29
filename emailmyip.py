import os

from postmarker.core import PostmarkClient
from urllib import request

req = request.Request("https://checkip.amazonaws.com", data=None)
res = request.urlopen(req, timeout=5)

ip_address = res.read().decode().strip()

postmark = PostmarkClient(server_token=os.environ['POSTMARK_API_KEY'])
postmark.emails.send(
  From=os.environ['FROM'],
  To=os.environ['TO'],
  Subject='Current IP Address',
  HtmlBody=ip_address
)

import dotenv
import os
import requests
from postmarker.core import PostmarkClient

response = requests.get("https://checkip.amazonaws.com")
ip_address = response.text.strip()

dotenv.load_dotenv()

postmark_api_key = os.environ['POSTMARK_API_KEY']
from_email_address = os.environ['FROM_EMAIL_ADDRESS']
to_email_address = os.environ['TO_EMAIL_ADDRESS']

postmark = PostmarkClient(server_token=postmark_api_key)
postmark.emails.send(
  From=from_email_address,
  To=to_email_address,
  Subject='Current IP Address',
  HtmlBody=ip_address
)

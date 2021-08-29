import dotenv
import os
import requests
import sys
from postmarker.core import PostmarkClient


def resource_path(relative_path):
  # https://stackoverflow.com/a/44352931/10183593
  base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
  return os.path.join(base_path, relative_path)


response = requests.get("https://checkip.amazonaws.com")
ip_address = response.text.strip()

dotenv.load_dotenv(dotenv_path=resource_path(".env"))

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

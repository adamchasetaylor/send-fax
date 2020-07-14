import os
from twilio.rest import Client
from dotenv import load_dotenv
load_dotenv()

TWILIO_ACCOUNT_SID = os.getenv('TWILIO_ACCOUNT_SID')
TWILIO_AUTH_TOKEN = os.getenv('TWILIO_AUTH_TOKEN')
FROM_FAX_NUMBER = os.getenv('FROM_FAX_NUMBER')
TO_FAX_NUMBER = os.getenv('TO_FAX_NUMBER')

client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)

fax = client.fax.faxes \
  .create(
    from_=FROM_FAX_NUMBER,
    to=TO_FAX_NUMBER,
    media_url='https://www.twilio.com/docs/documents/25/justthefaxmaam.pdf'
  )

print(fax.sid)
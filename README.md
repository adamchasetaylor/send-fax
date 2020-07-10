# send-fax

Environment variables must be configured in your .env file.

TWILIO_ACCOUNT_SID=

TWILIO_AUTH_TOKEN=

FROM_FAX_NUMBER=

TO_FAX_NUMBER=

## Local Setup

cd send-fax
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

## Run 

./start.sh
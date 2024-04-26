# arquivo com a api do google
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
from django.conf import settings

#carregar token de autorização
def load_credentials():
    
    credentials_path = settings.GOOGLE_API_KEY
    #os.path.join(os.path.dirname(os.path.abspath(__file__)), 'googleapi', 'key.json')
    creds = Credentials.from_authorized_user_file(credentials_path)
    return creds

def get_form_responses():
    creds = load_credentials()
    service = build('sheets', 'v4', credentials=creds)
    spreadsheet_id = 'your-spreadsheet-id'
    range_name = 'Form Responses!A2:E'
    result = service.spreadsheets().values().get(spreadsheetId=spreadsheet_id, range=range_name).execute()
    values = result.get('values', [])
    return values
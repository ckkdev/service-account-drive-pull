from googleapiclient import discovery
from google.oauth2 import service_account

credentials = service_account.Credentials.from_service_account_file('keyfile.json', scopes=['https://www.googleapis.com/auth/drive.metadata.readonly'])
delegated_credentials = credentials.with_subject('dustin@ckk.dev')
service = discovery.build('drive', 'v3', credentials=delegated_credentials)

# Call the Drive v3 API
results = service.files().list(
    pageSize=10, fields="nextPageToken, files(id, name)").execute()
items = results.get('files', [])

if not items:
    print('No files found.')
else:
    print('Files:')
    for item in items:
        print(u'{0} ({1})'.format(item['name'], item['id']))
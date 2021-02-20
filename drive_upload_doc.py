from apiclient.http import MediaFileUpload

def upload(service):
    pdffile = 'test.pdf'
    txtfile = 'sample.txt'

    mime = 'application/vnd.google-apps.document'
    res = service.files().create(
        body={
            'name': pdffile,
            'mimeType': mime
        },
        media_body=MediaFileUpload(pdffile, mimetype=mime, resumable=True)
    ).execute()
    return res

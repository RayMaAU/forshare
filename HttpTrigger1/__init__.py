import logging

import azure.functions as func

from . import demo

import requests

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    url = req.params.get('url')
    if not url:
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            url = req_body.get('url')

    if url:
        response = requests.get('https://' + url)
        return func.HttpResponse(
            response.content, 
            status_code = demo.OK_status_code
        )
    else:
        return func.HttpResponse(
             "This HTTP triggered function executed successfully. Pass a url in the query string or in the request body for a personalized response.",
             status_code = demo.NOT_FOUNT_status_code
        )

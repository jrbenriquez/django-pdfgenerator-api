import hashlib
import hmac

from pdfgenerator_api import settings


def generate_signature(resource):
    api_key = settings.PDFGENERATOR_API_KEY
    workspace = settings.PDFGENERATOR_API_WORKSPACE
    secret = settings.PDFGENERATOR_API_SECRET

    message = '{}{}{}'.format(api_key, resource, workspace)

    signature = hmac.new(
        str.encode(secret),
        msg=str.encode(message),
        digestmod=hashlib.sha256).hexdigest()

    return signature

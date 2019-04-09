from pdfgenerator_api import settings
from pdfgenerator_api.utils import generate_signature
from pdfgenerator_api.resources import METHOD_URLS


def signature_auth(method):
    def _signature_auth(*args, **kwargs):
        if method.__name__ not in METHOD_URLS:
            raise Exception('"resource" not found')
        resource = METHOD_URLS[method.__name__].format(
            template=kwargs.get('template_id', ''))
        headers = {
            'X-Auth-Key': settings.PDFGENERATOR_API_KEY,
            'X-Auth-Workspace': settings.PDFGENERATOR_API_WORKSPACE,
            'X-Auth-Signature': generate_signature(resource),
            'Content-Type': 'application/json; charset=utf-8',
            'Accept': 'application/json'
        }
        return method(headers=headers, resource=resource, *args, **kwargs)

    return _signature_auth


def simple_auth(method):
    def _simple_auth(*args, **kwargs):
        headers = {
            'X-Auth-Key': settings.PDFGENERATOR_API_KEY,
            'X-Auth-Secret': settings.PDFGENERATOR_API_SECRET,
            'X-Auth-Workspace': settings.PDFGENERATOR_API_WORKSPACE,
            'Content-Type': 'application/json; charset=utf-8',
            'Accept': 'application/json'
        }
        return method(headers=headers, *args, **kwargs)

    return _simple_auth


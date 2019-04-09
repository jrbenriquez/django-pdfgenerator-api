import json
import requests
import urllib

from pdfgenerator_api import settings
from pdfgenerator_api.auth import signature_auth

BASE_PATH = settings.PDFGENERATOR_API_BASEPATH

@signature_auth
def view_templates(*args, **kwargs):
    resource_url = kwargs['resource']
    headers = kwargs['headers']

    r = requests.get('{}{}'.format(
        BASE_PATH,
        resource_url), headers=headers)

    response_object = json.loads(r.text)
    
    return response_object['response']
    

@signature_auth
def view_template(*args, **kwargs):
    resource_url = kwargs['resource']
    template_id = kwargs['template_id']
    headers = kwargs['headers']

    r = requests.get('{}{}'.format(
        BASE_PATH,
        resource_url),
        headers=headers)

    response_object = json.loads(r.text)
    print(response_object)
    return response_object['response']


@signature_auth
def edit_template(*args, **kwargs):
    resource_url = kwargs['resource']

    get_params = {
        'signature': kwargs['headers']['X-Auth-Signature'],
        'workspace': kwargs['headers']['X-Auth-Workspace'],
        'key': kwargs['headers']['X-Auth-Key'],
        'data': json.dumps(kwargs.get('data', {}))
    }

    return '{base_path}{resource_url}?'.format(
        base_path=BASE_PATH,
        resource_url=resource_url
    ) + urllib.parse.urlencode(get_params)


@signature_auth
def create_template(*args, **kwargs):
    resource_url = kwargs['resource']
    headers = kwargs['headers']
    template_name = kwargs['template_name']

    data = {
        'name': template_name
    }

    r = requests.post('{}{}'.format(
        BASE_PATH,
        resource_url),
        headers=headers, json=data)

    response_object = json.loads(r.text)
    template_data = response_object['response']

    if settings.PDFGENERATOR_API_RETURN_EDIT_UPON_CREATE:
        template_id = template_data['id']
        return edit_template(template_id=template_id, data={})
    else:
        return template_data


@signature_auth
def download_document(*args, **kwargs):
    resource_url = kwargs['resource']
    headers = kwargs['headers']
    name = kwargs['name']
    data = kwargs.get('data', {})

    params = {
        'name': name,
        'output': settings.PDFGENERATOR_API_OUTPUT_TYPE,
        'format': settings.PDFGENERATOR_API_FORMAT_TYPE
    }
    print('{}{}?{}'.format(
        BASE_PATH,
        resource_url,
        urllib.parse.urlencode(params)))
    r = requests.post('{}{}?{}'.format(
        BASE_PATH,
        resource_url,
        urllib.parse.urlencode(params)),
        headers=headers, json=data)
    print(r.text)
    response_object = json.loads(r.text)
    return response_object


@signature_auth
def delete_template(*args, **kwargs):
    resource_url = kwargs['resource']
    headers = kwargs['headers']

    r = requests.delete('{}{}'.format(
        BASE_PATH,
        resource_url),
        headers=headers)

    response_object = json.loads(r.text)
    if response_object['response']['success']:
        return True
    return False

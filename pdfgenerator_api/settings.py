from django.conf import settings


PDFGENERATOR_API_BASEPATH = getattr(settings,
                                   'PDFGENERATOR_API_BASEPATH',
                                   'https://us1.pdfgeneratorapi.com/api/v3/')

PDFGENERATOR_API_KEY = getattr(settings, 'PDFGENERATOR_API_KEY',
                              None)

PDFGENERATOR_API_SECRET = getattr(settings, 'PDFGENERATOR_API_SECRET',
                                 None)

PDFGENERATOR_API_WORKSPACE = getattr(settings, 'PDFGENERATOR_API_WORKSPACE',
                                    None)

PDFGENERATOR_API_RETURN_EDIT_UPON_CREATE = getattr(
    settings,
    'PDFGENERATOR_API_RETURN_EDIT_UPON_CREATE',
    False)

PDFGENERATOR_API_OUTPUT_TYPE = getattr(
    settings,
    'PDFGENERATOR_API_OUTPUT_TYPE',
    'base64')

PDFGENERATOR_API_FORMAT_TYPE = getattr(
    settings,
    'PDFGENERATOR_API_FORMAT_TYPE',
    'pdf')

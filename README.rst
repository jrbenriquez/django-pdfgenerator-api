===============================
Django PDFGenerator_API
===============================

Django PDFGenerator_API is a simple Django app used connect and consume the provided api for PDFGeneratorAPI.
Public documentation of the API Service used is available at:

https://docs.pdfgeneratorapi.com/


Quick start
-----------

1. Add "pdfgenerator_api" to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = [
        ...
        'pdfgenerator_api',
    ]

2. Add your KEY, SECRET and WORKSPACE name in your settings.py or your environment variables::

    PDFGENERATOR_API_KEY = <key>
    PDFGENERATOR_API_SECRET = <secret>
    PDFGENERATOR_API_WORKSPACE = <workspace>


3. Additional options include: [] means default

    PDFGENERATOR_API_BASEPATH                  
        - if need to override default basepath
    
    PDFGENERATOR_API_RETURN_EDIT_UPON_CREATE   
        - [False]/True. Choose what is returned upon creating template (Edit Link[True] or Template Data[False])
    
    PDFGENERATOR_API_OUTPUT_TYPE
        - [base64]/url/I
    
    PDFGENERATOR_API_FORMAT_TYPE               
        - [pdf]/zip/html


METHODS
-------

1. List Template - view_templates()

2. Get Template  - view_template(template_id=<id>)   

3. Edit Template - edit_template(template_id=<id>)

4. Create Template - create_template(template_name=<name>)

5. Download Document - download_document(name=<filename>, data=<json_data>)

6. Delete Template - delete_template(template_id=<template_id>)

7. Copy Template (Not Yet Implemented)

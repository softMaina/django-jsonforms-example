from django.shortcuts import render
from django_jsonforms.forms import JSONSchemaForm

# Create your views here.
from .forms import RegistrySettingsForm

def index(request):
    # form = JSONSchemaForm(schema={
    #         'type': 'object',
    #         'title': 'National Id',
    #         'properties': {
    #             'color': {
    #                 'description': 'a color',
    #                 'type': 'string'
    #             },
    #             'number': {
    #                 'description': 'a very nice number',
    #                 'type': 'integer'
    #             },
    #             'list': {
    #                 'description': 'what a list',
    #                 'type': 'array',
    #                 'items': {
    #                     'type': 'string'
    #                 }
    #             }
    #         }
    #     },options={"theme":"bootstrap4", "disable_edit_json":True,"disable_array_add":True,"disable_collapse":True,"disable_properties":True},ajax=True)
    form = RegistrySettingsForm()

    output = form.as_p()
    print(output.find('class=\"editor_holder\"'))
    media = str(form.media)
    print(media.find('jsoneditor.min.js'))
    return render(request,'index.html',{'form':form})
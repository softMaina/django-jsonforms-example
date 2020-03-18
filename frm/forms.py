from django.forms import ModelForm, Form
from django_jsonforms.forms import JSONSchemaField
import json
class RegistrySettingsForm(Form):

    json = JSONSchemaField(schema={
  "title": "Birth Certificate",
  "type": "object",
  "properties": {
    "name": {
      "type": "string",
      "description": "First and Last name",
      "minLength": 4,
      "default": "Enter your Name"
    },
 "fathers_name": {
      "type": "string",
      "description": "First and Last name",
      "minLength": 4,
      "default": "Enter your Name"
    },
 "mothers_name": {
      "type": "string",
      "description": "First and Last name",
      "minLength": 4,
      "default": "Enter your Name"
    },
    "birth_entry_no": {
      "type": "integer",
      "default": "",
      "minlength":10
    },
    "gender": {
      "type": "string",
      "enum": [
        "male",
        "female",
        "other"
      ]
    },
    "date_of_birth": {
      "type": "string",
      "format": "date",
      "options": {
        "flatpickr": {}
      }
    },
    "district": {
      "type": "string",
      "title": "Location",
      "description": "Place of Birth",
      "default":"Kenya"
    }

  }
},options={"theme":"bootstrap3"}, ajax=True)
        

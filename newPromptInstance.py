import os
import django
os.environ['DJANGO_SETTINGS_MODULE'] = 'll_project.settings'
django.setup()
from createPrompt import generatePrompt


PROMPT = generatePrompt()


from imageGeneration.models import Prompt

def createPrompt():
    prompt_model = Prompt()
    prompt_model.text_field = PROMPT
    prompt_model.save()
    
createPrompt()
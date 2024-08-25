from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.http import require_http_methods

from visits.models import translatorVisitsNew

from . import utils

@require_http_methods(["GET", "POST"])
def translate_70b(request):
    languages = ["Afrikaans", "Albanian", "Amharic", "Arabic", "Armenian", "Assamese", "Aymara", "Azerbaijani", "Bambara", "Basque", 
                 "Belarusian", "Bengali", "Bhojpuri", "Bosnian", "Bulgarian", "Catalan", "Cebuano", "Chinese (Simplified)", 
                 "Chinese (Traditional)", "Corsican", "Croatian", "Czech", "Danish", "Dhivehi", "Dogri", "Dutch", "English", 
                 "English (British)", "Esperanto", "Estonian", "Ewe", "Filipino (Tagalog)", "Finnish", "French", "Frisian", "Galician", 
                 "Georgian", "German", "Greek", "Guarani", "Gujarati", "Haitian Creole", "Hausa", "Hawaiian", "Hebrew", "Hindi","Hmong", 
                 "Hungarian", "Icelandic", "Igbo", "Ilocano", "Indonesian", "Irish", "Italian", "Japanese", "Javanese", "Kannada", "Kazakh", 
                 "Khmer", "Kinyarwanda", "Konkani", "Korean", "Krio", "Kurdish", "Kurdish (Sorani)", "Kyrgyz", "Lao", "Latin", "Latvian", 
                 "Lingala", "Lithuanian", "Luganda", "Luxembourgish", "Macedonian", "Maithili", "Malagasy", "Malay", "Malayalam", "Maltese", 
                 "Maori", "Marathi", "Meiteilon (Manipuri)", "Mizo", "Mongolian", "Myanmar (Burmese)", "Nepali", "Norwegian", 
                 "Nyanja (Chichewa)", "Odia (Oriya)", "Oromo", "Pashto", "Persian", "Polish", "Portuguese", "Punjabi", "Quechua", "Romanian", 
                 "Russian", "Samoan", "Sanskrit", "Scots Gaelic", "Sepedi", "Serbian", "Sesotho", "Shona", "Sindhi", "Sinhala (Sinhalese)", 
                 "Slovak", "Slovenian", "Somali", "Spanish", "Sundanese", "Swahili", "Swedish", "Tagalog (Filipino)", "Tajik", "Tamil", "Tatar", 
                 "Telugu", "Thai", "Tigrinya", "Tsonga", "Turkish", "Turkmen", "Twi (Akan)", "Ukrainian", "Urdu", "Uyghur", 
                 "Uzbek", "Vietnamese", "Welsh", "Xhosa", "Yiddish", "Yoruba", "Zulu"]

    if request.method == "POST" and request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        language1 = request.POST.get("language1")
        language2 = request.POST.get("language2")
        tone = request.POST.get("tone")
        inputText = request.POST.get("inputText")

        output = utils.Translation70b(language1, language2, tone, inputText)
        return JsonResponse({'output': output})
    

    # queryset = translatorVisits.objects.all()
    # translatorVisits.objects.create()

    if(translatorVisitsNew.objects.all().count() == 0):
        translatorVisitsNew.objects.create(visits = 0)


    value = translatorVisitsNew.objects.all()[0].visits + 1
    translatorVisitsNew.objects.all().delete()
    translatorVisitsNew.objects.create(visits = value)


    return render(request, 'translator_basic.html', {"languages": languages, "pageVisits": value})

    
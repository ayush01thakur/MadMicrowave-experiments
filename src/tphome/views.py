from django.http import HttpResponse
from django.shortcuts import render, redirect

from visits.models import PageVisit

from . import utils


def home(request):
    queryset = PageVisit.objects.all()
    PageVisit.objects.create()
    context = {
               "pageVisitCount": queryset.count(),

               }
    
    return render(request, 'home.html', context)


def translate(request):
    output = "your translation will be shown here !"
    if(request.method == "POST"):
        data = request.POST

        language1= data.get("language1")
        language2= data.get("language2")
        tone= data.get("tone")
        inputText = data.get("inputText")

        # print(language1, language2, tone, inputText) this is working.
        output = utils.Translation70b(language1, language2, tone, inputText)
        


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

    context = {
        "languages": languages,
        "output": output
    }

    # i have to write the logic to traslate from one language to another using api, and then have to show the output
    
    return render(request, 'translate.html', context)
    
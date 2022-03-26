text_data = {
        'en':
        {
            "display":"Language: English",
            "quit":"Quit",
            "start":"Start",
            "back":"Back",
            "success_survey":"The survey was completed successfully!",
            "questions":["How satisfied were you with the attitude of health workers?\n Were they caring, respectful and compassionate?", 
                "How satisfied were you with the waiting time?", 
                "Were medical equipment, drugs and supplies available at the facility?", 
                "Were you satisfied with available infrastructure?", 
                "Was there ambulance service available?", 
                "Was the facility clean?" 
                ],
            "muted":"Muted",
            "unmuted":"Unmuted",
            "extra_help":"Extra help?",
            },
        'nl':
        {
            "display":"Taal: Nederlands",
            "quit":"Stop",
            "start":"Start",
            "back":"Terug",
            "success_survey":"De vragenlijst is succesvol afgerond. Bedankt voor uw tijd.",
            "questions":["Hoe tevreden bent u over de werkhouding van het medisch personeel?",
                "Hoe tevreden bent u over de wachttijd?",
                "Hoe tevreden bent u over de beschikbaarheid van medische apparatuur, medicijnen en benodigdheden?",
                "Hoe tevreden bent u over de beschikbare infrastructuur?",
                "Is er een ambulancedienst beschikbaar bij deze faciliteit?",
                "Hoe tevreden bent u over de hygiëne van de faciliteit?"
                ],
            "muted": "Gedempt",
            "unmuted":"Dempen opheffen",
            "extra_help":"Extra help?",
            }
        }

def get_translated_field(word):
    return text_data[languages[current_lang]][word]

def change_lang():
    current_lang = (current_lang + 1) % len(languages)

languages = list(text_data.keys())
current_lang = languages.index("en")

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
            "welcome":"Welcome! Scan card to start survey!",
            "muted":"Muted",
            "unmuted":"Unmuted",
            "extra_help":"Extra help?",
            "questions_voice":
            [
                "recordings/en/q1.mp3",
                "recordings/en/q2.mp3",
                "recordings/en/q3.mp3",
                "recordings/en/q4.mp3",
                "recordings/en/q5.mp3",
                "recordings/en/q6.mp3",
                "recordings/en/q_extra.mp3",
            ]
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
            "questions_voice":
            [
                "recordings/nl/q1.mp3",
                "recordings/nl/q2.mp3",
                "recordings/nl/q3.mp3",
                "recordings/nl/q4.mp3",
                "recordings/nl/q5.mp3",
                "recordings/nl/q6.mp3",
            ],
            "welcome":"Welcome! Scan card to start survey!",
            "muted": "Gedempt",
            "unmuted":"Dempen opheffen",
            "extra_help":"Extra help?",
            }
        }


languages = list(text_data.keys())

class TranslationService:
    def __init__(self):
        self.current_lang = languages.index("en")

    def get_translated_field(self,word):
        return text_data[languages[self.current_lang]][word]

    def change_lang(self):
        self.current_lang = (self.current_lang + 1) % len(languages)




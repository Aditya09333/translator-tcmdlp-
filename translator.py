from deep_translator import GoogleTranslator
from deep_translator.exceptions import LanguageNotSupportedException

def get_supported_languages() -> dict:
    """
    Returns a dictionary of languages supported by the GoogleTranslator.
    """
   
    return {
        'af': 'Afrikaans', 'sq': 'Albanian', 'am': 'Amharic', 'ar': 'Arabic',
        'hy': 'Armenian', 'az': 'Azerbaijani', 'eu': 'Basque', 'be': 'Belarusian',
        'bn': 'Bengali', 'bs': 'Bosnian', 'bg': 'Bulgarian', 'ca': 'Catalan',
        'ceb': 'Cebuano', 'ny': 'Chichewa', 'zh-CN': 'Chinese (Simplified)',
        'zh-TW': 'Chinese (Traditional)', 'co': 'Corsican', 'hr': 'Croatian',
        'cs': 'Czech', 'da': 'Danish', 'nl': 'Dutch', 'en': 'English',
        'eo': 'Esperanto', 'et': 'Estonian', 'tl': 'Filipino', 'fi': 'Finnish',
        'fr': 'French', 'fy': 'Frisian', 'gl': 'Galician', 'ka': 'Georgian',
        'de': 'German', 'el': 'Greek', 'gu': 'Gujarati', 'ht': 'Haitian Creole',
        'ha': 'Hausa', 'haw': 'Hawaiian', 'iw': 'Hebrew', 'he': 'Hebrew',
        'hi': 'Hindi', 'hmn': 'Hmong', 'hu': 'Hungarian', 'is': 'Icelandic',
        'ig': 'Igbo', 'id': 'Indonesian', 'ga': 'Irish', 'it': 'Italian',
        'ja': 'Japanese', 'jw': 'Javanese', 'kn': 'Kannada', 'kk': 'Kazakh',
        'km': 'Khmer', 'ko': 'Korean', 'ku': 'Kurdish (Kurmanji)',
        'ky': 'Kyrgyz', 'lo': 'Lao', 'la': 'Latin', 'lv': 'Latvian',
        'lt': 'Lithuanian', 'lb': 'Luxembourgish', 'mk': 'Macedonian',
        'mg': 'Malagasy', 'ms': 'Malay', 'ml': 'Malayalam', 'mt': 'Maltese',
        'mi': 'Maori', 'mr': 'Marathi', 'mn': 'Mongolian', 'my': 'Myanmar (Burmese)',
        'ne': 'Nepali', 'no': 'Norwegian', 'or': 'Odia', 'ps': 'Pashto',
        'fa': 'Persian', 'pl': 'Polish', 'pt': 'Portuguese', 'pa': 'Punjabi',
        'ro': 'Romanian', 'ru': 'Russian', 'sm': 'Samoan', 'gd': 'Scots Gaelic',
        'sr': 'Serbian', 'st': 'Sesotho', 'sn': 'Shona', 'sd': 'Sindhi',
        'si': 'Sinhala', 'sk': 'Slovak', 'sl': 'Slovenian', 'so': 'Somali',
        'es': 'Spanish', 'su': 'Sundanese', 'sw': 'Swahili', 'sv': 'Swedish',
        'tg': 'Tajik', 'ta': 'Tamil', 'te': 'Telugu', 'th': 'Thai',
        'tr': 'Turkish', 'uk': 'Ukrainian', 'ur': 'Urdu', 'ug': 'Uyghur',
        'uz': 'Uzbek', 'vi': 'Vietnamese', 'cy': 'Welsh', 'xh': 'Xhosa',
        'yi': 'Yiddish', 'yo': 'Yoruba', 'zu': 'Zulu',
    }

def translate_text(text: str, source_language_code: str, target_language_code: str) -> str | None:
    """
    Translates text using the GoogleTranslator from the deep-translator library.
    This is more reliable for a wide range of language pairs.

    Args:
        text: The text to translate.
        source_language_code: The language code of the input text (e.g., "en").
        target_language_code: The language code to translate the text into (e.g., "es").

    Returns:
        The translated text, or None if an error occurs.
    """
    try:
       
        source_to_use = 'auto' if source_language_code == 'auto' else source_language_code
        
       
        translated_text = GoogleTranslator(source=source_to_use, target=target_language_code).translate(text)
        return translated_text
        
    except LanguageNotSupportedException:
        
        print(f"Error: Language '{target_language_code}' is not supported by this translator.")
        return None
    except Exception as e:
        print(f"An unexpected error occurred during translation: {e}")
        return None

if __name__ == '__main__':
   
    print("Testing translator.py directly with deep-translator (Google)...")

    print("\n--- Translation Example 1 (English to German) ---")
    text_to_translate = "This translator is much more reliable."
    src_lang = "en"
    tgt_lang = "de"
    
    print(f"Original text ({src_lang}): {text_to_translate}")
    translated = translate_text(text_to_translate, src_lang, tgt_lang)
    
    if translated:
        print(f"Translated text ({tgt_lang}): {translated}")
    else:
        print("Translation failed.")
        
    print("\n--- Translation Example 2 (Auto-detect source) ---")
    text_to_translate_2 = "La vita è bella"
    
    src_lang_2 = "auto"
    tgt_lang_2 = "en"

    print(f"Original text (auto-detected): {text_to_translate_2}")
    translated_2 = translate_text(text_to_translate_2, src_lang_2, tgt_lang_2)
    
    if translated_2:
        print(f"Translated text ({tgt_lang_2}): {translated_2}")
    else:
        print("Translation failed.")

from translator import translate_text, get_supported_languages


SUPPORTED_LANGUAGES = get_supported_languages()

def display_supported_languages():
    """Displays the list of supported languages."""
    print("\nSupported Languages (via Google Translate):")
    
    sorted_langs = sorted(SUPPORTED_LANGUAGES.items(), key=lambda item: item[1])
    
    for code, name in sorted_langs:
        print(f"- {name} (code: {code})")
    print("...and many more. You can also use 'auto' for the source language.")
    print("-" * 20)

def get_language_code(name_or_code: str, is_source: bool = False) -> str | None:
    """
    Finds a language code from user input. Allows 'auto' for the source language.
    """
    normalized_input = name_or_code.lower()
    
    if is_source and normalized_input == 'auto':
        return 'auto'

    if normalized_input in SUPPORTED_LANGUAGES:
        return normalized_input
    
    for code, lang_name in SUPPORTED_LANGUAGES.items():
        if lang_name.lower() == normalized_input:
            return code
            
    return None

def main_cli():
    """Main function for the command-line interface."""
    print("Welcome to the Reliable Translator!")
    print("Powered by deep-translator (using Google Translate backend).")
    
    while True:
        
        print("\nEnter languages by name or code (e.g., 'English' or 'en').")
        print("Type 'list' to see the full language list, or press Enter to continue.")
        
        user_command = input("> ").strip().lower()
        if user_command == 'list':
            display_supported_languages()
            continue

        
        source_lang_input = input("Enter the source language (or 'auto'): ").strip()
        source_lang_code = get_language_code(source_lang_input, is_source=True)
        if not source_lang_code:
            print(f"Invalid source language: '{source_lang_input}'. Please try again.")
            continue

        
        target_lang_input = input("Enter the target language: ").strip()
        target_lang_code = get_language_code(target_lang_input)
        if not target_lang_code:
            print(f"Invalid target language: '{target_lang_input}'. Please try again.")
            continue

        if source_lang_code == target_lang_code:
            print("Source and target languages cannot be the same.")
            continue
            
        text_to_translate = input(f"Enter text to translate: ").strip()
        if not text_to_translate:
            print("No text provided for translation.")
            continue
        
        source_display_name = "auto-detected" if source_lang_code == 'auto' else SUPPORTED_LANGUAGES[source_lang_code]
        print(f"\nTranslating from {source_display_name} to {SUPPORTED_LANGUAGES[target_lang_code]}...")
        
        translated_text = translate_text(text_to_translate, source_lang_code, target_lang_code)
        
        if translated_text:
            print(f"\nOriginal text: {text_to_translate}")
            print(f"Translated text: {translated_text}")
        else:
            print("Translation failed. Please check your internet connection or the language codes.")

        print("-" * 20)
        another_translation = input("Do you want to translate another text? (yes/no): ").strip().lower()
        if another_translation != 'yes':
            print("Thank you for using the Reliable Translator!")
            break

if __name__ == "__main__":
    main_cli()

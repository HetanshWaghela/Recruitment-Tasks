import re

def transform_text(text : str) -> str:
    text= re.sub(r'\b[A-Z]{2,}\b', lambda x: x.group().lower(), text)

    text= re.sub(r'!+','🎭✨', text)

    text= re.sub(r'\bboring\b', 'DEFINATELY-NOT-BORING', text, flags=re.IGNORECASE)

    return text

test_cases = [
        "This is URGENT and IMPORTANT!",
        "The movie was boring but the ending was great!",
        "HELLO WORLD!!! How are you?",
        "I find this topic quite boring."
    ]
for test in test_cases:
    print(f"OUTPUT: {transform_text(test)}")


import re
import codecs

def clean_email_text(text):  # EXPECTS JSON STRING
    # 1. Decode escaped unicode (e.g., \\u034f -> \u034f)
    try:
        text = codecs.decode(text, 'unicode_escape')
    except Exception:
        pass

    # 2. Remove invisible/control characters
    text = re.sub(r'[\u200c\u200b\u200d\u034f\u202c\u202d\u00a0\ufeff]+', '', text)

    # 3. Remove URLs (http, https, www)
    text = re.sub(r'https?://\S+|www\.\S+', '', text)

    # 4. Collapse multiple newlines, even with junk/invisible chars in between
    text = re.sub(r'(\n[\s\u200c\u034f\ufeff\u00a0]*){2,}', '\n', text)

    # 5. Normalize internal whitespace and strip leading/trailing spaces
    text = re.sub(r'[ \t]+', ' ', text)
    text = re.sub(r' *\n *', '\n', text).strip()

    return text

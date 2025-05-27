import dateparser
from datetime import timedelta


def parse_time_from_content(content):
    import re
    from datetime import timedelta
    import dateparser

    # فقط دنبال قسمت‌هایی بگرد که ممکنه زمان داشته باشن
    possible_phrases = re.findall(r"(پنجشنبه.*?|جمعه.*?|شنبه.*?|امروز.*?|فردا.*?|ساعت \d{1,2}.*?)(?=\s|$)", content)

    for phrase in possible_phrases:
        parsed = dateparser.parse(phrase.strip(), languages=['fa'])
        if parsed:
            start = parsed
            end = start + timedelta(hours=1)
            return start, end

    # fallback: کل متن رو تست کن
    parsed = dateparser.parse(content, languages=['fa'])
    if parsed:
        start = parsed
        end = start + timedelta(hours=1)
        return start, end

    raise ValueError("زمان معتبر یافت نشد")

import re


def extract_emails_and_phones(text):
    email_pattern = r"\b[a-z0-9._%+-]+@[a-z0-9.-]+\.[a-z]{2,}\b"
    phone_pattern = r"\+?\d{1,4}[-\s]?\d{1,4}[-\s]?\d{1,4}[-\s]?\d{1,4}"
    emails = re.findall(email_pattern, text)
    phones = re.findall(phone_pattern, text)
    return emails, phones


def extract_dates(text):
    date_pattern = r"\b(\d{2}[-/]\d{2}[-/]\d{4}|\d{2}/\d{2}/\d{4})\b"
    return re.findall(date_pattern, text)


def extract_urls(text):
    url_pattern = r"\bhttps?://[a-z0-9.-]+\.[a-z]{2,}\b"
    return re.findall(url_pattern, text)


def replace_word(text, old_word, new_word):
    pattern = r"\b" + re.escape(old_word) + r"\b"
    return re.sub(pattern, new_word, text)


text = input("Enter text: ")

emails, phones = extract_emails_and_phones(text)
dates = extract_dates(text)
urls = extract_urls(text)

print("Emails:", emails)
print("Phones:", phones)
print("Dates:", dates)
print("URLs:", urls)

old_word = input("Enter word to replace: ")
new_word = input("Enter replacement word: ")

print("Modified text:", replace_word(text, old_word, new_word))

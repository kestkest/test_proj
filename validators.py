import re 

def is_date(data):
    regexp1 = re.compile(r'^(0[1-9]|[12][0-9]|3[01])\.(0[1-9]|1[012])\.\d{4}$')
    regexp2 = re.compile(r'^\d{4}-(0[1-9]|1[012])-(0[1-9]|[12][0-9]|3[01])$')
    if regexp1.match(data) or regexp2.match(data):
        return True
    return False

def is_phone(data):
    reg = re.compile(r'^\+7 \d{3} \d{3} \d{2} \d{2}$')
    result = True if reg.match(data) else False
    return result


def is_email(data):
    reg = re.compile(r'[\w.-]+@[\w.-]+\.[\w.-]+$')
    if reg.match(data):
        return True
    return False

def is_text(data):
    return True

validators = {'email': is_email, 'date': is_date, 'phone': is_phone, 'text': is_text}


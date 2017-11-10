from validators import validators

def fields_name_intersect(form, data):
    for key in form:
        if key == 'name':
            continue
        if not key in data:
            return False
    return True

def fields_types_match(form, data):
    for key, val in form.items():
        if key == 'name':
            continue
        if not validators[val](data[key]):
            return False
    return True

def get_fields_and_types(data):
    res = {}
    for key in data:
        if validators['date'](data[key]):
            res[key] = 'date'
            continue
        if validators['phone'](data[key]):
            res[key] = 'phone'
            continue
        if validators['email'](data[key]):
            res[key] = 'email'
            continue
        res[key] = 'text'
    return res

def get_proper_form(forms, data):
    name = None
    for form in forms:
        if not fields_name_intersect(form, data):
            continue
        else:
            if fields_types_match(form, data):
                name = form['name']
                break
    return name
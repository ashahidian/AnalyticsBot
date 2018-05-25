def create_tag(word, type):

    if type == 'EUR/MXN' or 'CHF/MXN' or 'USD/MXN' or 'USD/BRL':
        new_compound = [word, type, 'currencies']

    elif type == 'cc' or 'volume' or 'non-risk cc' or 'at risk cc' \
            or 'average rollover' or 'rollover ratio' or 'net client':
        new_compound = [word, type, 'metrics']

    elif type == 'country' or 'region':
        new_compound = [word, type, 'location']

    else:
        new_compound = [word, type, 'NOT FOUND']

    return new_compound
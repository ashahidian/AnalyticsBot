# old file. should be deleted

def create_tag(word, type):

    if type == 'business date' or type == 'last updated':
        new_compound = [word, type, 'date']

    elif type == 'currency pair key' or 'currency pair group key' or 'currency pair group' or 'currency pairs':
        new_compound = [word, type, 'dollardollar']

    elif type == 'marketer' or 'marketer code':
        new_compound = [word, type, 'salesperson']

    elif type == 'cc dollar' or 'cc euro' or 'volume euro':
        new_compound = [word, type, 'metrics']

    elif type == 'rfq numbers' or 'rfq volumes' or 'rfq delts':
        new_compound = [word, type, 'rfq']

    elif type == 'bl marketing group' or 'marketing client' or 'crds name' or 'crds code':
        new_compound = [word, type, 'clientname']

    elif type == 'platform group' or 'platform name' or 'platform type':
        new_compound = [word, type, 'platform']

    elif type == 'country' or 'region':
        new_compound = [word, type, 'location']

    elif type == 'lessone' or 'onetothree' or 'threetotwelve':
        new_compound = [word, type, 'tenorgroup']

    else:
        new_compound = [word, type, 'NOT FOUND']

    return new_compound
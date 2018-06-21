from pyCharm.app.management.initial_setup import values_from_database, setup_categories


def pipeline():
    # call initial setup to gather data from database
    client_list, currency_list, deal_id_list = values_from_database()

    # call initial setup to create dictionaries
    setup_categories(client_list, deal_id_list, currency_list)

    # call initial setup to create synonym dictionaries
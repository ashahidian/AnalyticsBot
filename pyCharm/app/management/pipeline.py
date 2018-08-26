from pyCharm.app.management.category_builder import values_from_database, setup_categories
import subprocess


def pipeline():
    # call initial setup to gather data from database
    client_list, currency_list, deal_id_list = values_from_database()

    # call initial setup to create dictionaries
    setup_categories(client_list, deal_id_list, currency_list)

    # call initial setup to create synonym dictionaries



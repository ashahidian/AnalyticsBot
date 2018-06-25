# first, call the database and gather the client names, id's and currencies
from pyCharm.app.rules.categories import category_names, category_currency, category_deal_id
from pyCharm.app.management.sql_treatment import sql_call


# call sql_call function to get the values from the database
def values_from_database():
    # update names according to database
    client_list = sql_call("SELECT client_name FROM example_table")
    currency_list = sql_call("SELECT currency_list FROM example_table")
    deal_id_list = sql_call("SELECT deal_id FROM example_table")

    return client_list, currency_list, deal_id_list


# call category creation
def setup_categories(client_list, deal_id_list, currency_list):
    category_names(client_list)
    category_currency(currency_list)
    category_deal_id(deal_id_list)

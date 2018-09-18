# first, call the database and gather the client names, id's and currencies
from bot.app.management.categories import *
from bot.app.management.sql_connection import sql_call


# call sql_call function to get the values from the database
def values_from_database():
    # update names according to database
    client_list = sql_call("SELECT DISTINCT Client FROM example_table")
    currency_list = sql_call("SELECT DISTINCT Currency Pair FROM example_table")
    deal_id_list = sql_call("SELECT DISTINCT Deal ID FROM example_table")
    platform_list = sql_call("SELECT DISTINCT Platform FROM example_table")

    return client_list, currency_list, deal_id_list, platform_list


# call category creation
def setup_categories(client_list, deal_id_list, currency_list, platform_list):
    category_names(client_list)
    category_currency(currency_list)
    category_deal_id(deal_id_list)
    category_platform(platform_list)

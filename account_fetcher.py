"""
FILE_NAME:      account_fetcher.py

DESCRIPTION:    Collect data from the exchange platform and continuously 
                update the data csv file to allow other codes to run.

AUTHOR:         Martin Jacques-Yves LEMAIRE

CONTACT:        martinjlemaire@icloud.com

DEPENDENT_FILES:
 - data.csv
"""

# IMPORTS
import ccxt, csv
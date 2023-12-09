"""
FILE_NAME:      balancer_injector_portfolio.py

DESCRIPTION:    balance the portfolio when large differences appear between allocations
                analogously manage capital injection in the different allocations

AUTHOR:         Martin Jacques-Yves LEMAIRE

CONTACT:        martinjlemaire@icloud.com

DEPENDENT_FILES:
 - data.csv
 - market_order_executer.py
"""

# IMPORTS
import ccxt, csv
#   a1.py
#   Shirley Z Kabir (szk4) and Sneha Kumar (sk2279)
#   September 18, 2016

"""Module for currency exchange
This module provides several string parsing functions to implement a
simple currency exchange routine using an online currency service.
The primary function in this module is exchange."""

# PART A
def before_space(s):
    """Returns: Substring of s; up to, but not including, the first space
    Parameter s: the string to slice
    Precondition: s has at least one space in it"""
    
    end = s.index(' ')
    return s[0:end]


def after_space(s):
    """Returns: Substring of s after the first space
    Parameter s: the string to slice
    Precondition: s has at least one space in it"""
    
    start = s.index(' ')
    return s[start+1:]

# PART B

def first_inside_quotes(s):
    """Returns: The first substring of s between two (double) quote characters
    A quote character is one that is inside a string, not one that delimits it.
    We typically use single quotes (') to delimit a string if want to use a
    double quote character (") inside of it.
    Example: If s is 'A "B C" D', this function returns 'B C'
    Example: If s is 'A "B C" D "E F" G', this function still returns 'B C'
    because it only picks
    the first such substring.
    
    Parameter s: a string to search
    Precondition: s is a string with at least two (double) quote characters
    inside."""
    
    start = s.index('"')
    end = s.index('"', start + 1)
    return s[start + 1: end]

    
def get_from(json):
    """Returns: The FROM value in the response to a currency query.
    Given a JSON response to a currency query, this returns the string inside
    double quotes (") immediately following the keyword "from". For example, if
    the JSON is
        '{"from":"2 United States Dollars","to":"1.825936 Euros","success":
        true,"error":""}'
    then this function returns '2 United States Dollars' (not '"2 United
        States Dollars"').
    It returns the empty string if the JSON is the result of on invalid query.
    Parameter json: a json string to parse
    Precondition: json is the response to a currency query"""
    
    return first_inside_quotes(json.replace('"from"',""))

    
def get_to(json):
    """Returns: The TO value in the response to a currency query.
    Given a JSON response to a currency query, this returns the string inside
    double quotes (") immediately following the keyword "to". For example, if the JSON is
      '{"from":"2 United States Dollars","to":"1.825936 Euros","success":true,"error":""}'
    then this function returns '1.825936 Euros' (not '"1.825936 Euros"'). It returns the
    empty string if the JSON is the result of on invalid query.
    Parameter json: a json string to parse
    Precondition: json is the response to a currency query"""
    
    start = json.index('"to"')+len('"to":')
    return first_inside_quotes(json.replace(json[:start], ""))
    
    
def has_error(json):
    """Returns: True if the query has an error; False otherwise.
    Given a JSON response to a currency query, this returns the opposite
    of the value following the keyword "success". For example, if the JSON is
      '{"from":"","to":"","success":false,"error":"Source currency code is
      invalid."}'
    then the query is not valid, so this function returns True (It does NOT return
    the message 'Source currency code is invalid').
    Parameter json: a json string to parse
    Precondition: json is the response to a currency query"""
    return json.find("false") != -1

# PART C

import urllib2

def currency_response(currency_from, currency_to, amount_from):
    """Returns: a JSON string that is a response to a currency query.
    A currency query converts amount_from money in currency currency_from 
    to the currency currency_to. The response should be a string of the form
        '{"from":"<old-amt>","to":"<new-amt>","success":true, "error":""}'
    where the values old-amount and new-amount contain the value and name 
    for the original and new currencies. If the query is invalid, both 
    old-amount and new-amount will be empty, while "valid" will be followed 
    by the value false.
    
    Parameter currency_from: the currency on hand
    Precondition: currency_from is a string
    
    Parameter currency_to: the currency to convert to
    Precondition: currency_to is a string
    
    Parameter amount_from: amount of currency to convert
    Precondition: amount_from is a float"""
    
    amtstring = str(amount_from)
    siteparta = 'http://cs1110.cs.cornell.edu/2016fa/a1server.php?from='
    sitepartb = '&to='
    sitepartc = '&amt='
    coolsite = (siteparta + currency_from + sitepartb + currency_to + sitepartc
                + amtstring)    
    site = urllib2.urlopen(coolsite)
    finalsite = site.read()
    return finalsite

    
# PART D

def iscurrency(currency):
    """Returns: True if currency is a valid (3 letter code for a) currency. 
    It returns False otherwise.
    
    Parameter currency: the currency code to verify
    Precondition: currency is a string."""
    
    query = currency_response(currency, 'USD', 2.5)
    return not has_error(query)


def exchange(currency_from, currency_to, amount_from):
    """Returns: amount of currency received in the given exchange.
    In this exchange, the user is changing amount_from money in 
    currency currency_from to the currency currency_to. The value 
    returned represents the amount in currency currency_to.
    The value returned has type float.
    
    Parameter currency_from: the currency on hand
    Precondition: currency_from is a string for a valid currency code
    
    Parameter currency_to: the currency to convert to
    Precondition: currency_to is a string for a valid currency code
    
    Parameter amount_from: amount of currency to convert
    Precondition: amount_from is a float"""
    
    query = currency_response(currency_from, currency_to, amount_from)
    start = query.index('"to"')+8
    end = query.index(' ', start)
    finalstring = query[start:end]
    return float(finalstring)
    

    

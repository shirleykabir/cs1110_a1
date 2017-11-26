#   a1test.py
#   Sneha Kumar (sk2279) and Shirley Kabir (szk4)
#   September 18, 2016

"""Unit test for module a1
When run as a script, this module invokes several procedures that 
test the various functions in the module a1."""

import a1
import cornelltest

def testA():
    #   TEST ONE
    print 'Testing function before_space 1'
    result = a1.before_space("Python rocks")
    cornelltest.assert_equals('Python', result)
    print 'Testing function after_space 1'
    result = a1.after_space("Python rocks")
    cornelltest.assert_equals('rocks', result)
    #  TEST TWO
    print 'Testing function before_space 2'
    result = a1.before_space("3324.92 Euros")
    cornelltest.assert_equals('3324.92', result)
    print 'Testing function after_space 2'
    result = a1.after_space("3324.92 Euros")
    cornelltest.assert_equals('Euros', result)
    # TEST THREE
    print 'Testing function before_space 3'
    result = a1.before_space("Cornell  University")
    cornelltest.assert_equals('Cornell', result)
    print 'Testing function after_space 3'
    result = a1.after_space("Cornell  University")
    cornelltest.assert_equals(' University', result)
    # TEST FOUR
    print 'Testing function before_space 4'
    result = a1.before_space("Mynameis ")
    cornelltest.assert_equals('Mynameis', result)
    print 'Testing function after_space 3'
    result = a1.after_space("Mynameis ")
    cornelltest.assert_equals('', result)
    
def testB():
    #   TEST ONE
    print 'Testing function get_from 1'
    result = a1.get_from('{"from":"2 United States Dollars","to":"1.825936 Euros","success":true,"error":""}')
    cornelltest.assert_equals('2 United States Dollars', result)
    #   TEST TWO
    print 'Testing function get_from 2'
    result = a1.get_from('{"from":"","to":"Qatari Rial","success":true,"error":""}')
    cornelltest.assert_equals('', result)
    #   TEST ONE
    print 'Testing function get_to 1'
    result = a1.get_to('{"from":"2 United States Dollars","to":"1.825936 Euros","success":true,"error":""}')
    cornelltest.assert_equals('1.825936 Euros', result)
    #   TEST TWO
    print 'Testing function get_to 2'
    result = a1.get_to('{"from":"","to":"","success":true,"error":""}')
    cornelltest.assert_equals('', result)
    #   TEST ONE
    print 'Testing function has_error 1'
    result = a1.has_error('{"from":"2 United States Dollars","to":"1.825936 Euros","success":true,"error":""}')
    cornelltest.assert_equals(False, result)
    #   TEST TWO
    print 'Testing function has_error 2'
    result = a1.has_error('{"from":"","to":"1.825936 Euros","success":false,"error":""}')
    cornelltest.assert_equals(True, result)
def testC():
    #   TEST ONE
    print 'Testing function currency_response 1'
    result = a1.currency_response('USD', 'EUR', 2.5)
    cornelltest.assert_equals('{ "from" : "2.5 United States Dollars", "to" : "2.24075 Euros", "success" : true, "error" : "" }', result)
    #   TEST TWO
    print 'Testing function currency_response 2'
    result = a1.currency_response('TND', 'BDT', 3453.67)
    cornelltest.assert_equals('{ "from" : "3453.67 Tunisian Dinar", "to" : "122560.93186266 Bangladeshi Taka", "success" : true, "error" : "" }', result)
    

def testD():
    #   TEST ONE
    print 'Testing function iscurrency 1'
    result = a1.iscurrency('USD')
    cornelltest.assert_equals(True, result)
    #   TEST TWO
    print 'Testing function iscurrency 2'
    result = a1.iscurrency('ZZK')
    cornelltest.assert_equals(False, result)
    #   TEST ONE
    print 'Testing function exchange 1'
    result = a1.exchange('USD', 'EUR', 2.5)
    cornelltest.assert_equals(2.24075, result)
    #   TEST ONE
    print 'Testing function exchange 2'
    result = a1.exchange('GEL', 'SOS', 0.0)
    cornelltest.assert_equals(0.0, result)


testA()
testB()
testC()
testD()
print "Module a1 passed all tests"
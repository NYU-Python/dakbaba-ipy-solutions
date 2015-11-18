#!/usr/bin/env python

import stock_price_summary as sps
import pytest as pt
import numpy as np 


#GOOD variables
filename = 'aapl.txt'
ITERABLE_NUMERIC_LIST = [1, 2, 3, 4, 5]
EVEN_NUMERIC_LIST = [1, 2, 3, 4]
DUPLICATES_ORDERED = [1, 1, 2, 3, 4, 5, 5]
DUPLICATES_NOTORDERED = [1, 1, 2, 1, 1, 3, 5, 5, 4, 5, 5]
UPPER_TICKER = APPL
LOWER_TICKER = appl

#BAD variables
NON_NUMERIC_LIST = [1, 2, 3, 'a']
NON_STRING = 5
NON_ITERABLE = 5
INVALID_FILENAME = 'some_bad_filename' 
INVALID_TICKER = 'apple'
INVALID_SUMMARY_TYPE = 'length'


def test_acquire_data():
	#unreadable file argument (i.e., cannot open): raises IOError
	with pt.raises(IOError):
		sps.acquire_data(INVALID_FILENAME, 1)

	#number of entries exceeds entries in file: raises ValueError
	with pt.raises(ValueError):
		sps.acquire_data(filename, 500)

	#with good arguments: compare return value to a hard coded list of values expected
	assert sps.acquire_data(filename, 2) == [114.71, 115.00]


 def test_is_all_numbers():
 	#not an iterable: raises TypeError
 	with pt.raises(TypeError):
 		sps.is_all_numbers(NON_ITERABLE)

 	#all numbers: returns True
 	assert sps.is_all_numbers(ITERABLE_NUMERIC_LIST) == True

 	#not all numbers: returns False
 	assert sps.is_all_numbers(NON_NUMERIC_LIST) == False


def test_get_median():
	#not all numbers, raise TypeError
	with pt.raises(TypeError):
		sps.get_median(NON_NUMERIC_LIST)

	#not iterable, raise TypeError
	with pt.raises(TypeError):
		sps.get_median(NON_ITERABLE)

	#check odd number list
	assert sps.get_median(ITERABLE_NUMERIC_LIST) == 3

	#check even number list
	assert sps.get_median(EVEN_NUMERIC_LIST) == 2.5


def test_get_centered():
	#not all numbers, raise TypeError
	with pt.raises(TypeError):
		sps.get_centered(NON_NUMERIC_LIST)

	#not iterable, raise TypeError
	with pt.raises(TypeError):
		sps.get_centered(NON_ITERABLE)

	#check that duplicate values are eliminated
	assert sps.get_centered(DUPLICATES_ORDERED) == list(ITERABLE_NUMERIC_LIST)

	#check that duplicate values are eliminated that are not ordered
	assert sps.get_centered(DUPLICATES_NOTORDERED) == list(ITERABLE_NUMERIC_LIST)

	#check that get centered returns expected value
	assert sps.get_centered(ITERABLE_NUMERIC_LIST) == 3


def test_get_average():
	#not all numbers, raise TypeError
	with pt.raises(TypeError):
		sps.get_average(NON_NUMERIC_LIST)

	#not iterable, raise TypeError
	with pt.raises(TypeError):
		sps.get_average(NON_ITERABLE)

	#check that value is correct
	assert sps.get_average(EVEN_NUMERIC_LIST) == np.mean(EVEN_NUMERIC_LIST)


def test_get_filename_from_ticker():
	#bad arg type (not str): raises TypeError
	with pt.raises(TypeError):
		sps.get_filename_from_ticker(NON_STRING)

	#uppercase ticker works
	assert sps.get_filename_from_ticker(UPPER_TICKER) == '../../Python/stock_prices/appl.csv'

	#lowercase ticker works
	assert sps.get_filename_from_ticker(LOWER_TICKER) == '../../Python/stock_prices/appl.csv'


def test_validate_args():
	#bad summary value
	with pt.raises(ValueError):
		sps.validate_args(INVALID_SUMMARY_TYPE, 1, LOWER_TICKER)

	#bad ticker
	with pt.raises(IOError):
		sps.validate_args('max', 1, INVALID_TICKER)

	#days is not a number
	with pt.raises(ValueError):
		sps.validate_args('max', NON_STRING, LOWER_TICKER)

	assert sps.validate_args('max', 1, LOWER_TICKER) == '../../Python/stock_prices/appl.csv'


def test_parse_args():
	#leng too long, IndexError
	with pt.raises(IndexError):
		sps.parse_args(ITERABLE_NUMERIC_LIST)

	assert sps.parse_args('max', 1, LOWER_TICKER) == ('max', 1, LOWER_TICKER)

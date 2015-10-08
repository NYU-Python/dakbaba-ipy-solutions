#!/usr/bin/env python

#def collect_data(days, ticker):
  days = int



#creating a the list of tickers
many_tickers = raw_input('How many tickers will you want to see?)
counter = 0
company_list = []

while many tickers < counter:
  company_name = raw_input('What company would you like to see? [AAPL,FB,GOOG,LNKD,MSFT]')
  company_name = company_name.upper
  company_list.append(company_name)
  print 'What else?'
  counter =+ 1


days = int(raw_input('Now pick a number of trading days for which you would like to see the average closing price [up to 251]'))


#create a dict for company data
company_dict = {}

#loop through company names
for company in company_list
  filename = company_name+'.txt'
  #loop through individual companies collecting data
  for line in open(filename):
	  date, start, high, low, end, volume = line.split(',')
	  company_list.append(end)
	  
	  #slice what I need
    sliced_list = company_list[0:days+1]
    company_dict(average_price = sum(sliced_list)/len(sliced_list))

for company in company_dict
  print company_name+": "+average_price

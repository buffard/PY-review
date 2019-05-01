# ticker symbols and company names
stockDict = { 
  'GM': 'General Motors',
  'CAT':'Caterpillar', 
  'EK':"Eastman Kodak" 
  }

# ticker symbols, number of shares, dates and price
purchases = [ 
  ( 'GM', 100, '10-sep-2001', 48 ),
  ( 'CAT', 100, '1-apr-1999', 24 ),
  ( 'GM', 200, '1-jul-1998', 56 ), 
  ( 'EK', 50, '2-jun-2005', 10 ) 
  ]

# Create a purchase history report that computes the full purchase price (shares times dollars) for each block of stock and uses the stockDict to look up the full company name. This is the basic relational database join algorithm between two tables.

for ticker, shares, date, price in purchases:
  shareValue = price * shares
  for tickSym, name in stockDict.items():
    if tickSym == ticker:
      ticker = name

  print("I purchased %s stock for $%d" %(ticker, shareValue))

  # Create a second purchase summary that which accumulates total investment by ticker symbol. In the above sample data, there are two blocks of GE. These can easily be combined by creating a dict where the key is the ticker and the value is the list of blocks purchased. The program makes one pass through the data to create the dict. A pass through the dict can then create a report showing each ticker symbol and all blocks of stock.
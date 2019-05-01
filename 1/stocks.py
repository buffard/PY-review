# ticker symbols and company names
stockDict = { 
  'GM': 'General Motors',
  'CAT':'Caterpillar', 
  'EK':"Eastman Kodak" 
  }

# ticker symbols, number of shares, dates and price
purchases = [ 
  ( 'GE', 100, '10-sep-2001', 48 ),
  ( 'CAT', 100, '1-apr-1999', 24 ),
  ( 'GE', 200, '1-jul-1998', 56 ) 
  ]

# Create a purchase history report that computes the full purchase price (shares times dollars) for each block of stock and uses the stockDict to look up the full company name. This is the basic relational database join algorithm between two tables.

for ticker, shares, date, price in purchases:
  shareValue = price * shares
  print("I purchased %s stock for $%d" %(ticker, shareValue))
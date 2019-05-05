showroom = set()
showroom.update(['tesla', 'VW Bus', 'Scion Xb', 'Woody'])
print('Showroom length:', len(showroom))
showroom.add('VW Bus')
print('Showroom', showroom)
showroom.update(['WRX', 'GTI'])
print('Showroom', showroom)
showroom.discard('WRX')
print('Showroom', showroom)

# Now create another set of cars in a variable junkyard. Someone who owns a junkyard full of old cars has approached you about buying the entire inventory. In the new set, add some different cars, but also add a few that are the same as in the showroom set.

junkyard = set()
junkyard.update(['Mazda', 'Lebaron', 'tesla', 'Scion Xb'])

# Use the intersection method to see which cars exist in both the showroom and that junkyard.
print("Double Inventory:", showroom.intersection(junkyard))

# Now you're ready to buy the cars in the junkyard. Use the union method to combine the junkyard into your showroom.
showroom = showroom.union(junkyard)
print("Full Inventory:", showroom)

# Use the discard() method to remove any cars that you acquired from the junkyard that you want in your showroom.
showroom.discard('Mazda')
print("Full Inventory:", showroom)
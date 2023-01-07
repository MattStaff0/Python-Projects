'''Hello Again Pyhton, Part 2
Author:Matthew Stafford, C. Science
Credit: None
Description: Calculate number of watermelons needed for reunion'''



# Section A finding how many watermelons to buy

# Initialize variables with values
ttl_ppl = 50
ttl_child = 15
ttl_adults = 35
melon_slices = 10

# Calculate number of watermelon slices needed
adult_slices = 2 * ttl_adults
child_slices = 3 * ttl_child * 1.1 # getting 10 percent more for children
ttl_slices = adult_slices + child_slices
print("Total slices needed:", ttl_slices)
print("Adult slices needed:", adult_slices)
print("Child slices needed:", child_slices)

# Calculate number of watermelons needed (this may be a float) # Round the number of watermelonsr
melons_needed = round(ttl_slices / 10)


# Report total number of watermelons to buy
print('Total watermelons to buy:', melons_needed)


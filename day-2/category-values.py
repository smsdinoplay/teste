"""
Category Values
"""
# create mixed list
myMixedTypeList = [45, 290578, 1.02, True, "My dog is on the bed.", "45"]

#print(myMixedTypeList[0])

# loop with for
for item in myMixedTypeList:
    value_index = myMixedTypeList.index(item)
    print('Index: {}'.format(value_index))
    print('Valor: {}'.format(myMixedTypeList[value_index]))
    
    #print("{} is of the data type {}".format(item,type(item)))

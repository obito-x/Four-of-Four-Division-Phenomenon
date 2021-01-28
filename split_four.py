# All Possible Fourty divisions Caculation


from split_two import split_two as sptwo
import json


fourty_sptwo_generator = iter(sptwo(40))
first_place = next(fourty_sptwo_generator) # 39 + 1 cannot included

dataFile = open('fourty_division_data.json', 'w')
dataList = [] 


for x, y in fourty_sptwo_generator:
	# Caculate all possible value from both side
    for fsp_x,fsp_y in sptwo(x): # fsp = earlier two digit
        for bsp_x, bsp_y in sptwo(y): # bsp = later two digit
            data = [fsp_x, fsp_y, bsp_x, bsp_y]
            data.sort(reverse=True)
            # [Data Repeation Error Fixed]
            if data not in dataList:
            	dataList.append(data)
            	print(data)


# Output to Json Data
json.dump(dataList, dataFile, indent=2)
print("Total possibility: " + str(len(dataList)))
dataFile.close()

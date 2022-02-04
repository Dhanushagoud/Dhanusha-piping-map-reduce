
import sys 

# iterate through each line provided via standard input
for line in sys.stdin:
  datalist = line.strip().split(",")
  if (len(datalist) == 16) : 
    manufacturer,model,salesThousands,yearResaleValue,vehicleType,priceInThousands,engineSize,horsepower,wheelbase,width,length,curbWeight,fuelCapacity,fuelEfficiency,latestLaunch,powerFactor = datalist

    # print intermediate key-value pairs to standard output
    print(manufacturer,"\t",priceInThousands)
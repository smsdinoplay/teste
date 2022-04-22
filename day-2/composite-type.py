"""
Composite Type
"""

# import libs
import csv
import copy

# create dictionary
myVehicle = {
    "vin" : "<empty>",
    "make" : "<empty>" ,
    "model" : "<empty>" ,
    "year" : 0,
    "range" : 0,
    "topSpeed" : 0,
    "zeroSixty" : 0.0,
    "mileage" : 0
}

# loop
# for key, value in myVehicle.items():
#     print("{} : {}".format(key,value))
    


# create empty list
myInventoryList = []


# read csv file
with open('car_fleet.csv') as csvFile:
    
    # ler arquivo e separar os dados
    csvReader = csv.reader(csvFile, delimiter=',')
    
    # variavel de controle
    lineCount = 0  
    
    # repeticao
    for row in csvReader:
        
        # primeira linha do arquivo (nome das colunas)
        if lineCount == 0:
            
            # f-string - interpolação de expressões
            print(f'Column names are: {", ".join(row)}')
            
            # implementar contador de voltas (loop)
            lineCount += 1  
        else:  
            #print(f'vin: {row[0]} make: {row[1]}, model: {row[2]}, year: {row[3]}, range: {row[4]}, topSpeed: {row[5]}, zeroSixty: {row[6]}, mileage: {row[7]}')
            
            print(
                f'vin: {row[0]}\n'
                f'make: {row[1]}\n'
                f'make: {row[1]}\n'
                f'model: {row[2]}\n'
                f'year: {row[3]}\n'
                f'range: {row[4]}\n'
                f'topSpeed: {row[5]}\n'
                f'zeroSixty: {row[6]}\n' 
                f'mileage: {row[7]}\n'
            )
            
            # criar copia do dado lido
            currentVehicle = copy.deepcopy(myVehicle) 
            
            # acessar posicoes da lista e atribuir
            currentVehicle["vin"] = row[0]  
            currentVehicle["make"] = row[1]  
            currentVehicle["model"] = row[2]  
            currentVehicle["year"] = row[3]  
            currentVehicle["range"] = row[4]  
            currentVehicle["topSpeed"] = row[5]  
            currentVehicle["zeroSixty"] = row[6]  
            currentVehicle["mileage"] = row[7]
            
            # adicionar o dado lido a lista
            myInventoryList.append(currentVehicle)
            
            # implementar contador de voltas (loop)
            lineCount += 1
            
    print(f'Processed {lineCount} lines.')


# mostrar inventario
print('---- my inventory ----')

# loop
for myCarProperties in myInventoryList:
    # return dictionary
    #print(myCarProperties)
    
    # return tuples pairs
    for key, value in myCarProperties.items():
        print("{} : {}".format(key,value))
        print("-----")
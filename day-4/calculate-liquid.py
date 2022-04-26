# store the human preproinsulin sequence in a variable called preproinsulin:
preproInsulin = "malwmrllpllallalwgpdpaaafvnqhlcgshlvealylvcgergffytpktrreaedlqvgqvelgggpgagslqplalegslqkrgiveqcctsicslyqlenycn"

# store the remaining sequence elements of human insulin in variables:
lsInsulin = "malwmrllpllallalwgpdpaaa"
bInsulin = "fvnqhlcgshlvealylvcgergffytpkt"
aInsulin = "giveqcctsicslyqlenycn"
cInsulin = "rreaedlqvgqvelgggpgagslqplalegslqkr"

# concatenar
insulin = bInsulin + aInsulin

#print("--- Sequencia de insulina ---")
#print(insulin)

# Store AA pKR values and N/C-terms in dictionaries:
pKR = {'y':10.07,'c': 8.18,'k':10.53,'h':6.00,'r':12.48,'d':3.65,'e':4.25}


## Count the occurrence of each pKR AA in the sequence, and append N/C-terms:
seqCount = ({x: float(insulin.count(x)) for x in ['y','c','k','h','r','d','e']})

#print("\n--- Contagem de ocorrencias ---")
#print(seqCount)


## Compute the net charge according to the Henderson-Hesselbach equation:
pH = 0

while (pH <= 14):
    
    # equacao de Henderson-Hesselbach
    netCharge = (
        +(sum({x: ((seqCount[x]*(10**pKR[x]))/((10**pH)+(10**pKR[x]))) for x in ['k','h','r']}.values()))
        -(sum({x: ((seqCount[x]*(10**pH))/((10**pH)+(10**pKR[x]))) for x in ['y','c','d','e']}.values()))
    )
    
    # mostrar o valor formatado
    print ('{0:.2f}'.format(pH), netCharge)
    
    # incrementa variavel de controle
    pH = pH + 1

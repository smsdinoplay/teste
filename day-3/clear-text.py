import re

# abrir e ler o arquivo
with open('day-3/preproinsulin-seq.txt') as f:
    insulinFile = f.read()
    
# mostrar dado original
print('--- DADO ORIGINAL ---')
print(insulinFile)


# funcao para limpar o dado
def clean_text(string):
    
    # regex remover numeros
    string = re.sub(r"\d+", "", string)
    
    # regex remover espacos em branco
    string = re.sub(r"\s", "", string)

    string = string.replace("ORIGIN", "")
    string = string.replace("//", "")
        
    #string = string.replace("61", "")
    #tring = string.replace("1", "")

    string = string.replace(" ", "")
    
    string = string.replace("\r", "")
    
    # remove breaklines
    string = string.replace("\n", "")
    
    # remove stripes (*) string
    string = string.strip().lower()

    return string 
    
# variavel para guardar o dado limpo
cleanInsulin = clean_text(insulinFile)

# mostrar dado limpo
print('\n--- DADO LIMPO ---')
print(cleanInsulin)


# contagem de caracteres
print('\n--- CONTAGEM DE CARACTERES ---')
print('Quantidade de caracteres: {}'.format(len(cleanInsulin)))


# dividir a string
print('\n--- DADOS CLASSIFICADOS ---')
print(f'LS: { cleanInsulin[0:24] }')
print(f'B: {cleanInsulin[25:54]}')
print(f'C: {cleanInsulin[55:89]}')
print(f'A: {cleanInsulin[90:110]}')
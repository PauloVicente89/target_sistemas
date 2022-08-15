# palavra a ser revertida
str = input("Palavra a ser revertida: ")

# Pegando length (tamanho) da palavra
tamanho_str = len(str)

# Não e uma função para inverter string como a reversed() por exemplo
# Portando aqui pegamos o tamanho da palavra e colocamos o indice de traz pra frente
sliced_str = str[tamanho_str::-1] 
print (sliced_str)
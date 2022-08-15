# Inserindo numero a ser consultado
n = int(input('Inserir número para ver se ele faz parte da sequência de Fibonacci: '))

# Valores iniciais para criar a sequencia
u_1 = 1
u_2 = 1
# Contador
count = 0

# Lista onde vai ser adicionado os valores da sequencia
lista = [0,1,1]

# RAange para soma dos valores
for vic in range(0, n):
    count = u_1 + u_2
    u_1 = count
    u_2 = (count - u_2)
    lista.append(count)

# Condição se o número existir ou não
if n in lista:
    print("[+] Número encontrado na sequência")
else:
    print("[-] Número fora da sequência")  
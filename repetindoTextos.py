# Solicita uma string e um número inteiro do usuário
texto = input("Digite uma string: ")
numero = int(input("Digite um número inteiro: "))

# Repete a string com espaços entre as repetições
resultado = (texto + " ") * numero

# Remove o espaço extra no final e exibe o resultado
print("Resultado:", resultado.strip())
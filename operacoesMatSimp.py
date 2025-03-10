#Vamos solicitar como entrada dois números e depois vamos realizar uma operação simples entre eles.

nun1 = int(input("Digite o primeiro numero:"))
nun2 = int(input("Digite o segundo numero:"))

sinal = input("Qaul expressao matematica vc deseja usar( + , - , * , / ): ")

if (sinal == "+"):
    resultado = nun1 + nun2
elif (sinal == "-"):
    resultado = abs(nun1 - nun2)
elif (sinal == "*"):
    resultado = nun1 * nun2
elif (sinal == "/"):
    resultado = nun1 / nun2
else:
    print("Sinal invalido!")

print(resultado)

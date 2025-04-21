name = input("Digite o seu nome: ")
print(f"Olá {name}. Vamos escolher comprar o seu ingresso")
age = int(input("Qual a sua idade? "))
ticket = 0

if age < 12:
    ticket += 5

elif age >= 12 and age < 18:
    ticket += 10

elif age >= 18 and age < 65:
    estudos = input("Você estuda? Sim (s) ou Não (n) ").lower().strip()
    if estudos == "s":
        ticket += 10
    else:
        ticket += 20

elif age >= 65:
    ticket += 0

else:
    print("Informe a sua idade!")

pipoca = input(
    "Você deseja adicionar combo de pipoca no seu ingresso? \n"
    "1 - Pipoca e bebida grande  \n"
    "2 - Pipoca e bebida média  \n"
    "3 - Apenas pipoca grande  \n"
    "4 - Apenas pipoca média  \n"
).strip()

if pipoca == "1":
    ticket += 35
elif pipoca == "2":
    ticket += 25
elif pipoca == "3":
    ticket += 18
elif pipoca == "4":
    ticket += 10
else:
    print("Não quer combo de pipoca")

chocolate = input("Deseja incluir uma barra de chocolate no seu combo? Sim (s) ou Não (n) ").lower().strip()

if chocolate == "s":
    ticket += 5

# Resultado final
print(f"\n{name}, o valor total do seu ingresso ficou em R${ticket}.")
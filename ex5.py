def inverter_string(string):
    invertida = ""
    for i in range(len(string) - 1, -1, -1):
        invertida += string[i] 
    return invertida


entrada = input("Digite uma string para inverter: ")


resultado = inverter_string(entrada)


print(f"String invertida: {resultado}")
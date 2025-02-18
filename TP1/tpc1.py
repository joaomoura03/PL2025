texto = "Hoje, 7 de Fevereiro de 2025, o professor de Processamento de Linguagens deu-nos este trabalho para fazer.=OfF E deu-nos 7=On dias para o fazer... Cada trabalho destes vale 0.25 valores da nota final!"

def tpc1(texto):
    somatorio = 0
    num_atual = ""
    estado = "ON"
    for i, char in enumerate(texto):
        if char.isdigit():
            num_atual += char
        else:
            if num_atual:
                if estado == "ON":
                    somatorio += int(num_atual)
                num_atual = ""
            if texto[i:i+2].lower() == "on":
                estado = "ON"
            elif texto[i:i+3].lower() == "off":
                estado = "OFF"
            if char == "=":
                print(somatorio)
    if num_atual and estado == "ON":
        somatorio += int(num_atual)
    print(somatorio)

if __name__ == "__main__":
    tpc1(texto)
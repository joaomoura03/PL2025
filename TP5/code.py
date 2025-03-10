import ply.lex as lex
import json
import re
from datetime import date
from prettytable import PrettyTable
import sys

tokens = (
    "LISTAR",
    "MOEDA",
    "SELECIONAR",
    "SALDO",
    "SAIR"    
)

saldoMachine = 0


def printTable(data):
    header = ["Código", "Nome", "Quantidade", "Preço"]
    items = []
    for value in data:
        code = value["cod"]
        name = value["nome"]
        quantity = value["quant"]
        price = str(value["preco"]) + "€"
        
        if quantity > 0:
            items.append([code, name, quantity, price])
    table = PrettyTable(header)
    for item in items:
        table.add_row(item)
    print(table)    


def calcularTroco():
    coins = {"2e": 200, "1e": 100, "50c": 50, "20c": 20, "10c": 10, "5c": 5, "2c": 2, "1c": 1}
    global saldoMachine
    saldoCent = saldoMachine * 100
    trocoStr = ""
    for coin, value in sorted(coins.items(), key=lambda item: item[1], reverse=True):
        count = saldoCent // value
        if count > 0:
            saldoCent -= count * value
            trocoStr += f"{count}x {coin}, "
    
    trocoStr = trocoStr.rstrip(", ")
    trocoStr += "."
    return trocoStr
        

def calcularSaldo():
    global saldoMachine
    saldoToStr = ""
    if len(str(saldoMachine)) > 1:
        if str(saldoMachine).split(".")[1] == "0":
            saldoToStr = str(saldoMachine).split(".")[0] + 'e'
        elif len(str(saldoMachine).split(".")[1]) == 1:
            saldoToStr = str(saldoMachine).split(".")[0] + 'e' + str(saldoMachine).split(".")[1] + '0c'
        else:
            saldoToStr = str(saldoMachine).split(".")[0] + 'e' + str(saldoMachine).split(".")[1] + 'c'
    else:
        if saldoMachine != 0:
            saldoToStr = str(saldoMachine) + 'e'
    return saldoToStr   


def t_LISTAR(t):
    r'LISTAR'
    stock = t.lexer.stock
    print("maq:")
    printTable(stock)
    return t


def t_MOEDA(t):
    r'MOEDA.+'
    global saldoMachine
    moedas = re.findall(r'(1e|2e|50c|20c|10c|5c|2c|1c)', t.value)
    for moeda in moedas:
        if moeda == "1e":
            saldoMachine += 1
        elif moeda == "2e":
            saldoMachine += 2
        elif moeda == "50c":
            saldoMachine += 0.50
        elif moeda == "20c":
            saldoMachine += 0.20
        elif moeda == "10c":
            saldoMachine += 0.10
        elif moeda == "5c":
            saldoMachine += 0.05
        elif moeda == "2c":
            saldoMachine += 0.02
        elif moeda == "1c":
            saldoMachine += 0.01
    saldoToStr = calcularSaldo()
    print(f"maq: Saldo = {saldoToStr}")
    return t


def t_SELECIONAR(t):
    r'SELECIONAR\s[A-Z]{1}[0-9]+'
    global saldoMachine
    itemID = re.match(r'SELECIONAR ([A-Z]{1}[0-9]+)', t.value).group(1)
    stock = t.lexer.stock
    item = None
    for artigo in stock:
        if artigo["cod"] == itemID:
            item = artigo
            break
    if item == None:
        print(f"maq: Não existe o item \"{itemID}\" na maquina.")
        return t
    else:
        if item["quant"] == 0:
            print(f"maq: Não tem stock do item \"{itemID}\".")
            return t
        else:
            itemPrice = item["preco"]
            if itemPrice > saldoMachine:
                print(f"maq: Não tem saldo suficiente para comprar o item {itemID}.")
                print(f"maq: Saldo = {calcularSaldo()}; Pedido = {itemPrice}")
            else:
                item["quant"] -= 1
                saldoMachine -= itemPrice
                saldoMachine = round(saldoMachine, 2)
                print(f"maq: Pode retirar o produto dispensado \"{item['nome']}\" .")   
                print(f"maq: Saldo = {calcularSaldo()}")
                file = open("stock.json", "w")
                json.dump({"stock": stock}, file)
            

def t_SALDO(t):
    r'SALDO'
    saldoToStr = calcularSaldo()
    if saldoToStr == "":
        print("maq: Saldo = 0e")
    else:
        print(f"maq: Saldo = {saldoToStr}")
    return t
    

def t_SAIR(t):
    r'SAIR'
    trocoToString = calcularTroco()
    if trocoToString == ".":
        print("maq: Não tem troco a devolver. Até à próxima.")
    else:     
        print(f"maq: Pode retirar o troco: {trocoToString}")
        print("maq: Até à próxima.")
    sys.exit()

        
def main():
    print(f"\nmaq: {date.today()}, Stock carregado, Estado atualizado.")
    print("maq: Bom dia. Estou disponível para atender o seu pedido.")
    lexer = lex.lex()
    while True:
        try:
            with open("stock.json", "r") as file:
                stock = json.load(file)
                lexer.stock = stock['stock']
            inputText = input(">> ")
            lexer.input(inputText)
            toke = lexer.token()
        except EOFError:
            break


t_ignore = " \t"


def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)


def t_error(t):   
    print(f"maq: Comando inválido: {t}")
    t.lexer.skip(1000)


if "__main__" == __name__:
    main()        
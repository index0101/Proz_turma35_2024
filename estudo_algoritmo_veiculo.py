# VeÍculos:

def categoria_habilitacao(rodas, peso_bruto, pessoas):
    if rodas in [2, 3]:
        return "A: Veículos com duas ou três rodas"
    elif rodas == 4 and pessoas <= 8 and peso_bruto <= 3500:
        return "B: Veículos com quatro rodas, que acomodam até oito pessoas e seu peso é de até 3500 kg"
    elif rodas >= 4 and 3500 < peso_bruto <= 6000:
        return "C: Veículos com quatro rodas ou mais e com peso entre 3500 e 6000 kg"
    elif rodas >= 4 and pessoas > 8:
        return "D: Veículos com quatro rodas ou mais e que acomodam mais de oito pessoas"
    elif rodas >= 4 and peso_bruto > 6000:
        return "E: Veículos com quatro rodas ou mais e com mais de 6000 kg"
    else:
        return "Categoria não definida para as especificações fornecidas"

# Exemplo de uso:
rodas = int(input("Informe a quantidade de rodas: "))
peso_bruto = float(input("Informe o peso bruto em quilogramas: "))
pessoas = int(input("Informe a quantidade de pessoas no veículo: "))

categoria = categoria_habilitacao(rodas, peso_bruto, pessoas)
print(f"A categoria de habilitação necessária é: {categoria}")


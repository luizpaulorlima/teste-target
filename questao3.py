import json

def ler_faturamento_json(arquivo):
    with open(arquivo, 'r') as file:
        dados = json.load(file)  
    return [item['valor'] for item in dados if item['valor'] is not None and item['valor'] > 0]

def calcular_faturamento(dias_faturamento):
    if not dias_faturamento:
        return None, None, None

    menor_faturamento = min(dias_faturamento)
    maior_faturamento = max(dias_faturamento)
    media_mensal = sum(dias_faturamento) / len(dias_faturamento)
    dias_acima_media = sum(1 for faturamento in dias_faturamento if faturamento > media_mensal)

    return menor_faturamento, maior_faturamento, dias_acima_media

dias_faturamento = ler_faturamento_json('dados.json')

menor, maior, dias_acima_media = calcular_faturamento(dias_faturamento)

print(f"Menor valor de faturamento: R${menor:.2f}")
print(f"Maior valor de faturamento: R${maior:.2f}")
print(f"Número de dias com faturamento acima da média: {dias_acima_media}")

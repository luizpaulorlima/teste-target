import xml.etree.ElementTree as ET

def ler_faturamento_xml(arquivo):
    tree = ET.parse(arquivo)
    root = tree.getroot()
    return [
        float(row.find('valor').text) 
        for row in root.findall('row') 
        if row.find('valor') is not None and float(row.find('valor').text) > 0
    ]

def calcular_faturamento(dias_faturamento):
    if not dias_faturamento:
        return None, None, None
    menor_faturamento = min(dias_faturamento)
    maior_faturamento = max(dias_faturamento)
    media_mensal = sum(dias_faturamento) / len(dias_faturamento)
    dias_acima_media = sum(1 for faturamento in dias_faturamento if faturamento > media_mensal)
    return menor_faturamento, maior_faturamento, dias_acima_media

dias_faturamento = ler_faturamento_xml('dados.xml')
menor, maior, dias_acima_media = calcular_faturamento(dias_faturamento)

if menor is not None and maior is not None:
    print(f"Menor faturamento: R${menor:.2f}")
    print(f"Maior faturamento: R${maior:.2f}")
else:
    print("Erro ao calcular o menor ou maior valor de faturamento.")

print(f"Número de dias com faturamento acima da média: {dias_acima_media}")

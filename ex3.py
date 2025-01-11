import json

faturamento_json = '''
{
    "faturamento": [221, 0, 523, 415, 0, 0, 389, 0, 0, 350, 0, 
                    450, 0, 412, 0, 321, 0, 525, 612, 0, 
                    398, 502, 620, 0, 0, 550, 480, 0, 0, 300]
}
'''

dados = json.loads(faturamento_json)
faturamento = dados["faturamento"]

faturamento_validos = [valor for valor in faturamento if valor > 0]

menor_faturamento = min(faturamento_validos)
maior_faturamento = max(faturamento_validos)
media_mensal = sum(faturamento_validos) / len(faturamento_validos)
dias_acima_media = sum(1 for valor in faturamento_validos if valor > media_mensal)

print(f"Menor faturamento do mês: R$ {menor_faturamento:.2f}")
print(f"Maior faturamento do mês: R$ {maior_faturamento:.2f}")
print(f"Número de dias com faturamento acima da média mensal: {dias_acima_media}")
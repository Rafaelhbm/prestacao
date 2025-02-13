def valorPagamento(valor_prestacao, dias_atrasados):
    if dias_atrasados == 0:
        return valor_prestacao
    else:
        multa = valor_prestacao * 0.03
        juros = valor_prestacao * (dias_atrasados * 0.001)
        return  valor_prestacao + multa + juros

total_prestacoes = 0
valor_total = 0

while True:
    valor_prestacao = float(input("Informe o valor da prestação (ou 0 para sair): "))
    if valor_prestacao == 0:
        break
    dias_atrasados = int(input("Informe o número de dias em atraso: "))
    valor_pago = valorPagamento(valor_prestacao, dias_atrasados)
    print(f"Valor a ser pago: R$ {valor_pago:.2f}")
    total_prestacoes += 1
    valor_total += valor_pago

print(f"Relatório do dia:")
print(f"Quantidade de prestações pagas: {total_prestacoes}")
print(f"Valor total de prestações pagas: R$ {valor_total:.2f}")
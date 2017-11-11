
import os, sys

if(len(sys.argv) < 4):
    print('usage: python aportes_fixo <capital_inicial> <aportes_mensais> <taxa_mensal>')
    exit()

capital_inicial = float(sys.argv[1])
aportes_mensais = int(sys.argv[2])
taxa_mensal     = float(sys.argv[3])

taxa_mensal     = (taxa_mensal/100) if taxa_mensal >= 0 else 1

capital_investido = capital_inicial

valor_anual = capital_inicial

it = 40 # 40 anos
for it in range(1, 40 +1):
    print('============')
    print('Ano: %d' % it)

    valor_mensal = valor_anual
    for mes in range(1, 12 +1):
        capital_investido += aportes_mensais
        valor_mensal = (valor_mensal+aportes_mensais)*(1+taxa_mensal)
        # print('\tValor Mensal: %.2f' % valor_mensal )

    valor_anual = valor_mensal

    print('Aportes: %.2f' % aportes_mensais)
    print('Capital Investido: %d' % capital_investido)
    print('Valor Anual: %.2f' % valor_anual)
    print('Valor Anual - IR 15%%: %.2f' % (valor_anual*(1-0.15)))
    print('Valor Anual - IR 17,5%%: %.2f' % (valor_anual*(1-0.175)))
    if valor_anual*(1-0.15)/1000000 >= 1:
        print('\n#####\nMILHAO!\n')
    if valor_anual*(1-0.175)/1000000 >= 1:
        break

    aportes_mensais += aportes_mensais*0.05

# print('valor_final = ' + str(valor_anual))

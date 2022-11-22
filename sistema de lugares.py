colunas = 8
linhas = 5
valor = 0
reservado = []
pocco_bus = []

def opcoes():
    print("[1] - Ver assentos disponiveis:\n"
          "[2] - Comprar passagem:\n"
          "[3] - Gerar relatorio:\n"
          "[4] - Finalizar:\n")


# estrutura da matriz
def estrutura_matriz(pocco_bus):
    linhas = len(pocco_bus)
    colunas = len(pocco_bus[0])

    for i in range(linhas):
        for j in range(colunas):
            if pocco_bus[i][j] == 'M':
                print('\033[34m %s \033[m' % f'{pocco_bus[i][j]:^3}', end="")
            elif pocco_bus[i][j] == 'R':
                print('\033[31m %s \033[m' % f'{pocco_bus[i][j]:^3}', end="")
            elif pocco_bus[i][j] == 'C':
                print('\033[37m %s \033[m' % f'{pocco_bus[i][j]:^3}', end="")
            else:
                print('\033[32m %s \033[m' % f'{pocco_bus[i][j]:^3}', end="")
        print()


# Quantidade de assentos para venda.
def format_assentos(linhas, colunas, pocco_bus, valor):
    lista = []
    for i in range(linhas):
        for j in range(colunas):
            if i == 0 and j == 0:
                lista.append('M')
            elif i == 0 and j != 0:
                lista.append('C')
            elif j == 2:
                lista.append('C')
            else:
                valor += 1
                lista.append(valor)
        pocco_bus.append(lista[:])
        lista.clear()
    return pocco_bus


# Reserva de assentos.
def reservar(pocco_bus ,reservado):

    menu = True
    while menu:
        estrutura_matriz(pocco_bus)
        assento = int(input('\nSelecione um assento disponivel ou [0] para voltar ao menu de opções: ').replace('',''))
        if assento < 0 or assento > 28:
            print('\n\033[31mAssento inválido!\033[m Por favor digite algum assento que esteja disponivel.\n')
        elif assento == 0:
            print('\n\033[32mCompra finalizada!\033[m')
            print('==================================================================')
            break
        else:
            vendido = False
            if vendido == False and assento in reservado and len(reservado) != 0:
                print('\n\033[31mAssento ocupado!\033[m Por favor digite algum assento que esteja disponivel.\n')
            else:
                for disponiveis in range(len(pocco_bus)):
                    for z in pocco_bus[disponiveis]:
                        if assento == z and assento != 'R':
                            reservado.append(assento)
                            colunas = pocco_bus[disponiveis].index(z)
                            linhas = disponiveis
                            pocco_bus[linhas][colunas] = 'R'
                            resp = str(input('\n\033[32mCompra realizada com sucesso!\033[m\nDeseja comprar outra passagem? [S/N] ')).strip().lower()
                            while True:
                                if resp == 's':
                                    break
                                elif resp == 'n':
                                    menu = False
                                    print('\n\033[32mCompra finalizada!\033[m')
                                    print('==================================================================')
                                    break
                                else:
                                    resp = str(input('\n\033[31mOpção invalida!\033[m \nDeseja comprar outra passagem? [S/N] ')).lower()

                            vendido = True
                            if len(reservado) == 28 and resp in 'Ss':
                                print('\n\033[31mAssentos esgotados!\033[m\n')
                                break


# Gerando o relatorio em txt.
def gerar_relat(pocco_bus, reservado):
    with open('Relatorio.txt', 'w' ) as assento:
        assento.write('==================== Relatorio POCCOBUS ======================= \n')
        assento.write('Assentos ocupados: \n')
        for i in reservado:
            assento.write(f'Assento {i} - ocupado \n')
        assento.write('\n')
        assento.write('Assentos disponiveis: \n')
        for disponiveis in range(len(pocco_bus)):
            for z in pocco_bus[disponiveis]:
                if z != 'O' and z != 'C' and z != 'M' and z != 'R':
                    assento.write(f'Assento {z} - disponivel \n')
        assento.write('\n')
        assento.close()
    print('================================================================')
    print('\033[32mRelatório gerado com sucesso! \033[m')
    print('================================================================\n')


# Inicio do sistemas

format_assentos(colunas,linhas,pocco_bus,valor)
print(' ====================================================')
print('             Bem-vindo ao POCCOBUS                   ')
print(' ====================================================\n')

while True:
    opcoes()
    try:
        escolha = int(input('Escolha a opção desejada: ').replace(' ',' '))

        if escolha > 4 or escolha < 0:
            print('\n\033[31mOpção invalida!!!\033[m \n')

        elif escolha == 1:
            print('')
            estrutura_matriz(pocco_bus)
            print('')

        elif escolha == 2:
            print('')
            reservar(pocco_bus, reservado)
            print('')

        elif escolha == 3:
            print('')
            gerar_relat(pocco_bus, reservado)

        else:
            print('\nMuito obrigado por viajar com a POCCOBUS.')
            break

    except ValueError:
        print('\n\033[31mOpção invalida!!!\033[m \n')

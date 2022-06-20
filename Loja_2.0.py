import sqlite3
import datetime

dados_l = sqlite3.connect('Loja_2.0.db')
cursor = dados_l.cursor()
funcoes = ['Cadastro', 'Fora', 'Venda', 'Pedido', 'Deletar', 'Modificacao']
print('\033[1:30:42m Bem vindo ao SL2.0 feito por FJR \033[m')
funcao = int(input('Selecione uma função:\n'
                   'Cadastro[1]\n'
                   'Fora[2]\n'
                   'Vendas[3]\n'
                   'Pedido[4]\n'
                   'Deletar[5]\n'
                   'Modificar dados[6] \n'
                   '---['))
if funcao == 1:
    dados_l = sqlite3.connect('Loja_2.0.db')
    cursor = dados_l.cursor()
    print('\033[7:30:42m --> CADASTRO <--\033[m')
    cursor.execute("CREATE TABLE IF NOT EXISTS CADASTRO (Codigo integer ,Classe text , Observacao text , Estoque integer , "
                   "Preço integer ,  Status text )")
    dados_l.commit()
    codigo = int(input('\033[7:30:42m Insira codigo do produto \033[m'))
    classe = str(input('\033[7:30:42m Insira classe do produto \033[m')).strip().capitalize()
    observacao = str(input('\033[7:30:42m Insira observacao sobre o produto '
                           '\033[7:30:41m [OPCIONAL] \033[m')).strip().capitalize()
    if observacao == '':
        observacao = 'vazio'
    estoque = int(input('\033[7:30:42m Insira o numero de itens \033[m'))
    preco = int(input('\033[7:30:42m Insira o valor de compra \033[m'))
    status = str(input('\033[7:30:42m Insira o status [Vendido/Disponivel] \033[m'
                       '\033[7:30:41m [OPCIONAL] \033[m')).strip().capitalize()
    if status == '':
        status = 'Indefinido'
    q = str(input(f'CONFIRMAR [S/N] DADOS :\n'
                  f'Codigo: {codigo} \n'
                  f',Classe:{classe} \n'
                  f',Obervacao:{observacao} \n'
                  f',Estoque:{estoque} \n'
                  f',Preco:{preco} \n'
                  f'Status:{status} \n'
                  f'---['))
    if q in 'Nn':
        codigo = int(input('\033[7:30:42m Insira codigo do produto \033[m'))
        classe = str(input('\033[7:30:42m Insira classe do produto \033[m')).strip().capitalize()
        observacao = str(input('\033[7:30:42m Insira observacao sobre o produto '
                               '\033[7:30:41m [OPCIONAL] \033[m')).strip().capitalize()
        if observacao == '':
            observacao = 'vazio'
            estoque = int(input('\033[7:30:42m Insira o numero de itens \033[m'))
            preco = int(input('\033[7:30:42m Insira o valor de compra \033[m'))
            status = str(input('\033[7:30:42m Insira o status [Vendido/Disponivel] \033[m'
                               '\033[7:30:41m [OPCIONAL] \033[m')).strip().capitalize()
        if status == '':
            status = 'Indefinido'
        cursor.execute(
            "INSERT INTO  Cadastro VALUES (" + str(codigo) + ",'" + classe + "','" + observacao + "'," + str(
                estoque) + " ," + str(preco) + ",'" + status + "')")
        dados_l.commit()
    else:
        cursor.execute(
            "INSERT INTO  Cadastro VALUES (" + str(codigo) + ",'" + classe + "','" + observacao + "'," + str(
                estoque) + " ," + str(preco) + ",'" + status + "')")
        dados_l.commit()
if funcao == 2:
    dados_l = sqlite3.connect('Loja_2.0.db')
    cursor = dados_l.cursor()
    print('\033[7:30:42m --> FORA <--\033[m')
    cursor.execute("CREATE TABLE IF NOT EXISTS FORA (Codigo integer ,Classe text , Observacao text , Cliente text , "
                   "Data text, Numero do cliente integer )")
    dados_l.commit()
    codigo = int(input('\033[7:30:42m Insira codigo do produto \033[m'))
    classe = str(input('\033[7:30:42m Insira classe do produto \033[m')).strip().capitalize()
    observacao = str(input('\033[7:30:42m Insira observacao sobre o produto \033[m'
                           '\033[7:30:41m [OPCIONAL] \033[m')).strip().capitalize()
    if observacao == '':
        observacao = 'vazio'
    cliente = str(input('\033[7:30:42m Insira cliente \033[m')).strip().capitalize()
    data = datetime.datetime.today()
    celular_cliente = int(input('\033[7:30:42m Insira numero do cliente[DDD[NUM-ERO]] \033[m'))
    q = str(input(f'CONFIRMAR [S/N] DADOS :\n'
                  f'Codigo: {codigo}\n'
                  f',Classe:{classe}\n'
                  f',Obervacao:{observacao}\n'
                  f',Cliente:{cliente}\n'
                  f',Preco:{data}\n'
                  f'Numero do cliente:{celular_cliente}\n'
                  f'---['))
    if q in 'Nn':
        codigo = int(input('\033[7:30:42m Insira codigo do produto \033[m'))
        classe = str(input('\033[7:30:42m Insira classe do produto \033[m')).strip().capitalize()
        observacao = str(input('\033[7:30:42m Insira observacao sobre o produto \033[m'
                               '\033[7:30:41m [OPCIONAL] \033[m')).strip().capitalize()
        if observacao == '':
            observacao = 'vazio'
        cliente = str(input('\033[7:30:42m Insira cliente \033[m')).strip().capitalize()
        data = datetime.datetime.today()
        cursor.execute(
            "INSERT INTO  FORA VALUES (" + str(
                codigo) + ",'" + classe + "','" + observacao + "','" + cliente + "','" + str(data) + "'," + str(
                celular_cliente) + ")")
        dados_l.commit()
    else:
        cursor.execute(
            "INSERT INTO  FORA VALUES (" + str(
                codigo) + ",'" + classe + "','" + observacao + "','" + cliente + "' ,'" + str(data) + "'," + str(
                celular_cliente) + ")")
        dados_l.commit()
if funcao == 3:
    dados_l = sqlite3.connect('Loja_2.0.db')
    cursor = dados_l.cursor()
    print('\033[7:30:42m --> VENDA <-- \033[m')
    cursor.execute("CREATE TABLE IF NOT EXISTS VENDA (Codigo integer ,Classe text , Observacao text , Estoque integer, "
                   "Vendedor text,  Cliente text , Preco integer)")
    dados_l.commit()
    codigo = int(input('\033[7:30:42m Insira codigo do produto \033[m'))
    classe = str(input('\033[7:30:42m Insira classe do produto \033[m')).strip().capitalize()
    observacao = str(input('\033[7:30:42m Insira observacao sobre o produto \033[m'
                           '\033[7:30:41m [OPCIONAL] \033[m')).strip().capitalize()
    if observacao == '':
        observacao = 'vazio'
    estoque = int(input('\033[7:30:42m Insira o numero de itens \033[m'))
    vendedor = str(input('\033[7:30:42m Insira o vendedor \033[m')).strip().capitalize()
    cliente = str(input('\033[7:30:42m Insira o cliente \033[m')).strip().capitalize()
    preco = int(input('\033[7:30:42m Insira o preço de venda \033[m'))
    codigo_cadastro = cursor.execute("SELECT Codigo FROM CADASTRO").fetchall()
    codigo_venda = cursor.execute("SELECT Codigo FROM VENDA").fetchall()
    if codigo_cadastro == codigo_venda:
        cursor.execute("UPDATE CADASTRO SET Status = 'Vendido' WHERE '"+str(codigo_cadastro) + "'")
    q = str(input(f'CONFIRMAR [S/N] DADOS :\n'
                  f'Codigo: {codigo}\n'
                  f',Classe:{classe}\n'
                  f',Obervacao:{observacao}\n'
                  f',Estoque:{estoque}\n'
                  f',Vendedor:{vendedor}\n'
                  f' Cliente:{cliente}\n'
                  f'Preço:{preco}\n'
                  f'---['))
    if q in 'Nn':
        codigo = int(input('\033[7:30:42m Insira codigo do produto \033[m'))
        classe = str(input('\033[7:30:42m Insira classe do produto \033[m')).strip().capitalize()
        observacao = str(input('\033[7:30:42m Insira observacao sobre o produto \033[m'
                               '\033[7:30:41m [OPCIONAL] \033[m')).strip().capitalize()
        if observacao == '':
            observacao = 'vazio'
        estoque = int(input('\033[7:30:42m Insira o numero de itens \033[m'))
        vendedor = str(input('\033[7:30:42m Insira o vendedor \033[m')).strip().capitalize()
        cliente = str(input('\033[7:30:42m Insira o cliente \033[m')).strip().capitalize()
        preco = int(input('\033[7:30:42m Insira o preço de venda \033[m'))
        cursor.execute(
            "INSERT INTO  VENDA VALUES (" + str(
                codigo) + ",'" + classe + "','" + observacao + "',," + str(
                estoque) + ",'" + vendedor + "','" + cliente + "'," + str(preco) + ")")
        dados_l.commit()
    else:
        cursor.execute(
            "INSERT INTO  VENDA VALUES (" + str(
                codigo) + ",'" + classe + "','" + observacao + "'," + str(
                estoque) + ",'" + vendedor + "','" + cliente + "'," + str(preco) + ")")
        dados_l.commit()
if funcao == 4:
    dados_l = sqlite3.connect('Loja_2.0.db')
    cursor = dados_l.cursor()
    print('\033[7:30:42m --> PEDIDO <-- \033[m')
    cursor.execute("CREATE TABLE IF NOT EXISTS PEDIDO ( Codigo integer , Classe text , Observacao text  ,  Cliente text , Valor de compra integer) ")
    codigo = int(input('\033[7:30:42m Insira codigo do produto \033[m'))
    classe = str(input('\033[7:30:42m Insira classe do produto \033[m')).strip().capitalize()
    observacao = str(input('\033[7:30:42m Insira observacao sobre o produto \033[m'
                           '\033[7:30:41m [OPCIONAL] \033[m')).strip().capitalize()
    if observacao == '':
        observacao = 'vazio'
    cliente = str(input('\033[7:30:42m Insira o cliente \033[m')).strip().capitalize()
    preco = int(input('\033[7:30:42m Insira o preço de venda \033[m'))
    q = str(input(f'CONFIRMAR [S/N] DADOS :\n'
                  f'Codigo:{codigo} \n'
                  f',Classe:{classe} \n'
                  f',Obervacao:{observacao} \n'
                  f',Cliente:{cliente} \n'
                  f',Preço:{preco} \n'
                  f'---['))
    if q in 'Nn':
        codigo = int(input('\033[7:30:42m Insira codigo do produto \033[m'))
        classe = str(input('\033[7:30:42m Insira classe do produto \033[m')).strip().capitalize()
        observacao = str(input('\033[7:30:42m Insira observacao sobre o produto \033[m'
                               '\033[7:30:41m [OPCIONAL] \033[m')).strip().capitalize()
        if observacao == '':
            observacao = 'vazio'
        cliente = str(input('\033[7:30:42m Insira o cliente \033[m')).strip().capitalize()
        preco = int(input('\033[7:30:42m Insira o preço de venda \033[m'))
        cursor.execute(
            "INSERT INTO  PEDIDO VALUES (" + str(
                codigo) + ",'" + classe + "','" + observacao + "','" + cliente + "'," + str(preco) + ")")
        dados_l.commit()
    else:
        cursor.execute(
            "INSERT INTO  PEDIDO VALUES (" + str(
                codigo) + ",'" + classe + "','" + observacao + "','" + cliente + "'," + str(preco) + ")")
        dados_l.commit()
if funcao == 5:
    dados_l = sqlite3.connect('Loja_2.0.db')
    cursor = dados_l.cursor()
    print('\033[7:30:42m --> DELETAR DADOS   <-- \033[m')
    variaveis_cadastro = ['Codigo', 'Classe', 'Observacao',
                          'Estoque', 'Preço', 'Status']
    variaveis_fora = ['Codigo', 'Classe',
                      'Observacao', 'Cliente', 'Data', 'Numero']
    variaveis_pedido = ['Codigo', 'Classe', 'Observacao', 'Cliente', 'Valor']
    variaveis_venda = ['Codigo', 'Classe', 'Observacao',
                       'Estoque', 'Vendedor', 'Cliente', 'Preço']
    tabela = str(input('\033[7:30:42mSelecione uma tabela[Cadastro/Fora/Pedido/Venda]\033[m')).strip().capitalize()
    while tabela not in ['Cadastro', 'Fora', 'Pedido', 'Venda']:
        tabela = str(input('\033[7:30:42mSelecione uma tabela[Cadastro/Fora/Pedido/Venda]\033[m')).strip().capitalize()
    if tabela == 'Cadastro':
        print(variaveis_cadastro)
        coluna = str(input('\033[7:30:42m Insira coluna \033[m')).capitalize().strip()
        if coluna == 'Codigo':
            valor_velho = int(input('\033[7:30:42m Insira codigo que sera deletado\033[m'))
            print(f' \033[7:30:42m {coluna} {valor_velho} -- > Deletado \033[m')
            cursor.execute(
                "DELETE  from CADASTRO  WHERE Codigo = " + str(valor_velho) + " ")
            dados_l.commit()
        if coluna == 'Estoque':
            valor_velho = int(input('\033[7:30:42m Insira estoque que sera deletado\033[m'))
            print(f' \033[7:30:42m {coluna} {valor_velho} -- > Deletado \033[m')
            cursor.execute(
                "DELETE  from CADASTRO  WHERE Estoque = " + str(valor_velho) + " ")
            dados_l.commit()
        if coluna == 'Preço':
            valor_velho = int(input('\033[7:30:42m Insira preço que sera deletado\033[m'))
            print(f' \033[7:30:42m {coluna} {valor_velho} -- > Deletado \033[m')
            cursor.execute(
                "DELETE  from CADASTRO  WHERE Preço = " + str(valor_velho) + " ")
            dados_l.commit()
        if coluna == 'Classe':
            valor_velho = str(input('\033[7:30:42m Insira classe que sera deletado \033[m'))
            print(f' \033[7:30:42m {coluna} {valor_velho} -- > Deletado \033[m')
            cursor.execute(
                "DELETE from  CADASTRO  WHERE Classe = '" + valor_velho + "' ")
            dados_l.commit()
        if coluna == 'Observacao':
            valor_velho = str(input('\033[7:30:42m Insira observacao que sera deletado \033[m'))
            print(f' \033[7:30:42m {coluna} {valor_velho} -- > Deletado \033[m')
            cursor.execute(
                "DELETE from CADASTRO  WHERE Observacao = '" + valor_velho + "' ")
            dados_l.commit()
        if coluna == 'Status':
            valor_velho = str(input('\033[7:30:42m Insira status que sera deletado \033[m'))
            print(f' \033[7:30:42m {coluna} {valor_velho} -- > Deletado \033[m')
            cursor.execute("DELETE from CADASTRO  WHERE Status = '" + valor_velho + "' ")
            dados_l.commit()
    if tabela == 'Fora':
        print(variaveis_fora)
        coluna = str(input('\033[7:30:42m Insira coluna \033[m')).capitalize().strip()
        if coluna == 'Codigo':
            valor_velho = int(input('\033[7:30:42m Insira codigo que sera deletado \033[m'))
            print(f' \033[7:30:42m {coluna} {valor_velho} -- > Deletado \033[m')
            cursor.execute(
                "DELETE  from FORA  WHERE Codigo = " + str(valor_velho) + " ")
            dados_l.commit()
        if coluna == 'Classe':
            valor_velho = str(input('\033[7:30:42m Insira classe que sera deletado \033[m'))
            print(f' \033[7:30:42m {coluna} {valor_velho} -- > Deletado \033[m')
            cursor.execute(
                "DELETE  from FORA  WHERE Classe = '" + valor_velho + "' ")
            dados_l.commit()
        if coluna == 'Observacao':
            valor_velho = str(input('\033[7:30:42m Insira observacao que sera deletado \033[m'))
            print(f' \033[7:30:42m {coluna} {valor_velho} -- > Deletado \033[m')
            cursor.execute(
                "DELETE  from FORA  WHERE Observacao = '" + valor_velho + "' ")
            dados_l.commit()
        if coluna == 'Cliente':
            valor_velho = str(input('\033[7:30:42m Insira Cliente que sera deletado \033[m'))
            print(f' \033[7:30:42m {coluna} {valor_velho} -- > Deletado \033[m')
            cursor.execute(
                "DELETE  from FORA  WHERE Cliente = '" + valor_velho + "' ")
            dados_l.commit()
        if coluna == 'Classe':
            valor_velho = str(input('\033[7:30:42m Insira classe que sera deletado \033[m'))
            print(f' \033[7:30:42m {coluna} {valor_velho} -- > Deletado \033[m')
            cursor.execute(
                "DELETE  from FORA  WHERE Classe = '" + valor_velho + "' ")
            dados_l.commit()
        if coluna == 'Data':
            valor_velho = str(input('\033[7:30:42m Insira data que sera deletado \033[m'))
            print(f' \033[7:30:42m {coluna} {valor_velho} -- > Deletado \033[m')
            cursor.execute("DELETE  from FORA WHERE Data = '" + valor_velho + "' ")
            dados_l.commit()
        if coluna == 'Numero':
            valor_velho = str(input('\033[7:30:42m Insira numero que sera deletado \033[m'))
            print(f' \033[7:30:42m {coluna} {valor_velho} -- > Deletado \033[m')
            cursor.execute("DELETE from FORA  WHERE Numero = '" + valor_velho + "' ")
            dados_l.commit()
    if tabela == 'Pedido':
        print(variaveis_pedido)
        coluna = str(input('\033[7:30:42m Insira coluna \033[m')).capitalize().strip()
        if coluna == 'Codigo':
            valor_velho = int(input('\033[7:30:42m Insira codigo que sera deletado \033[m'))
            print(f' \033[7:30:42m {coluna} {valor_velho} -- > Deletado \033[m')
            cursor.execute(
                "DELETE from PEDIDO  WHERE Codigo = " + str(valor_velho) + " ")
            dados_l.commit()
        if coluna == 'Classe':
            valor_velho = str(input('\033[7:30:42m Insira classe que sera deletado \033[m'))
            print(f' \033[7:30:42m {coluna} {valor_velho} -- > Deletado \033[m')
            cursor.execute(
                "DELETE from PEDIDO  WHERE Classe = '" + valor_velho + "' ")
            dados_l.commit()
        if coluna == 'Observacao':
            valor_velho = str(input('\033[7:30:42m Insira observacao que sera deletada \033[m'))
            print(f' \033[7:30:42m {coluna} {valor_velho} -- > Deletado \033[m')
            cursor.execute(
                "DELETE from  PEDIDO  WHERE Observacao = '" + valor_velho + "' ")
            dados_l.commit()
        if coluna == 'Cliente':
            valor_velho = str(input('\033[7:30:42m Insira Cliente que sera deletado \033[m'))
            print(f' \033[7:30:42m {coluna} {valor_velho} -- > Deletado \033[m')
            cursor.execute(
                "DELETE  from PEDIDO  WHERE Cliente = '" + valor_velho + "' ")
            dados_l.commit()
        if coluna == 'Valor':
            valor_velho = int(input('\033[7:30:42m Insira Valor que sera deletado \033[m'))
            print(f' \033[7:30:42m {coluna} {valor_velho} -- > Deletado \033[m')
            cursor.execute(
                "DELETE  from PEDIDO  WHERE Valor = '" + str(valor_velho) + "' ")
            dados_l.commit()
    if tabela == 'Venda':
        print(variaveis_venda)
        coluna = str(input('\033[7:30:42m Insira coluna \033[m')).capitalize().strip()
        if coluna == 'Codigo':
            valor_velho = int(input('\033[7:30:42m Insira codigo que sera deletado \033[m'))
            print(f' \033[7:30:42m {coluna} {valor_velho} -- > Deletado \033[m')
            cursor.execute(
                "DELETE  from VENDA  WHERE Codigo = " + str(valor_velho) + " ")
            dados_l.commit()
        if coluna == 'Classe':
            valor_velho = str(input(' \033[7:30:42m Insira classe que sera deletado \033[m'))
            print(f' \033[7:30:42m {coluna} {valor_velho} -- > Deletado \033[m')
            cursor.execute(
                "DELETE from VENDA WHERE Classe = '" + valor_velho + "' ")
            dados_l.commit()
        if coluna == 'Observacao':
            valor_velho = str(input('\033[7:30:42m Insira observacao que sera deletado \033[m'))
            print(f' \033[7:30:42m {coluna} {valor_velho} -- > Deletado \033[m')
            cursor.execute("DELETE from  VENDA  WHERE Observacao = '" + valor_velho + "' ")
            dados_l.commit()
        if coluna == 'Estoque':
            valor_velho = int(input('\033[7:30:42m Insira estoque que sera deletado \033[m'))
            print(f' \033[7:30:42m {coluna} {valor_velho} -- > Deletado \033[m')
            cursor.execute(
                "DELETE from VENDA  WHERE Estoque = " + str(valor_velho) + " ")
            dados_l.commit()
        if coluna == 'Vendedor':
            valor_velho = str(input('\033[7:30:42m Insira vendedor que sera deletado \033[m'))
            print(f' \033[7:30:42m {coluna} {valor_velho} -- > Deletado \033[m')
            cursor.execute(
                "DELETE from VENDA  WHERE Vendedor = '" + valor_velho + "' ")
            dados_l.commit()
        if coluna == 'Cliente':
            valor_velho = str(input('\033[7:30:42m Insira Cliente que sera deletado \033[m'))
            print(f' \033[7:30:42m {coluna} {valor_velho} -- > Deletado \033[m')
            cursor.execute(
                "DELETE from  VENDA  WHERE Cliente = '" + valor_velho + "' ")
            dados_l.commit()
        if coluna == 'Preço':
            valor_velho = int(input('\033[7:30:42m Insira preço que sera deletado \033[m'))
            print(f' \033[7:30:42m {coluna} {valor_velho} -- > Deletado \033[m')
            cursor.execute(
                "DELETE  from VENDA  WHERE Preco = " + str(valor_velho) + " ")
            dados_l.commit()
if funcao == 6:
    dados_l = sqlite3.connect('Loja_2.0.db')
    cursor = dados_l.cursor()
    print('\033[7:30:42m --> MUDAR DADOS  <-- \033[m')
    variaveis_cadastro = ['Codigo', 'Classe', 'Observacao',
                          'Estoque', 'Preço', 'Status']
    variaveis_fora = ['Codigo', 'Classe',
                      'Observacao', 'Cliente', 'Data', 'Numero']
    variaveis_pedido = ['Codigo', 'Classe', 'Observacao', 'Cliente', 'Valor']
    variaveis_venda = ['Codigo', 'Classe', 'Observacao',
                       'Estoque', 'Vendedor', 'Cliente', 'Preço']
    tabela = str(input('\033[7:30:42mSelecione uma tabela[Cadastro/Fora/Pedido/Venda]\033[m')).strip().capitalize()
    while tabela not in ['Cadastro', 'Fora', 'Pedido', 'Venda']:
        tabela = str(input('\033[7:30:42mSelecione uma tabela[Cadastro/Fora/Pedido/Venda]\033[m')).strip().capitalize()
    if tabela == 'Cadastro':
        print(variaveis_cadastro)
        coluna = str(input('\033[7:30:42m Insira coluna \033[m')).capitalize().strip()
        if coluna == 'Codigo':
            valor_velho = int(input('\033[7:30:42m Insira codigo que sera substituido\033[m'))
            valor_novo = int(input('\033[7:30:42m Insira codigo que sera colocado \033[m'))
            print(f'\033[7:30:42m {coluna}{valor_velho} -- > {coluna}{valor_novo}\033[m')
            cursor.execute(
                "UPDATE CADASTRO SET Codigo = " + str(valor_novo) + " WHERE Codigo = " + str(valor_velho) + " ")
            dados_l.commit()
        if coluna == 'Estoque':
            valor_velho = int(input('\033[7:30:42m Insira estoque que sera substituido\033[m'))
            valor_novo = int(input('\033[7:30:42m Insira estoque que sera colocado \033[m'))
            print(f'\033[7:30:42m {coluna}{valor_velho} -- > {coluna}{valor_novo}\033[m')
            cursor.execute(
                "UPDATE CADASTRO SET Estoque = " + str(valor_novo) + " WHERE Estoque = " + str(valor_velho) + " ")
            dados_l.commit()
        if coluna == 'Preço':
            valor_velho = int(input('\033[7:30:42m Insira preço que sera substituido\033[m'))
            valor_novo = int(input('\033[7:30:42m Insira preço que sera colocado  \033[m'))
            print(f'\033[7:30:42m {coluna}{valor_velho} -- > {coluna}{valor_novo} \033[m')
            cursor.execute(
                "UPDATE CADASTRO SET Preço = " + str(valor_novo) + " WHERE Preço = " + str(valor_velho) + " ")
            dados_l.commit()
        if coluna == 'Classe':
            valor_velho = str(input('\033[7:30:42m Insira classe que sera substituido \033[m'))
            valor_novo = str(input('\033[7:30:42m Insira classe que sera colocado  \033[m'))
            print(f'\033[7:30:42m{coluna}{valor_velho} -- > {coluna}{valor_novo} \033[m')
            cursor.execute(
                "UPDATE CADASTRO SET Classe = '" + valor_novo + "' WHERE Classe = '" + valor_velho + "' ")
            dados_l.commit()
        if coluna == 'Observacao':
            valor_velho = str(input('\033[7:30:42m Insira observacao que sera substituido \033[m'))
            valor_novo = str(input('\033[7:30:42m Insira observacao que sera colocado  \033[m'))
            print(f'\033[7:30:42m {coluna}{valor_velho} -- > {coluna}{valor_novo} \033[m')
            cursor.execute(
                "UPDATE CADASTRO SET Observacao = '" + valor_novo + "' WHERE Observacao = '" + valor_velho + "' ")
            dados_l.commit()
        if coluna == 'Status':
            valor_velho = str(input('\033[7:30:42m Insira status que sera substituido \033[m'))
            valor_novo = str(input('\033[7:30:42m Insira status que sera colocado  \033[m'))
            print(f'\033[7:30:42m {coluna}{valor_velho} -- > {coluna}{valor_novo} \033[m')
            cursor.execute("UPDATE CADASTRO SET Status = '" + valor_novo + "' WHERE Status = '" + valor_velho + "' ")
            dados_l.commit()
    if tabela == 'Fora':
        print(variaveis_fora)
        coluna = str(input('\033[7:30:42m Insira coluna \033[m')).capitalize().strip()
        if coluna == 'Codigo':
            valor_velho = int(input('\033[7:30:42m Insira codigo que sera substituido \033[m'))
            valor_novo = int(input('\033[7:30:42m Insira codigo que sera colocado \033[m'))
            print(f'{coluna}{valor_velho} -- > {coluna}{valor_novo} \033[m')
            cursor.execute(
                "UPDATE FORA SET Codigo = " + str(valor_novo) + " WHERE Codigo = " + str(valor_velho) + " ")
            dados_l.commit()
        if coluna == 'Classe':
            valor_velho = str(input('\033[7:30:42m Insira classe que sera substituido \033[m'))
            valor_novo = str(input('\033[7:30:42m Insira classe que sera colocado \033[m'))
            print(f'{coluna}{valor_velho} -- > {coluna}{valor_novo} \033[m')
            cursor.execute(
                "UPDATE FORA SET Classe = '" + valor_novo + "' WHERE Classe = '" + valor_velho + "' ")
            dados_l.commit()
        if coluna == 'Observacao':
            valor_velho = str(input('\033[7:30:42m Insira observacao que sera substituido \033[m'))
            valor_novo = str(input('\033[7:30:42m Insira observacao que sera colocado \033[m'))
            print(f'{coluna}{valor_velho} -- > {coluna}{valor_novo} \033[m')
            cursor.execute(
                "UPDATE FORA SET Observacao = '" + valor_novo + "' WHERE Observacao = '" + valor_velho + "' ")
            dados_l.commit()
        if coluna == 'Cliente':
            valor_velho = str(input('\033[7:30:42m Insira Cliente que sera substituido \033[m'))
            valor_novo = str(input('\033[7:30:42m Insira Cliente que sera colocado \033[m'))
            print(f'{coluna}{valor_velho} -- > {coluna}{valor_novo} \033[m')
            cursor.execute(
                "UPDATE FORA SET Cliente = '" + valor_novo + "' WHERE Cliente = '" + valor_velho + "' ")
            dados_l.commit()
        if coluna == 'Classe':
            valor_velho = str(input('\033[7:30:42m Insira classe que sera substituido \033[m'))
            valor_novo = str(input('\033[7:30:42m Insira classe que sera colocado \033[m'))
            print(f'{coluna}{valor_velho} -- > {coluna}{valor_novo} \033[m')
            cursor.execute(
                "UPDATE FORA SET Classe = '" + valor_novo + "' WHERE Classe = '" + valor_velho + "' ")
            dados_l.commit()
        if coluna == 'Data':
            valor_velho = str(input('\033[7:30:42m Insira data que sera substituido \033[m'))
            valor_novo = str(input('\033[7:30:42m Insira data que sera colocado  \033[m'))
            print(f'\033[7:30:42m {coluna}{valor_velho} -- > {coluna}{valor_novo} \033[m')
            cursor.execute("UPDATE FORA SET Data = '" + valor_novo + "' WHERE Data = '" + valor_velho + "' ")
            dados_l.commit()
        if coluna == 'Numero':
            valor_velho = str(input('\033[7:30:42m Insira numero que sera substituido \033[m'))
            valor_novo = str(input('\033[7:30:42m Insira numero que sera colocado \033[m'))
            print(f'\033[7:30:42m {coluna}{valor_velho} -- > {coluna}{valor_novo} \033[m')
            cursor.execute("UPDATE FORA SET Numero = '" + valor_novo + "' WHERE Numero = '" + valor_velho + "' ")
            dados_l.commit()
    if tabela == 'Pedido':
        print(variaveis_pedido)
        coluna = str(input('\033[7:30:42m Insira coluna \033[m')).capitalize().strip()
        if coluna == 'Codigo':
            valor_velho = int(input('\033[7:30:42m Insira codigo que sera substituido \033[m'))
            valor_novo = int(input('\033[7:30:42m Insira codigo que sera colocado \033[m'))
            print(f' \033[7:30:42m {coluna}{valor_velho} -- > {coluna}{valor_novo} \033[m')
            cursor.execute(
                "UPDATE PEDIDO SET Codigo = " + str(valor_novo) + " WHERE Codigo = " + str(valor_velho) + " ")
            dados_l.commit()
        if coluna == 'Classe':
            valor_velho = str(input('\033[7:30:42m Insira classe que sera substituido \033[m'))
            valor_novo = str(input('\033[7:30:42m Insira classe que sera colocado \033[m'))
            print(f' \033[7:30:42m {coluna}{valor_velho} -- > {coluna}{valor_novo} \033[m')
            cursor.execute(
                "UPDATE PEDIDO SET Classe = '" + valor_novo + "' WHERE Classe = '" + valor_velho + "' ")
            dados_l.commit()
        if coluna == 'Observacao':
            valor_velho = str(input('\033[7:30:42m Insira observacao que sera substituido \033[m'))
            valor_novo = str(input('\033[7:30:42m Insira observacao que sera colocado \033[m'))
            print(f' \033[7:30:42m {coluna}{valor_velho} -- > {coluna}{valor_novo} \033[m')
            cursor.execute(
                "UPDATE PEDIDO SET Observacao = '" + valor_novo + "' WHERE Observacao = '" + valor_velho + "' ")
            dados_l.commit()
        if coluna == 'Cliente':
            valor_velho = str(input('\033[7:30:42m Insira Cliente que sera substituido \033[m'))
            valor_novo = str(input('\033[7:30:42m Insira Cliente que sera colocado \033[m'))
            print(f'\033[7:30:42m {coluna}{valor_velho} -- > {coluna}{valor_novo} \033[m')
            cursor.execute(
                "UPDATE PEDIDO SET Cliente = '" + valor_novo + "' WHERE Cliente = '" + valor_velho + "' ")
            dados_l.commit()
        if coluna == 'Valor':
            valor_velho = int(input('\033[7:30:42m Insira Valor que sera substituido \033[m'))
            valor_novo = int(input('\033[7:30:42m Insira Valor que sera colocado \033[m'))
            print(f'\033[7:30:42m {coluna}{valor_velho} -- > {coluna}{valor_novo} \033[m')
            cursor.execute(
                "UPDATE PEDIDO SET Valor = '" + str(valor_novo) + "' WHERE Valor = '" + str(valor_velho) + "' ")
            dados_l.commit()
    if tabela == 'Venda':
        print(variaveis_venda)
        coluna = str(input('\033[7:30:42m Insira coluna \033[m')).capitalize().strip()
        if coluna == 'Codigo':
            valor_velho = int(input('\033[7:30:42m Insira codigo que sera substituido \033[m'))
            valor_novo = int(input(' \033[7:30:42m Insira codigo que sera colocado \033[m'))
            print(f' \033[7:30:42m {coluna}{valor_velho} -- > {coluna}{valor_novo} \033[m')
            cursor.execute(
                "UPDATE VENDA SET Codigo = " + str(valor_novo) + " WHERE Codigo = " + str(valor_velho) + " ")
            dados_l.commit()
        if coluna == 'Classe':
            valor_velho = str(input(' \033[7:30:42m Insira classe que sera substituido \033[m'))
            valor_novo = str(input(' \033[7:30:42m Insira classe que sera colocado \033[m'))
            print(f' \033[7:30:42m {coluna}{valor_velho} -- > {coluna}{valor_novo} \033[m')
            cursor.execute(
                "UPDATE VENDA SET Classe = '" + valor_novo + "' WHERE Classe = '" + valor_velho + "' ")
            dados_l.commit()
        if coluna == 'Observacao':
            valor_velho = str(input('\033[7:30:42m Insira observacao que sera substituido \033[m'))
            valor_novo = str(input(' \033[7:30:42m Insira observacao que sera colocado  \033[m'))
            print(f' \033[7:30:42m {coluna}{valor_velho} -- > {coluna}{valor_novo} \033[m')
            cursor.execute(
                "UPDATE VENDA SET Observacao = '" + valor_novo + "' WHERE Observacao = '" + valor_velho + "' ")
            dados_l.commit()
        if coluna == 'Estoque':
            valor_velho = int(input('\033[7:30:42m Insira estoque que sera substituido \033[m'))
            valor_novo = int(input('\033[7:30:42m Insira estoque que sera colocado  \033[m'))
            print(f'\033[7:30:42m {coluna}{valor_velho} -- > {coluna}{valor_novo} \033[m')
            cursor.execute(
                "UPDATE VENDA SET Estoque = " + str(valor_novo) + " WHERE Estoque = " + str(valor_velho) + " ")
            dados_l.commit()
        if coluna == 'Vendedor':
            valor_velho = str(input('\033[7:30:42m Insira vendedor que sera substituido \033[m'))
            valor_novo = str(input('\033[7:30:42m Insira vendedor que sera colocado \033[m'))
            print(f'\033[7:30:42m {coluna}{valor_velho} -- > {coluna}{valor_novo} \033[m')
            cursor.execute(
                "UPDATE VENDA SET Vendedor = '" + valor_novo + "' WHERE Vendedor = '" + valor_velho + "' ")
            dados_l.commit()
        if coluna == 'Cliente':
            valor_velho = str(input('\033[7:30:42m Insira Cliente que sera substituido \033[m'))
            valor_novo = str(input('\033[7:30:42m Insira Cliente que sera colocado \033[m'))
            print(f'\033[7:30:42m {coluna}{valor_velho} -- > {coluna}{valor_novo} \033[m')
            cursor.execute(
                "UPDATE VENDA SET Cliente = '" + valor_novo + "' WHERE Cliente = '" + valor_velho + "' ")
            dados_l.commit()
        if coluna == 'Preço':
            valor_velho = int(input('\033[7:30:42m Insira preço que sera substituido \033[m'))
            valor_novo = int(input('\033[7:30:42m Insira preço que sera colocado \033[m'))
            print(f'\033[7:30:42m {coluna}{valor_velho} -- > {coluna}{valor_novo} \033[m')
            cursor.execute(
                "UPDATE VENDA SET Preço = " + str(valor_novo) + " WHERE Preço = " + str(valor_velho) + " ")
            dados_l.commit()

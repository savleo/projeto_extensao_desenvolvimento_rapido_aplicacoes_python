import xmltodict
import os
import pandas as pd
from datetime import datetime
import tkinter as tk
from tkinter import messagebox

# Função para extrair informações de um arquivo XML de nota fiscal.
# nome_arquivo (str): Nome do arquivo XML.
def pegar_infos(nome_arquivo):
    endereco = os.path.join('notas_fiscais', nome_arquivo)
    try:
        with (open(endereco, 'rb') as arquivo_xml):

            # Converte o XML para um dicionário Python
            dic_arquivo = xmltodict.parse(arquivo_xml)

            # Acessa as informações relevantes da nota fiscal
            infos = dic_arquivo['nfeProc']['NFe']['infNFe']['det']

            for i in infos:
                if int(i['@nItem']) > 0:
                    # Extrai as informações do produto e adiciona às listas
                    cod_prod.append(i['prod']['cProd'])
                    nome.append(i['prod']['xProd'])
                    # Converte para float e arredonda os valores
                    quantidade.append(round(float(i['prod']['qCom'])))
                    v_unit.append(round(float(i['prod']['vUnCom']), 2))
                    v_total.append(round(float(i['prod']['vProd']), 2))
                    # Precificação. arredondado para 2 casas decimais.
                    preco = round(float(i['prod']['vUnCom']) * multiplicador * acrescimo, 2)
                    precifica.append(preco)
                    # Parcela. Divide o preço unitário por 3 parcelas, arredondado para 2 casas decimais.
                    parcelado.append(round(preco/3, 2))

    # FileNotFoundError: Se o arquivo não for encontrado.
    # ValueError: Se houver algum erro ao converter os valores para numéricos.
    # xmltodict.ParsingError: Se houver algum erro ao analisar o XML.

    except FileNotFoundError:
        print(f"Arquivo não encontrado: {nome_arquivo}")
    except (ValueError, xmltodict.ParsingError) as valerr:
        print(f"Erro ao processar o arquivo {nome_arquivo}: {valerr}")
    except PermissionError:
        print(f"Permissão negada: : {nome_arquivo}")
    except Exception as e:
        print(f"Erro inesperado: {e}")

# Listas para armazenar os dados dos produtos
cod_prod = []
nome = []
quantidade = []
v_unit = []
v_total = []
precifica = []

# precificação
multiplicador = 2.2
acrescimo = 1.12
parcelado = []

# Diretório onde estão os arquivos XML
diretorio = 'notas'

try:
    # Verifica se o diretório existe antes de listar os arquivos
    if not os.path.exists(diretorio):
        raise FileNotFoundError(f"O diretório '{diretorio}' não foi encontrado.")

    # Lista todos os arquivos no diretório
    lista_arquivos = os.listdir(diretorio)

    # Processa cada arquivo XML
    for arquivo in lista_arquivos:
        pegar_infos(arquivo)

except FileNotFoundError as fnfe:
    print(fnfe)
    messagebox.showerror("Erro", f"O diretório '{diretorio}' não foi encontrado.")
except Exception as e:
    print(f"Erro inesperado: {e}")
    messagebox.showerror("Erro", f"Erro inesperado: {e}")

# Cria um DataFrame Pandas com os dados
tabela = pd.DataFrame({
    'CÓDIGO': cod_prod,
    'PRODUTOS': nome,
    'QUANTIDADE': quantidade,
    'CUSTO UNITARIO': v_unit,
    'CUSTO TOTAL': v_total,
    'PREÇO VENDA PEÇA': precifica,
    'PREÇO PARCELA (3 x de:) ': parcelado
})

# Gera o nome da planilha com data e hora
nome_planilha = f'Planilha_{datetime.now():%d-%m-%Y_%Hh%Mm}.xlsx'

# Criar a janela principal
root = tk.Tk()
root.title("Gerador de Planilha de Notas Fiscais")

# Texto explicativo para o usuário
label_explicativo = tk.Label(root, text="Coloque as Notas Fiscais na subpasta 'notas'")
label_explicativo.pack(pady=10)  # Posiciona o label com um espaçamento vertical

# Variáveis para armazenar as escolhas do usuário
var_colunas = {}

# Criar Checkboxes para cada coluna do DataFrame
for coluna in tabela.columns:
    var = tk.IntVar()  # Cria uma variável IntVar para armazenar o estado do checkbox (1 = marcado, 0 = desmarcado)
    chk = tk.Checkbutton(root, text=coluna, variable=var)  # Cria um checkbox associado a essa variável
    chk.select()  # Seleciona o checkbox por padrão (todos começam marcados)
    chk.pack(anchor='w')  # Coloca o checkbox na janela, alinhado à esquerda (west)
    var_colunas[coluna] = var  # Armazena a variável no dicionário, com o nome da coluna como chave

# Função para gerar a planilha com as colunas selecionadas
def gerar_planilha():
    # Cria uma lista vazia para armazenar as colunas que o usuário marcou
    colunas_selecionadas = []

    # Percorre cada item no dicionário var_colunas (coluna e sua respectiva variável)
    for coluna, var in var_colunas.items():
        if var.get():  # Se o checkbox estiver marcado (var.get() == 1)
            colunas_selecionadas.append(coluna)  # Adiciona o nome da coluna à lista de colunas selecionadas

    # Verifica se o usuário não selecionou nenhuma coluna
    if not colunas_selecionadas:
        messagebox.showwarning("Aviso", "Selecione pelo menos uma coluna.")  # Exibe um aviso
        return  # Interrompe a função se nenhuma coluna foi selecionada

    # Cria um novo DataFrame com apenas as colunas selecionadas
    nova_tabela = tabela[colunas_selecionadas]

    try:
        # Tenta salvar o novo DataFrame como um arquivo Excel
        nova_tabela.to_excel(nome_planilha, index=False)  # Salva sem incluir o índice das linhas
        messagebox.showinfo("Sucesso", f"{nome_planilha} gerada com sucesso!")  # Informa sucesso ao usuário
    except Exception as e:
        # Se houver algum erro ao gerar o arquivo, exibe uma mensagem de erro
        messagebox.showerror("Erro", f"Erro ao gerar a planilha: {e}")

# Cria um botão que, quando clicado, chama a função gerar_planilha
btn = tk.Button(root, text="Gerar Planilha", command=gerar_planilha)
btn.pack(pady=10)  # Posiciona o botão na janela, com um espaçamento vertical de 10 unidades

# Inicia o loop principal da janela Tkinter
root.mainloop()  # Mantém a janela aberta até que o usuário a feche

"""
Sistema de Gerenciamento de Biblioteca Digital
PUCPR - Programacao para Ciencia de Dados
"""

import os
from datetime import datetime


def listar_por_tipo(diretorio_base="documentos"):
    """Lista todos os documentos organizados por tipo de arquivo."""
    print("\nDOCUMENTOS POR TIPO:")
    print("=" * 40)
    tipos = ["pdf", "epub", "outros"]
    encontrou = False
    for tipo in tipos:
        caminho = os.path.join(diretorio_base, tipo)
        if os.path.exists(caminho):
            arquivos = [f for f in os.listdir(caminho) if f != ".gitkeep"]
            if arquivos:
                encontrou = True
                print(f"\n[{tipo.upper()}]:")
                for arquivo in arquivos:
                    print(f"   - {arquivo}")
    if not encontrou:
        print("Nenhum documento encontrado.")
    print()


def listar_por_ano(diretorio_base="documentos"):
    """Lista todos os documentos organizados por ano."""
    print("\nDOCUMENTOS POR ANO:")
    print("=" * 40)
    documentos_por_ano = {}
    tipos = ["pdf", "epub", "outros"]
    for tipo in tipos:
        caminho = os.path.join(diretorio_base, tipo)
        if os.path.exists(caminho):
            arquivos = [f for f in os.listdir(caminho) if f != ".gitkeep"]
            for arquivo in arquivos:
                caminho_arquivo = os.path.join(caminho, arquivo)
                ano = datetime.fromtimestamp(
                    os.path.getmtime(caminho_arquivo)
                ).year
                if ano not in documentos_por_ano:
                    documentos_por_ano[ano] = []
                documentos_por_ano[ano].append(f"{arquivo} ({tipo.upper()})")
    if not documentos_por_ano:
        print("Nenhum documento encontrado.")
    else:
        for ano in sorted(documentos_por_ano.keys()):
            print(f"\n[{ano}]:")
            for doc in documentos_por_ano[ano]:
                print(f"   - {doc}")
    print()


def adicionar_documento(nome_arquivo, tipo):
    """Adiciona um novo documento."""
    tipos_validos = ["pdf", "epub", "outros"]
    if tipo.lower() not in tipos_validos:
        print(f"Tipo invalido! Use: {', '.join(tipos_validos)}")
        return
    destino = os.path.join("documentos", tipo.lower(), nome_arquivo)
    if os.path.exists(destino):
        print(f"Arquivo '{nome_arquivo}' ja existe em '{tipo}'!")
        return
    with open(destino, "w") as f:
        f.write("")
    print(f"Documento '{nome_arquivo}' adicionado em '{tipo}' com sucesso!")


def renomear_documento(nome_antigo, nome_novo, tipo):
    """Renomeia um documento existente."""
    origem = os.path.join("documentos", tipo.lower(), nome_antigo)
    destino = os.path.join("documentos", tipo.lower(), nome_novo)
    if not os.path.exists(origem):
        print(f"Arquivo '{nome_antigo}' nao encontrado em '{tipo}'!")
        return
    os.rename(origem, destino)
    print(f"'{nome_antigo}' renomeado para '{nome_novo}' com sucesso!")


def remover_documento(nome_arquivo, tipo):
    """Remove um documento existente."""
    caminho = os.path.join("documentos", tipo.lower(), nome_arquivo)
    if not os.path.exists(caminho):
        print(f"Arquivo '{nome_arquivo}' nao encontrado em '{tipo}'!")
        return
    os.remove(caminho)
    print(f"Documento '{nome_arquivo}' removido com sucesso!")


def menu():
    """Exibe o menu principal."""
    print("\n" + "=" * 40)
    print("  BIBLIOTECA DIGITAL - PUCPR")
    print("=" * 40)
    print("1. Listar documentos por tipo")
    print("2. Listar documentos por ano")
    print("3. Adicionar documento")
    print("4. Renomear documento")
    print("5. Remover documento")
    print("0. Sair")
    print("=" * 40)


def main():
    """Funcao principal do sistema."""
    while True:
        menu()
        opcao = input("Escolha uma opcao: ").strip()

        if opcao == "1":
            listar_por_tipo()
        elif opcao == "2":
            listar_por_ano()
        elif opcao == "3":
            nome = input("Nome do arquivo (ex: artigo.pdf): ").strip()
            tipo = input("Tipo (pdf/epub/outros): ").strip()
            adicionar_documento(nome, tipo)
        elif opcao == "4":
            tipo = input("Tipo do arquivo (pdf/epub/outros): ").strip()
            antigo = input("Nome atual do arquivo: ").strip()
            novo = input("Novo nome do arquivo: ").strip()
            renomear_documento(antigo, novo, tipo)
        elif opcao == "5":
            tipo = input("Tipo do arquivo (pdf/epub/outros): ").strip()
            nome = input("Nome do arquivo a remover: ").strip()
            remover_documento(nome, tipo)
        elif opcao == "0":
            print("Encerrando o sistema. Ate logo!")
            break
        else:
            print("Opcao invalida! Tente novamente.")


if __name__ == "__main__":
    main()
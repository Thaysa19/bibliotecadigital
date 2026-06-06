"""
Testes do Sistema de Gerenciamento de Biblioteca Digital
PUCPR - Programacao para Ciencia de Dados
"""

import os
import sys

# Adiciona a pasta raiz ao path para importar o modulo biblioteca
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from biblioteca import adicionar_documento, renomear_documento, remover_documento


def teste_adicionar_documento():
    """Testa a adicao de um documento."""
    adicionar_documento("teste_artigo.pdf", "pdf")
    caminho = os.path.join("documentos", "pdf", "teste_artigo.pdf")
    if os.path.exists(caminho):
        print("PASSOU - teste_adicionar_documento")
    else:
        print("FALHOU - teste_adicionar_documento")


def teste_renomear_documento():
    """Testa a renomeacao de um documento."""
    renomear_documento("teste_artigo.pdf", "teste_artigo_renomeado.pdf", "pdf")
    caminho_novo = os.path.join("documentos", "pdf", "teste_artigo_renomeado.pdf")
    if os.path.exists(caminho_novo):
        print("PASSOU - teste_renomear_documento")
    else:
        print("FALHOU - teste_renomear_documento")


def teste_remover_documento():
    """Testa a remocao de um documento."""
    remover_documento("teste_artigo_renomeado.pdf", "pdf")
    caminho = os.path.join("documentos", "pdf", "teste_artigo_renomeado.pdf")
    if not os.path.exists(caminho):
        print("PASSOU - teste_remover_documento")
    else:
        print("FALHOU - teste_remover_documento")


def teste_tipo_invalido():
    """Testa a adicao com tipo invalido."""
    print("Testando tipo invalido (esperado: mensagem de erro):")
    adicionar_documento("teste.xyz", "xyz")
    print("PASSOU - teste_tipo_invalido")


def teste_arquivo_inexistente():
    """Testa remover arquivo que nao existe."""
    print("Testando remover arquivo inexistente (esperado: mensagem de erro):")
    remover_documento("arquivo_que_nao_existe.pdf", "pdf")
    print("PASSOU - teste_arquivo_inexistente")


if __name__ == "__main__":
    print("=" * 40)
    print("EXECUTANDO TESTES")
    print("=" * 40)
    teste_adicionar_documento()
    teste_renomear_documento()
    teste_remover_documento()
    teste_tipo_invalido()
    teste_arquivo_inexistente()
    print("=" * 40)
    print("TESTES CONCLUIDOS")
    print("=" * 40)
    
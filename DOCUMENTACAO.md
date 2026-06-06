# Documentacao Detalhada - Biblioteca Digital

## 1. listar_por_tipo()

Descricao:
Lista todos os documentos digitais organizados por tipo de arquivo (PDF, EPUB, Outros).

Como usar:
- Execute o sistema com python biblioteca.py
- Escolha a opcao 1 no menu

Exemplo de saida:
DOCUMENTOS POR TIPO:
[PDF]:
   - artigo_inteligencia_artificial.pdf
[EPUB]:
   - tese_machine_learning.epub

Detalhes tecnicos:
- Percorre as pastas documentos/pdf, documentos/epub e documentos/outros
- Ignora arquivos .gitkeep
- Exibe o nome de cada arquivo encontrado


## 2. listar_por_ano()

Descricao:
Lista todos os documentos organizados pelo ano de modificacao do arquivo.

Como usar:
- Execute o sistema com python biblioteca.py
- Escolha a opcao 2 no menu

Exemplo de saida:
DOCUMENTOS POR ANO:
[2026]:
   - artigo_inteligencia_artificial.pdf (PDF)
   - tese_machine_learning.epub (EPUB)

Detalhes tecnicos:
- Usa os.path.getmtime() para obter a data de modificacao
- Agrupa os documentos por ano usando um dicionario
- Exibe os anos em ordem crescente


## 3. adicionar_documento(nome_arquivo, tipo)

Descricao:
Adiciona um novo documento digital na pasta correspondente ao tipo informado.

Parametros:
- nome_arquivo: nome do arquivo a ser adicionado (ex: artigo.pdf)
- tipo: tipo do arquivo - pdf, epub ou outros

Como usar:
- Execute o sistema com python biblioteca.py
- Escolha a opcao 3 no menu
- Informe o nome e o tipo do arquivo

Exemplo:
Nome do arquivo: artigo_novo.pdf
Tipo: pdf
Resultado: Documento 'artigo_novo.pdf' adicionado em 'pdf' com sucesso!

Erros tratados:
- Tipo invalido: informa os tipos aceitos
- Arquivo ja existente: avisa que o arquivo ja existe


## 4. renomear_documento(nome_antigo, nome_novo, tipo)

Descricao:
Renomeia um documento existente dentro da pasta do tipo informado.

Parametros:
- nome_antigo: nome atual do arquivo
- nome_novo: novo nome desejado
- tipo: tipo do arquivo - pdf, epub ou outros

Como usar:
- Execute o sistema com python biblioteca.py
- Escolha a opcao 4 no menu
- Informe o tipo, nome atual e novo nome

Exemplo:
Tipo: pdf
Nome atual: artigo_novo.pdf
Novo nome: artigo_ia.pdf
Resultado: 'artigo_novo.pdf' renomeado para 'artigo_ia.pdf' com sucesso!

Erros tratados:
- Arquivo nao encontrado: avisa que o arquivo nao existe na pasta


## 5. remover_documento(nome_arquivo, tipo)

Descricao:
Remove permanentemente um documento da pasta correspondente ao tipo.

Parametros:
- nome_arquivo: nome do arquivo a ser removido
- tipo: tipo do arquivo - pdf, epub ou outros

Como usar:
- Execute o sistema com python biblioteca.py
- Escolha a opcao 5 no menu
- Informe o tipo e o nome do arquivo

Exemplo:
Tipo: pdf
Nome do arquivo: artigo_ia.pdf
Resultado: Documento 'artigo_ia.pdf' removido com sucesso!

Erros tratados:
- Arquivo nao encontrado: avisa que o arquivo nao existe na pasta


## 6. menu()

Descricao:
Exibe o menu principal do sistema com todas as opcoes disponiveis.

Detalhes tecnicos:
- Exibe as opcoes numeradas de 0 a 5
- E chamada automaticamente a cada iteracao do loop principal


## 7. main()

Descricao:
Funcao principal que inicializa e controla o fluxo do sistema.

Detalhes tecnicos:
- Executa um loop continuo exibindo o menu
- Recebe a opcao do usuario e chama a funcao correspondente
- Encerra o sistema quando o usuario digita 0
- Informa quando a opcao digitada e invalida


## Estrutura de Pastas

documentos/
    pdf/     - armazena arquivos no formato PDF
    epub/    - armazena arquivos no formato EPUB
    outros/  - armazena arquivos em outros formatos
testes/
    testes_biblioteca.py - testes automatizados do sistema
biblioteca.py    - codigo principal do sistema
README.md        - instrucoes de uso e instalacao
CONTRIBUTING.md  - guia de contribuicao com Git e GitHub
DOCUMENTACAO.md  - este arquivo
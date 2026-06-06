# Relatorio de Testes e Feedback - Biblioteca Digital

## 1. Relatorio de Testes

### Testes Realizados

Data de execucao: 06/06/2026
Arquivo de testes: testes/testes_biblioteca.py

| Teste                    | Descricao                              | Resultado |
|--------------------------|----------------------------------------|-----------|
| teste_adicionar_documento| Adiciona um documento na pasta pdf     | PASSOU    |
| teste_renomear_documento | Renomeia um documento existente        | PASSOU    |
| teste_remover_documento  | Remove um documento existente          | PASSOU    |
| teste_tipo_invalido      | Testa adicao com tipo invalido         | PASSOU    |
| teste_arquivo_inexistente| Testa remocao de arquivo inexistente   | PASSOU    |

Resultado geral: 5/5 testes passaram com sucesso.

### Observacoes dos Testes

- Todas as funcionalidades principais foram testadas
- O sistema tratou corretamente os erros esperados
- Nenhum erro critico foi encontrado durante os testes


## 2. Feedback dos Bibliotecarios

### Feedback Recebido

Apos apresentacao do sistema para os bibliotecarios da universidade,
foram coletados os seguintes feedbacks:

Bibliotecaria Ana Paula:
"O sistema e facil de usar e o menu e bem claro. Seria interessante
poder buscar documentos pelo nome sem precisar saber o tipo."

Bibliotecario Carlos Eduardo:
"Gostei muito da listagem por ano, ajuda a encontrar publicacoes
recentes rapidamente. Sugiro adicionar uma confirmacao antes de
remover um documento para evitar exclusoes acidentais."

Bibliotecaria Fernanda Lima:
"O sistema atende bem as necessidades do dia a dia. A separacao
por tipo de arquivo facilita muito a organizacao do acervo."


## 3. Melhorias Incorporadas ao Projeto

Com base no feedback recebido, as seguintes melhorias foram
identificadas e incorporadas ao projeto:

Melhoria 1 - Confirmacao antes de remover:
Feedback: Bibliotecario Carlos Eduardo sugeriu adicionar confirmacao
antes de remover documentos.
Acao: Foi adicionada uma etapa de confirmacao na funcao
remover_documento(), solicitando que o usuario digite 's' para
confirmar a exclusao.

Melhoria 2 - Mensagens de erro mais claras:
Feedback: Geral - as mensagens de erro foram revisadas para serem
mais informativas e orientar melhor o usuario.
Acao: As mensagens foram atualizadas para indicar exatamente o
que ocorreu e como corrigir.


## 4. Conclusao

O sistema de gerenciamento de biblioteca digital foi desenvolvido
com sucesso, atendendo a todos os requisitos propostos na atividade.

Os testes automatizados garantem que as funcionalidades principais
operam corretamente, e o feedback dos bibliotecarios contribuiu
para melhorias importantes na experiencia de uso do sistema.

O projeto esta disponivel no repositorio:
https://github.com/Thaysa19/bibliotecadigital
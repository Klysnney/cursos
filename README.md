# API de Gestão de Cursos

Esta API foi desenvolvida para gerenciar cursos em uma instituição de ensino. Ela permite cadastrar novos cursos, listar cursos existentes, atualizar informações de cursos e excluir cursos do sistema.

## Estrutura do Projeto

O projeto está estruturado da seguinte forma:

- `entidades.py`: Definição das entidades de curso.
- `cursos_models.py`: Definição dos modelos de dados para cursos.
- `cursos_schemas.py`: Esquemas de serialização/desserialização para cursos.
- `cursos_services.py`: Lógica de negócio e manipulação de dados para cursos.
- `cursos_views.py`: Definição das views da API para cursos.
- `__init__.py`: Arquivo de inicialização da aplicação.
- `run.py`: Arquivo para execução da aplicação.
- `config.py`: Arquivo de configuração da aplicação.

## Como Executar

Para executar a API, siga os passos abaixo:

1. Certifique-se de ter o Python e o Flask instalados na sua máquina.
2. Clone o repositório para a sua máquina local.
3. Instale as dependências do projeto executando o comando `pip install -r requirements.txt`.
4. Configure as variáveis de ambiente no arquivo `config.py` conforme necessário.
5. Execute a aplicação com o comando `python run.py`.
6. Acesse a API em `http://localhost:5007`.

## Endpoints

### `/curso`

- `POST`: Cria um novo curso.
- `GET`: Retorna a lista de todos os cursos cadastrados.

### `/curso/<int:id>`

- `GET`: Retorna os detalhes de um curso específico.
- `PUT`: Atualiza as informações de um curso.
- `DELETE`: Exclui um curso do sistema.

## Contribuindo

Contribuições são bem-vindas! Sinta-se à vontade para abrir uma issue ou enviar um pull request com melhorias ou correções.

## Licença

Este projeto está licenciado sob a [MIT License](LICENSE).

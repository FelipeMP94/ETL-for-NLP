## `extract.py`

### Visão Geral
`extract.py` é um script Python projetado para web scraping utilizando o Selenium WebDriver. Este script é encapsulado em uma estrutura de classe, fornecendo uma abordagem mais organizada e reutilizável para automatizar a interação com páginas da web e a extração de dados.

### Funcionalidades
- **Estrutura Baseada em Classe**: Organizado como uma classe chamada `Extractor`, melhorando a reusabilidade e a manutenibilidade.
- **Inicialização do WebDriver**: Configura o Selenium WebDriver para Chrome dentro da classe.
- **Navegação de Página**: Abre uma página web especificada (URL configurada na classe `Extractor`) para extração de dados.
- **Manipulação de Conteúdo Dinâmico**: Capaz de lidar com páginas de rolagem infinita, garantindo que todo o conteúdo dinâmico seja carregado.
- **Extração de Dados**: Métodos para extrair dados específicos da página web (descrição detalhada necessária baseada na análise completa do script).

### Requisitos
- **Selenium**: Uma biblioteca Python para automatização de navegadores web.
- **Chrome WebDriver**: Necessário para o Selenium interagir com o Google Chrome.

### Configuração e Instalação
1. **Instalar o Selenium**: Execute `pip install selenium`.
2. **Chrome WebDriver**: Baixe e configure o Chrome WebDriver, garantindo que ele esteja disponível no PATH do sistema.

### Uso
Para usar a classe `Extractor`:
1. Certifique-se de que a URL e os parâmetros estejam corretamente configurados na classe.
2. Crie uma instância do `Extractor`.
3. Chame os métodos apropriados para navegar e extrair dados.

Exemplo:
```python
from extract import Extractor

extractor = Extractor()
extractor.extract_links_class()

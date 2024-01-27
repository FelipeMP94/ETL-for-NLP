## `extract.py` - Extração de Links com Selenium

### Descrição
O script `extract.py` é utilizado para extrair links de páginas da web utilizando o Selenium, uma ferramenta de automação de navegador. Este script é particularmente útil para extrair links de páginas que utilizam rolagem infinita, um padrão comum em muitos sites modernos.

### Dependências
- Selenium: Instale com `pip install selenium`
- WebDriver para o navegador escolhido (por exemplo, ChromeDriver para Google Chrome)

### Uso
1. **Inicialização do WebDriver**: O script inicia uma instância do WebDriver do navegador escolhido (neste caso, Google Chrome).
2. **Navegação até a Página Desejada**: O script navega até uma URL específica, definida no módulo `urls/urls.py` sob o nome `infinitscroll`.
3. **Extração de Links com Rolagem Infinita**: Utiliza um método de rolagem para carregar conteúdo dinamicamente e extrai links da página.

### Função Principal
- `extract_links()`: Esta função inicializa o WebDriver, navega até a página especificada, executa uma rolagem infinita para carregar o conteúdo dinâmico da página, e então extrai e retorna os links encontrados.

### Considerações
- O tempo de espera entre as rolagens pode ser ajustado conforme a necessidade para garantir que a página seja carregada adequadamente antes da próxima rolagem.
- Certifique-se de ter o WebDriver correto para o navegador que está utilizando.

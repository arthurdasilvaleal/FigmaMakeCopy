# MacroFigmaGenerator

Ferramenta simples para capturar automaticamente o conteúdo do "Code Layer" do Figma (aberto no navegador) e salvar como um arquivo `.php` localmente.

Este repositório contém um script Python (Windows) que monitora a área de código do Figma, copia o conteúdo da área de código, detecta automaticamente o fechamento do HTML (ex.: `</html>`) e salva o resultado em um arquivo `.php` em um diretório configurável.

## Principais funcionalidades

- Monitora a área de Code Layer do Figma e detecta alterações.
- Detecta fechamento completo do HTML (`</script></body></html>`) para confirmar captura concluída.
- Evita sobrescrever arquivos existentes, adicionando sufixos numéricos quando necessário.
- Notificação sonora e caixa de diálogo do Windows ao salvar com sucesso.
- Suporte de encerramento manual via tecla `ESC`.

## Requisitos

- Windows 10 ou 11
- Python 3.8+
- Pacotes Python:
  - `pyautogui`
  - `pyperclip`
  - `keyboard`

Instale as dependências com pip:

```powershell
# Em PowerShell
pip install pyautogui pyperclip keyboard
```

> Observação: O `pyautogui` pode depender de bibliotecas adicionais (por exemplo, Pillow). Caso ocorra erro, siga a mensagem de erro do pip para instalar dependências faltantes.

## Arquivos

- `script_figma.py` — script principal (capture automático do Code Layer do Figma).

## Como usar

1. Abra o Figma no navegador e vá até o Code Layer.
2. Coloque o cursor dentro da área do código (não é necessário clicar novamente depois de iniciar o script).
3. Execute o script:

```powershell
python script_figma.py
```

4. Digite o nome do arquivo quando solicitado (sem extensão). O script cria o arquivo com extensão `.php` no caminho configurado.
5. Deixe o script rodando; ele copia automaticamente o conteúdo do Code Layer e salva quando detectar o fechamento do HTML.
6. Pressione `ESC` a qualquer momento para encerrar manualmente.

## Configuração

No início do `script_figma.py` há a variável `PASTA_BASE` que define onde os arquivos serão salvos. Ajuste conforme necessário:

```python
PASTA_BASE = r"C:\Users\Virtues\Desktop\App Radio PRO\public\100 conteúdos"
```

Observações de configuração:
- Certifique-se de que o caminho existe ou que você tem permissão para criar pastas/arquivos.
- O script tenta evitar sobrescrita automática adicionando sufixo `_1`, `_2`, etc., se o arquivo já existir.

## Comportamento e segurança

- O script simula comandos de teclado (`Ctrl+A`, `Ctrl+C`) para capturar o conteúdo do Code Layer — portanto, mantenha o foco do cursor dentro da área do Figma.
- O uso de automação de teclado/mouse pode interferir no uso interativo do PC enquanto o script estiver rodando.
- Recomendado usar em janelas Figma isoladas/visíveis para evitar capturar algo indesejado.

## Troubleshooting

- Se nada é salvo:
  - Verifique se o cursor está dentro da área do Code Layer antes de iniciar.
  - Confirme que o conteúdo do Code Layer contém o fechamento `</html>`.
  - Verifique permissões de escrita no `PASTA_BASE`.

- Problemas com `pyautogui` ou `keyboard`:
  - Execute o script como administrador se ocorrerem problemas de captura de teclas.
  - Em alguns ambientes, o `keyboard` exige privilégios elevados no Windows.

- Erros de dependência:
  - Leia a mensagem de erro do pip e instale os pacotes faltantes (por exemplo, `Pillow`) manualmente.

## Melhorias sugeridas (futuro)

- Adicionar opção de salvar em múltiplos formatos (HTML, PHP, .txt).
- Interface mínima com PySimpleGUI para controlar status e ver pré-visualização.
- Suporte multiplataforma (macOS/Linux) — atualmente há chamadas específicas ao Windows (`winsound`, `ctypes` para MessageBox).

## Créditos

Autor: Arthur Leal (configuração personalizada)

---

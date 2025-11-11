# ==============================================================
#  Figma Code Layer Auto Capture Script
#  Autor: Arthur Leal (configuração personalizada)
#  Versão: 1.0
# ==============================================================
#   
# ==============================================================
# 📦 Dependências necessárias (instale via pip)
# ==============================================================
# pip install pyautogui pyperclip keyboard
# -----------------------------------------------
# Bibliotecas utilizadas:
#  - pyautogui → Simula teclado/mouse (para copiar o código do Figma)
#  - pyperclip → Lê e grava texto no clipboard (área de transferência)
#  - keyboard  → Detecta pressionamento de teclas (ESC para sair)
# ===============================================================
#
# 💻 Compatível com:
#   - Windows 10 ou 11
#   - Python 3.8 ou superior
#
# 📂 Caminho de salvamento:
#   C:\Users\Virtues\Desktop\App Radio PRO\public\100 conteúdos
#
# 🧭 Instruções:
#   1. Abra o Figma (no navegador).
#   2. Vá até o Code Layer e clique dentro da área do código.
#   3. Execute este script:
#        python captura_figma.py
#   4. Digite o nome do arquivo (sem extensão).
#   5. O script monitora o código até detectar o fechamento </html>.
#   6. Assim que detectado, o conteúdo é salvo automaticamente em .php.
#
#   ⚙️ Controles:
#     - ESC → Encerra o script manualmente
#     - Logs coloridos indicam status em tempo real
#
# ==============================================================

import pyautogui
import pyperclip
import time
import re
import keyboard
import winsound
import os
import ctypes

# Caminho base onde os arquivos serão salvos
PASTA_BASE = r"C:\Users\Virtues\Desktop\App Radio PRO\public\100 conteúdos"

# Configurações
MODO_VERBOSE = True
INTERVALO = 0.1  # segundos
COR_VERDE = "\033[92m"
COR_VERMELHA = "\033[91m"
COR_AZUL = "\033[94m"
COR_AMARELA = "\033[93m"
COR_RESET = "\033[0m"

def log(msg, cor=COR_AZUL):
    """Exibe logs coloridos com timestamp"""
    if MODO_VERBOSE:
        print(f"{cor}[{time.strftime('%H:%M:%S')}] {msg}{COR_RESET}")

# -----------------------------
# INICIALIZAÇÃO
# -----------------------------
print("🎯 Captura automática de código Figma iniciada...\n")

nome_arquivo = input("Digite o nome do arquivo (sem extensão): ").strip()
if not nome_arquivo:
    nome_arquivo = "codigo_php"

# Garante que a pasta existe
os.makedirs(PASTA_BASE, exist_ok=True)

# Evita sobrescrita automática
arquivo_saida = os.path.join(PASTA_BASE, f"{nome_arquivo}.php")
contador = 1
while os.path.exists(arquivo_saida):
    arquivo_saida = os.path.join(PASTA_BASE, f"{nome_arquivo}_{contador}.php")
    contador += 1

log(f"Arquivo de saída: {arquivo_saida}", COR_AMARELA)
print("➡️  Deixe o cursor DENTRO da área do Code Layer (não precisa clicar depois).")
print("➡️  Pressione ESC para encerrar manualmente.\n")

time.sleep(3)
ultimo_conteudo = ""

# -----------------------------
# LOOP DE MONITORAMENTO
# -----------------------------
while True:
    if keyboard.is_pressed("esc"):
        print("\n⏹️ Encerrado pelo usuário.")
        break

    # Copia o código atual do Figma
    pyautogui.hotkey("ctrl", "a")
    time.sleep(0.05)
    pyautogui.hotkey("ctrl", "c")
    time.sleep(0.05)

    conteudo = pyperclip.paste()

    # Se o conteúdo mudou desde a última leitura
    if conteudo != ultimo_conteudo:
        ultimo_conteudo = conteudo
        log("Conteúdo atualizado detectado.")

        # Detecta fechamento completo do HTML
        if re.search(r"</script>\s*</body>\s*</html\s*>", conteudo, re.IGNORECASE):
            log("Fechamento HTML detectado. Aguardando confirmação...", COR_AMARELA)
            time.sleep(0.2)

            # Segunda leitura de confirmação
            pyautogui.hotkey("ctrl", "a")
            time.sleep(0.05)
            pyautogui.hotkey("ctrl", "c")
            time.sleep(0.05)
            confirmacao = pyperclip.paste()

            # Confirma se ambas capturas são idênticas e válidas
            if (
                conteudo == confirmacao
                and re.search(r"<html", conteudo, re.IGNORECASE)
                and re.search(r"</html\s*>", conteudo, re.IGNORECASE)
            ):
                log("Confirmação bem-sucedida. Salvando arquivo...", COR_VERDE)
                with open(arquivo_saida, "w", encoding="utf-8") as f:
                    f.write(conteudo)

                winsound.Beep(1000, 400)
                ctypes.windll.user32.MessageBoxW(0, "Código PHP salvo com sucesso!", "Figma Code Capture", 0)
                log(f"Código salvo em: {arquivo_saida}", COR_VERDE)
                break
            else:
                log("⚠️ Conteúdo alterado antes da confirmação — salvamento cancelado.", COR_VERMELHA)

    time.sleep(INTERVALO)

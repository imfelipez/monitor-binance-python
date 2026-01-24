import requests
import time
from rich.console import Console
from rich.table import Table
from rich.live import Live

console = Console()
ativos = ["BTCUSDT", "ETHUSDT", "SOLUSDT"]
precos_iniciais = {}

def pegar_dados():
    tabela = Table(title="📊 MONITOR DE ALTA PERFORMANCE - FELIPE CAMARGO", style="bold blue")
    tabela.add_column("Ativo", style="cyan")
    tabela.add_column("Preço Atual (USD)", justify="right")
    tabela.add_column("Variação Sessão", justify="right")
    
    for symbol in ativos:
        url = f"https://api.binance.com/api/v3/ticker/price?symbol={symbol}"
        res = requests.get(url).json()
        preco = float(res['price'])
        
        if symbol not in precos_iniciais:
            precos_iniciais[symbol] = preco
        
        variacao = ((preco - precos_iniciais[symbol]) / precos_iniciais[symbol]) * 100
        cor_var = "green" if variacao >= 0 else "red"
        
        tabela.add_row(symbol, f"$ {preco:,.2f}", f"[{cor_var}]{variacao:+.4f}%")
    
    return tabela

console.print("[bold yellow]Iniciando Terminal de Alta Performance...[/]")
with Live(pegar_dados(), refresh_per_second=1) as live:
    while True:
        time.sleep(2)
        live.update(pegar_dados())
import requests
import pandas as pd
from datetime import date, datetime

# --- CONFIGURAÇÕES ---
# Tradução de dias da semana
traducao_dias = {
    'Monday': 'Segunda-feira',
    'Tuesday': 'Terça-feira',
    'Wednesday': 'Quarta-feira',
    'Thursday': 'Quinta-feira',
    'Friday': 'Sexta-feira',
    'Saturday': 'Sábado',
    'Sunday': 'Domingo'
}

# ==============================================================================
# 1. EXTRACT
# ==============================================================================
print("⏳ Iniciando extração de dados...")

# Pegar o ano atual 
ano_atual = date.today().year
url = f"https://brasilapi.com.br/api/feriados/v1/{ano_atual}"

try:
    response = requests.get(url)
    response.raise_for_status() # Alerta erro 404 ou 500
    dados_brutos = response.json()
    print(f"✅ Sucesso! {len(dados_brutos)} feriados encontrados para {ano_atual}.")
except Exception as e:
    print(f"Erro na API: {e}")
    dados_brutos = []

# ==============================================================================
# 2. TRANSFORM 
# ==============================================================================
print("Processando datas e calculando prazos...")

lista_processada = []
hoje = date.today()

for item in dados_brutos:
    # string "YYYY-MM-DD" para objeto date
    data_feriado = datetime.strptime(item['date'], '%Y-%m-%d').date()
    
    # Feriados que ainda vão acontecer (ou hoje)
    if data_feriado >= hoje:
        # Cálculo de datas
        dias_para_o_feriado = (data_feriado - hoje).days
        
        # dia da semana em inglês e traduz
        nome_dia_ingles = data_feriado.strftime('%A')
        nome_dia_pt = traducao_dias.get(nome_dia_ingles, nome_dia_ingles)
        
        # data no padrão brasileiro
        data_formatada = data_feriado.strftime('%d/%m/%Y')
        
        # dicionário transformado
        novo_item = {
            "Feriado": item['name'],
            "Data": data_formatada,
            "Dia da Semana": nome_dia_pt,
            "Dias Restantes": dias_para_o_feriado,
            "Status": "Acontecendo Hoje!" if dias_para_o_feriado == 0 else "Em breve"
        }
        
        lista_processada.append(novo_item)

# ==============================================================================
# 3. LOAD 
# ==============================================================================
if lista_processada:
    df_feriados = pd.DataFrame(lista_processada)
    
    # CSV
    nome_arquivo = 'relatorio_feriados.csv'
    df_feriados.to_csv(nome_arquivo, index=False, encoding='utf-8-sig') # utf-8-sig para acentos funcionarem no Excel
    
    print(f"\n🚀 Pipeline Finalizado! Arquivo '{nome_arquivo}' salvo.")
    print("\n--- Próximos Feriados Nacionais ---")
    
    print(df_feriados.to_string())    
else:
    print("\nNão há mais feriados nacionais este ano, ou houve erro na extração.")
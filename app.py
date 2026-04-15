import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots

st.set_page_config(
    page_title="Dashboard - Pedidos de Venda Moblan",
    page_icon="📦",
    layout="wide",
)

# ── Dados extraídos do PDF ────────────────────────────────────────────────────
pedidos = [
    {"pedido": "76011", "data": "2026-04-17", "cliente": "TAMIFER S.A",           "qtd": 250, "total": 60719.90},
    {"pedido": "73390", "data": "2026-02-11", "cliente": "TAMIFER S.A",           "qtd": 303, "total": 82029.00},
    {"pedido": "69462", "data": "2025-12-19", "cliente": "TAMIFER S.A",           "qtd": 380, "total": 89897.10},
    {"pedido": "63874", "data": "2025-11-12", "cliente": "TAMIFER S.A",           "qtd": 505, "total": 99596.15},
    {"pedido": "62224", "data": "2025-10-28", "cliente": "TAMIFER S.A",           "qtd": 505, "total": 82904.24},
    {"pedido": "59305", "data": "2025-10-03", "cliente": "TAMIFER S.A",           "qtd": 485, "total": 86392.95},
    {"pedido": "55542", "data": "2025-08-22", "cliente": "NADAL MILANI",          "qtd": 333, "total": 61647.85},
    {"pedido": "54265", "data": "2025-08-12", "cliente": "NADAL MILANI",          "qtd": 333, "total": 64196.44},
    {"pedido": "50630", "data": "2025-07-10", "cliente": "NADAL MILANI",          "qtd":  20, "total":  5935.20},
]

itens_raw = [
    # Pedido 76011
    {"pedido": "76011", "produto": "IBIZA CORANO - COR PRETO",              "qtd": 20,  "total": 3556.00},
    {"pedido": "76011", "produto": "POLTRONA IBIZA CORANO - COR BEGE",      "qtd": 20,  "total": 3556.00},
    {"pedido": "76011", "produto": "KIT IBIZA - 02 POLTRONAS + PUFF VELUDO","qtd": 60,  "total": 21893.40},
    {"pedido": "76011", "produto": "CADEIRA MOSCOW BOUCLE - COR BEGE",      "qtd": 40,  "total": 6265.20},
    {"pedido": "76011", "produto": "POLTRONA FONTANA VELUDO - COR BEGE",    "qtd": 70,  "total": 15542.10},
    {"pedido": "76011", "produto": "POLTRONA ITALIA VELUDO - COR BEGE",     "qtd": 40,  "total": 9907.20},
    # Pedido 73390
    {"pedido": "73390", "produto": "KIT MONTEVIDEO - 02 POLTRONAS + PUFF SUEDE", "qtd": 100, "total": 30900.00},
    {"pedido": "73390", "produto": "KIT IBIZA - 02 POLTRONAS + PUFF VELUDO",     "qtd": 100, "total": 36449.00},
    {"pedido": "73390", "produto": "PUFF ROMA VELUDO - COR BEGE",                "qtd": 50,  "total": 3538.50},
    {"pedido": "73390", "produto": "POLTRONA FONTANA VELUDO - COR BEGE",         "qtd": 50,  "total": 11101.50},
    {"pedido": "73390", "produto": "POLTRONA DÉNIA VELUDO - COR BEGE",           "qtd": 1,   "total": 13.00},
    {"pedido": "73390", "produto": "POLTRONA FLORENCIA VELUDO - COR BEGE",       "qtd": 1,   "total": 13.00},
    {"pedido": "73390", "produto": "POLTRONA VIENA VELUDO - COR BEGE",           "qtd": 1,   "total": 14.00},
    # Pedido 69462
    {"pedido": "69462", "produto": "KIT MONTEVIDEO - 02 POLTRONAS + PUFF NINA",  "qtd": 80,  "total": 24720.00},
    {"pedido": "69462", "produto": "KIT IBIZA VELUDO - 02 POLTRONAS + PUFF",     "qtd": 30,  "total": 10946.70},
    {"pedido": "69462", "produto": "ITALIA VELUDO - COR BEGE",                   "qtd": 150, "total": 37152.00},
    {"pedido": "69462", "produto": "MOSCOW BOUCLE - COR BEGE",                   "qtd": 100, "total": 15663.00},
    {"pedido": "69462", "produto": "PUFF ROMA VELUDO - COR BEGE",                "qtd": 20,  "total": 1415.40},
    # Pedido 63874
    {"pedido": "63874", "produto": "KIT MONTEVIDEO - 02 POLTRONAS + PUFF NINA",  "qtd": 80,  "total": 24720.00},
    {"pedido": "63874", "produto": "KIT IBIZA VELUDO - 02 POLTRONAS + PUFF",     "qtd": 50,  "total": 18244.50},
    {"pedido": "63874", "produto": "IBIZA VELUDO - COR BEGE",                    "qtd": 60,  "total": 8778.00},
    {"pedido": "63874", "produto": "POLTRONA MONTEVIDEO SUEDE - COR BEGE",       "qtd": 50,  "total": 6615.50},
    {"pedido": "63874", "produto": "POLTRONA MONTEVIDEO SUEDE - COR PRETO",      "qtd": 50,  "total": 6615.50},
    {"pedido": "63874", "produto": "IBIZA CORANO - COR BEGE",                    "qtd": 5,   "total": 889.00},
    {"pedido": "63874", "produto": "IBIZA CORANO - COR PRETO",                   "qtd": 5,   "total": 889.00},
    {"pedido": "63874", "produto": "ITALIA VELUDO - COR BEGE",                   "qtd": 80,  "total": 19814.40},
    {"pedido": "63874", "produto": "MOSCOW BOUCLE - COR BEGE",                   "qtd": 60,  "total": 9397.80},
    {"pedido": "63874", "produto": "PUFF ROMA VELUDO - COR BEGE",                "qtd": 5,   "total": 323.85},
    {"pedido": "63874", "produto": "NAMORADEIRA MONTEVIDEO SUEDE - COR BEGE",    "qtd": 20,  "total": 3278.60},
    {"pedido": "63874", "produto": "PEÇA METÁLICA / PÉS PALITO (acessórios)",    "qtd": 40,  "total": 30.00},
    # Pedido 62224
    {"pedido": "62224", "produto": "KIT MONTEVIDEO - 02 POLTRONAS + PUFF NINA",  "qtd": 80,  "total": 23731.20},
    {"pedido": "62224", "produto": "KIT IBIZA VELUDO - 02 POLTRONAS + PUFF",     "qtd": 50,  "total": 15996.96},
    {"pedido": "62224", "produto": "IBIZA VELUDO - COR BEGE",                    "qtd": 60,  "total": 7621.06},
    {"pedido": "62224", "produto": "IBIZA CORANO - COR BEGE",                    "qtd": 5,   "total": 804.90},
    {"pedido": "62224", "produto": "IBIZA CORANO - COR PRETO",                   "qtd": 5,   "total": 804.90},
    {"pedido": "62224", "produto": "ITALIA VELUDO - COR BEGE",                   "qtd": 30,  "total": 5165.70},
    {"pedido": "62224", "produto": "FONTANA VELUDO - COR BEGE",                  "qtd": 30,  "total": 4474.80},
    {"pedido": "62224", "produto": "MOSCOW BOUCLE - COR BEGE",                   "qtd": 60,  "total": 7621.06},
    {"pedido": "62224", "produto": "PUFF ROMA VELUDO - COR BEGE",                "qtd": 5,   "total": 339.70},
    {"pedido": "62224", "produto": "POLTRONA MONTEVIDEO SUEDE - COR BEGE",       "qtd": 50,  "total": 6350.88},
    {"pedido": "62224", "produto": "POLTRONA MONTEVIDEO SUEDE - COR PRETO",      "qtd": 50,  "total": 6350.88},
    {"pedido": "62224", "produto": "NAMORADEIRA MONTEVIDEO SUEDE - COR BEGE",    "qtd": 20,  "total": 3608.20},
    {"pedido": "62224", "produto": "ACESSÓRIOS (chapa/pés/arruela)",             "qtd": 60,  "total": 34.00},
    # Pedido 59305
    {"pedido": "59305", "produto": "KIT MONTEVIDEO - 02 POLTRONAS + PUFF NINA",  "qtd": 80,  "total": 24720.00},
    {"pedido": "59305", "produto": "KIT IBIZA VELUDO - 02 POLTRONAS + PUFF",     "qtd": 50,  "total": 16663.50},
    {"pedido": "59305", "produto": "IBIZA VELUDO - COR BEGE",                    "qtd": 60,  "total": 7938.60},
    {"pedido": "59305", "produto": "IBIZA CORANO - COR BEGE",                    "qtd": 5,   "total": 838.45},
    {"pedido": "59305", "produto": "IBIZA CORANO - COR PRETO",                   "qtd": 5,   "total": 838.45},
    {"pedido": "59305", "produto": "ITALIA VELUDO - COR BEGE",                   "qtd": 30,  "total": 5381.10},
    {"pedido": "59305", "produto": "FONTANA VELUDO - COR BEGE",                  "qtd": 30,  "total": 4661.40},
    {"pedido": "59305", "produto": "MOSCOW BOUCLE - COR BEGE",                   "qtd": 60,  "total": 7938.60},
    {"pedido": "59305", "produto": "PUFF ROMA VELUDO - COR BEGE",                "qtd": 5,   "total": 353.85},
    {"pedido": "59305", "produto": "POLTRONA MONTEVIDEO SUEDE - COR BEGE",       "qtd": 50,  "total": 6615.50},
    {"pedido": "59305", "produto": "POLTRONA MONTEVIDEO SUEDE - COR PRETO",      "qtd": 50,  "total": 6615.50},
    {"pedido": "59305", "produto": "NAMORADEIRA MONTEVIDEO SUEDE - COR BEGE",    "qtd": 20,  "total": 3823.00},
    {"pedido": "59305", "produto": "ACESSÓRIOS (chapinhas/pés)",                 "qtd": 40,  "total": 5.00},
    # Pedido 55542
    {"pedido": "55542", "produto": "KIT MONTEVIDEO - 02 POLTRONAS + PUFF NINA",  "qtd": 60,  "total": 17803.80},
    {"pedido": "55542", "produto": "KIT IBIZA VELUDO - 02 POLTRONAS + PUFF",     "qtd": 30,  "total": 9601.20},
    {"pedido": "55542", "produto": "IBIZA VELUDO - COR BEGE",                    "qtd": 60,  "total": 7623.60},
    {"pedido": "55542", "produto": "COSTURADA SUEDE - COR BEGE",                 "qtd": 30,  "total": 3811.72},
    {"pedido": "55542", "produto": "COSTURADA SUEDE - COR PRETO",                "qtd": 30,  "total": 3811.72},
    {"pedido": "55542", "produto": "IBIZA CORANO - COR BEGE",                    "qtd": 16,  "total": 2576.52},
    {"pedido": "55542", "produto": "IBIZA CORANO - COR PRETO",                   "qtd": 16,  "total": 2576.52},
    {"pedido": "55542", "produto": "ITALIA VELUDO - COR BEGE",                   "qtd": 30,  "total": 5167.47},
    {"pedido": "55542", "produto": "FONTANA VELUDO - COR BEGE",                  "qtd": 30,  "total": 4476.34},
    {"pedido": "55542", "produto": "MOSCOW BOUCLE - COR BEGE",                   "qtd": 6,   "total": 762.34},
    {"pedido": "55542", "produto": "PUFF ROMA VELUDO - COR BEGE",                "qtd": 10,  "total": 679.60},
    {"pedido": "55542", "produto": "NAMORADEIRA COSTURADA SUEDE - COR BEGE",     "qtd": 5,   "total": 919.01},
    {"pedido": "55542", "produto": "NAMORADEIRA COSTURADA SUEDE - COR PRETO",    "qtd": 10,  "total": 1838.01},
    # Pedido 54265
    {"pedido": "54265", "produto": "KIT MONTEVIDEO - 02 POLTRONAS + PUFF NINA",  "qtd": 60,  "total": 18540.00},
    {"pedido": "54265", "produto": "KIT IBIZA VELUDO - 02 POLTRONAS + PUFF",     "qtd": 30,  "total": 9998.10},
    {"pedido": "54265", "produto": "IBIZA VELUDO - COR BEGE",                    "qtd": 60,  "total": 7938.60},
    {"pedido": "54265", "produto": "COSTURADA SUEDE - COR BEGE",                 "qtd": 30,  "total": 3969.30},
    {"pedido": "54265", "produto": "COSTURADA SUEDE - COR PRETO",                "qtd": 30,  "total": 3969.30},
    {"pedido": "54265", "produto": "IBIZA CORANO - COR BEGE",                    "qtd": 16,  "total": 2683.04},
    {"pedido": "54265", "produto": "IBIZA CORANO - COR PRETO",                   "qtd": 16,  "total": 2683.04},
    {"pedido": "54265", "produto": "ITALIA VELUDO - COR BEGE",                   "qtd": 30,  "total": 5381.10},
    {"pedido": "54265", "produto": "FONTANA VELUDO - COR BEGE",                  "qtd": 30,  "total": 4661.40},
    {"pedido": "54265", "produto": "MOSCOW BOUCLE - COR BEGE",                   "qtd": 6,   "total": 793.86},
    {"pedido": "54265", "produto": "PUFF ROMA VELUDO - COR BEGE",                "qtd": 10,  "total": 707.70},
    {"pedido": "54265", "produto": "NAMORADEIRA COSTURADA SUEDE - COR BEGE",     "qtd": 5,   "total": 957.00},
    {"pedido": "54265", "produto": "NAMORADEIRA COSTURADA SUEDE - COR PRETO",    "qtd": 10,  "total": 1914.00},
    # Pedido 50630
    {"pedido": "50630", "produto": "KIT 2 POLTRONAS COM PUFF COSTURADO",         "qtd": 20,  "total": 5935.20},
]

df = pd.DataFrame(pedidos)
df["data"] = pd.to_datetime(df["data"])
df["mes"] = df["data"].dt.to_period("M").astype(str)
df["pedido_label"] = df["pedido"] + "\n" + df["data"].dt.strftime("%d/%m/%y")

df_itens = pd.DataFrame(itens_raw)

# ── Sidebar ───────────────────────────────────────────────────────────────────
with st.sidebar:
    st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/3/3a/Moblan.svg/1200px-Moblan.svg.png", use_container_width=True) if False else None
    st.title("Filtros")
    clientes = ["Todos"] + sorted(df["cliente"].unique().tolist())
    cliente_sel = st.selectbox("Cliente", clientes)
    if cliente_sel != "Todos":
        df = df[df["cliente"] == cliente_sel]
        df_itens = df_itens[df_itens["pedido"].isin(df["pedido"])]

# ── Cabeçalho ─────────────────────────────────────────────────────────────────
st.title("Dashboard de Pedidos de Venda")
st.caption("Moblan Decor — Exportação Nadal Milani | Dados: Bling ERP")
st.divider()

# ── KPIs ──────────────────────────────────────────────────────────────────────
total_faturamento = df["total"].sum()
total_pedidos     = len(df)
total_qtd         = df["qtd"].sum()
ticket_medio      = total_faturamento / total_pedidos if total_pedidos else 0

k1, k2, k3, k4 = st.columns(4)
k1.metric("Faturamento Total",   f"R$ {total_faturamento:,.2f}".replace(",", "X").replace(".", ",").replace("X", "."))
k2.metric("Pedidos",             total_pedidos)
k3.metric("Itens Vendidos (un)", f"{total_qtd:,}".replace(",", "."))
k4.metric("Ticket Médio / Pedido", f"R$ {ticket_medio:,.2f}".replace(",", "X").replace(".", ",").replace("X", "."))

st.divider()

# ── Linha 1: Faturamento por pedido + por mês ─────────────────────────────────
col1, col2 = st.columns([3, 2])

with col1:
    st.subheader("Faturamento por Pedido")
    df_sorted = df.sort_values("data")
    fig1 = px.bar(
        df_sorted,
        x="pedido",
        y="total",
        color="cliente",
        color_discrete_map={"TAMIFER S.A": "#1f77b4", "NADAL MILANI": "#ff7f0e"},
        text_auto=False,
        labels={"pedido": "Pedido", "total": "Valor (R$)", "cliente": "Cliente"},
        category_orders={"pedido": df_sorted["pedido"].tolist()},
    )
    fig1.update_traces(texttemplate="R$ %{y:,.0f}", textposition="outside")
    fig1.update_layout(
        yaxis_tickformat=",.0f",
        yaxis_title="Valor (R$)",
        xaxis_title="Nº Pedido",
        legend_title="Cliente",
        margin=dict(t=10),
    )
    st.plotly_chart(fig1, use_container_width=True)

with col2:
    st.subheader("Faturamento por Mês")
    df_mes = df.groupby("mes", as_index=False)["total"].sum().sort_values("mes")
    fig2 = px.line(
        df_mes,
        x="mes",
        y="total",
        markers=True,
        labels={"mes": "Mês", "total": "Valor (R$)"},
    )
    fig2.update_traces(line_color="#2ca02c", marker_size=8)
    fig2.update_layout(
        yaxis_tickformat=",.0f",
        yaxis_title="Valor (R$)",
        xaxis_title="",
        margin=dict(t=10),
    )
    st.plotly_chart(fig2, use_container_width=True)

# ── Linha 2: Quantidade por pedido + top produtos ────────────────────────────
col3, col4 = st.columns([3, 2])

with col3:
    st.subheader("Quantidade Vendida por Pedido")
    fig3 = px.bar(
        df_sorted,
        x="pedido",
        y="qtd",
        color="cliente",
        color_discrete_map={"TAMIFER S.A": "#1f77b4", "NADAL MILANI": "#ff7f0e"},
        labels={"pedido": "Pedido", "qtd": "Quantidade (un)", "cliente": "Cliente"},
        category_orders={"pedido": df_sorted["pedido"].tolist()},
    )
    fig3.update_traces(texttemplate="%{y}", textposition="outside")
    fig3.update_layout(
        yaxis_title="Quantidade (un)",
        xaxis_title="Nº Pedido",
        legend_title="Cliente",
        margin=dict(t=10),
    )
    st.plotly_chart(fig3, use_container_width=True)

with col4:
    st.subheader("Faturamento por Cliente")
    df_cli = df.groupby("cliente", as_index=False)["total"].sum()
    fig4 = px.pie(
        df_cli,
        names="cliente",
        values="total",
        color_discrete_map={"TAMIFER S.A": "#1f77b4", "NADAL MILANI": "#ff7f0e"},
        hole=0.4,
    )
    fig4.update_traces(texttemplate="R$ %{value:,.0f}<br>%{percent}", textposition="outside")
    fig4.update_layout(margin=dict(t=10))
    st.plotly_chart(fig4, use_container_width=True)

# ── Top Produtos ──────────────────────────────────────────────────────────────
st.subheader("Top 10 Produtos por Faturamento")

# Normaliza nomes de produto para agrupar similares
def normaliza(nome):
    mapa = {
        "KIT MONTEVIDEO": "KIT MONTEVIDEO",
        "KIT IBIZA": "KIT IBIZA",
        "ITALIA VELUDO": "ITALIA VELUDO",
        "MOSCOW BOUCLE": "MOSCOW BOUCLE",
        "POLTRONA FONTANA": "POLTRONA FONTANA",
        "POLTRONA MONTEVIDEO SUEDE": "POLTRONA MONTEVIDEO SUEDE",
        "IBIZA VELUDO": "IBIZA VELUDO",
        "IBIZA CORANO": "IBIZA CORANO",
        "FONTANA VELUDO": "FONTANA VELUDO",
        "PUFF ROMA": "PUFF ROMA",
        "NAMORADEIRA": "NAMORADEIRA",
        "POLTRONA ITALIA": "ITALIA VELUDO",
        "CADEIRA MOSCOW": "MOSCOW BOUCLE",
        "COSTURADA SUEDE": "POLTRONA MONTEVIDEO SUEDE",
        "KIT 2 POLTRONAS": "KIT MONTEVIDEO",
    }
    for chave, valor in mapa.items():
        if chave in nome.upper():
            return valor
    return nome.split(" - ")[0].strip()

df_itens["produto_grupo"] = df_itens["produto"].apply(normaliza)
df_top = (
    df_itens.groupby("produto_grupo", as_index=False)
    .agg(faturamento=("total", "sum"), quantidade=("qtd", "sum"))
    .sort_values("faturamento", ascending=False)
    .head(10)
)

fig5 = px.bar(
    df_top,
    y="produto_grupo",
    x="faturamento",
    orientation="h",
    color="faturamento",
    color_continuous_scale="Blues",
    text_auto=False,
    labels={"produto_grupo": "Produto", "faturamento": "Faturamento (R$)"},
)
fig5.update_traces(
    texttemplate="R$ %{x:,.0f}",
    textposition="outside",
)
fig5.update_layout(
    xaxis_tickformat=",.0f",
    coloraxis_showscale=False,
    yaxis=dict(autorange="reversed"),
    margin=dict(t=10),
    height=380,
)
st.plotly_chart(fig5, use_container_width=True)

# ── Tabela de pedidos ─────────────────────────────────────────────────────────
st.subheader("Tabela de Pedidos")
df_tabela = df[["pedido", "data", "cliente", "qtd", "total"]].copy()
df_tabela["data"] = df_tabela["data"].dt.strftime("%d/%m/%Y")
df_tabela["total_fmt"] = df_tabela["total"].apply(
    lambda v: f"R$ {v:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")
)
df_tabela = df_tabela.rename(columns={
    "pedido": "Pedido",
    "data": "Data",
    "cliente": "Cliente",
    "qtd": "Qtd. Itens",
    "total_fmt": "Valor Total",
}).drop(columns=["total"])

st.dataframe(df_tabela, use_container_width=True, hide_index=True)

st.caption("Fonte: Bling - Pedido de Venda (exportado em 15/04/2026)")

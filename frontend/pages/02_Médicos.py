import streamlit as st
import requests
import pandas as pd

# Função para obter os nomes dos clientes
def get_client_names():
    response = requests.get("http://backend:8000/clientes/")
    if response.status_code == 200:
        clientes = response.json()
        # Ordena os nomes dos clientes em ordem alfabética
        return sorted([cliente['nome'] for cliente in clientes])
    else:
        st.error("Erro ao obter os nomes dos clientes")
        return []

# Obtendo os nomes dos clientes
client_names = get_client_names()

with st.expander("Adicionar um Novo Agendamento"):
    # Adiciona uma opção vazia no início da lista de clientes
    client_names.insert(0, "")

    # Selectbox para o nome do paciente, com valor padrão vazio
    nome_cliente = st.selectbox("Nome do Paciente", options=client_names)

    email_selecionado = ''
    if nome_cliente:
        # Função para obter o e-mail do cliente selecionado
        response = requests.get(f"http://backend:8000/clientes/?nome={nome_cliente}")
        if response.status_code == 200:
            cliente = response.json()[0]  # Assumindo que apenas um cliente será retornado
            email_selecionado = cliente.get('email', '')  # Retorna o e-mail do cliente ou uma string vazia se não houver e-mail
        else:
            st.error("Erro ao obter o e-mail do cliente")

    with st.form("new_agendamento"):
        # Preenchendo automaticamente o campo de e-mail do paciente
        email_paciente = st.text_input("Email do Paciente", value=email_selecionado, key="email_paciente")


with st.expander("Obter Detalhes de um Agendamento"):
    nome_cliente = st.text_input("Nome Cliente")
    if st.button("Buscar"):
        response = requests.get(f"http://backend:8000/clientes/nome/{nome_cliente}")
        if response.status_code == 200:
            cliente = response.json()
            df = pd.DataFrame([cliente])

            # Renomear as colunas para nomes mais amigáveis
            df = df.rename(columns={
                "email": "E-mail",
                # Adicione mais renomeações conforme necessário
            })

            # Obter o valor do e-mail
            email_cliente = df["E-mail"].iloc[0] if not df.empty else ""

            # Exibir o DataFrame
            st.dataframe(df)

            # Preencher automaticamente o campo de e-mail
            email_input = st.text_input("E-mail do Paciente", value=email_cliente)
        else:
            st.error("Erro ao buscar os detalhes do cliente. Verifique o nome e tente novamente.")
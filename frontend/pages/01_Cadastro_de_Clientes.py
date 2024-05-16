import streamlit as st
import datetime
import requests
import pandas as pd

st.set_page_config(layout="wide")
st.image("agendar.png", width=200)
st.title("Cadastro de Clientes")

with st.expander('Adicionar um Novo Cliente'):
    with st.form('new_cliente'):
        nome_do_cliente = st.text_input('Nome do Cliente')
        data_nascimento_cliente_input = st.text_input('Data de Nascimento (dd-mm-aaaa)')
        cpf_cliente = st.text_input('CPF')
        uf_cliente = st.text_input('UF')
        cidade_cliente = st.text_input('Cidade')
        bairro_cliente = st.text_input('Bairro')
        rua_cliente = st.text_input('Rua/Logradouro')
        numero_cliente = st.text_input('Número')
        email_cliente = st.text_input('E-mail')
        telefone_cliente = st.text_input('Telefone')

        submit_button = st.form_submit_button('Adicionar Novo Cliente')

# Visualizar Todos os Clientes
with st.expander("Visualizar Clientes"):
    if st.button("Exibir Todos os Clientes"):
        raise

# Obter Detalhes de um Cliente      
with st.expander("Obter Detalhes de um Cliente"):
    get_id = st.number_input("ID do Cliente", min_value=1, format="%d")
    if st.button("Buscar Cliente"):
        raise

# Deletar Cliente
with st.expander("Excluir Cliente"):
    delete_id = st.number_input("ID do Cliente para Exclusão", min_value=1, format="%d")
    if st.button("Excluir Cliente"):
        raise
  
# Atualizar Produto
with st.expander("Atualizar dados do Cliente"):
    with st.form("update_agendamento"):
        update_button = st.form_submit_button("Atualizar Dados")
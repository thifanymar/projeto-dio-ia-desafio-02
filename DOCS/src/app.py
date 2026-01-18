import streamlit as st
from services.blob_service import upload_blob
from services.credit_card_service import analize_credit_card

def configure_interface():
    st.title("upload de arquivos DIO - Desafio 2 - Azure - Fake Doce")
    uploaded_file = st.file_uploader("Escolha um arquivo", type = {"png","jpg","jpeg"})

    if uploaded_file is not None:
        fileName = uploaded_file.name

    #enviar para o blob
    blob_url = upload_blob(uploaded_file,fileName)
    if blob_url:
        st.write(f"arquivo {fileName} enviado com sucesso")
        credit_card_info = analize_credit_card(blob_url) #chamar funcao de cartao de credito
        show_image_and_validation(blob_url,credit_card_info)
    else:
        st.write(f"erro ao enviar o arquivo {fileName}")

def show_image_and_validation(blob_url, credit_card_info):
    st.image(blob_url,caption="img enviada", use_column_width=True)
    st.write("Resultado da validacao:")

    if credit_card_info and credit_card_info["card_name"]:
        st.markdown(f"<h1 style= 'color: green;'> Cartão Válido <h/11>")
        st.write(f"nome do titular: {credit_card_info['card_name']}")
        st.write(f"banco: {credit_card_info['bank_name']}")
        st.write(f"data de validade: {credit_card_info['expiry_date']}")

    else:
        
        st.markdown(f"<h1 style= 'color: green;'> Cartão inválido <h/11>")
        st.write("Este nao e um numero de cartao valido")

if __name__ == "main":
    configure_interface()
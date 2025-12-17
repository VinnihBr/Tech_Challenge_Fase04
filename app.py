import streamlit as st
import pandas as pd
import numpy as np
import joblib
from pathlib import Path

# Configuração da página

st.set_page_config(page_title="Simulador de Obesidade", layout="centered")
st.title("🔬 Simulador de Obesidade")


# Mapeamentos formulário

gender_map = {"Feminino": "Female", "Masculino": "Male"}
yesno_map = {"Sim": "yes", "Não": "no"}
freq_map = {"Não": "no", "Às vezes": "Sometimes", "Frequentemente": "Frequently", "Sempre": "Always"}
transporte_map = {
    "Carro": "Automobile",
    "Moto": "Motorbike",
    "Bicicleta": "Bike",
    "Transporte Público": "Public_Transportation",
    "Caminhando": "Walking"
}

# Formulário

st.header("Formulário")

genero = gender_map[st.selectbox("Gênero", gender_map)]
idade = st.slider("Idade", 10, 100, 20)
altura = st.number_input("Altura (m)", 0.9, 2.5, 1.70, 0.01)
peso = st.number_input("Peso (kg)", 30.0, 400.0, 70.0, 0.1)

hist = yesno_map[st.selectbox("Histórico familiar de obesidade?", yesno_map, key="hist")]
favc = yesno_map[st.selectbox("Consome alimentos calóricos?", yesno_map, key="favc")]

fcvc = st.selectbox("Consumo de vegetais (1=raramente, 2=as vezes, 3=frequentemente)", [1, 2, 3], index=1)
ncp = st.selectbox("Quantas refeições por dia?", [1, 2, 3, 4], index=1)

caec = freq_map[st.selectbox("Consome lanches entre refeições?", freq_map, key="caec")]
smoke = yesno_map[st.selectbox("Fuma?", yesno_map, key="smoke")]

ch2o = st.selectbox("Consumo de água (1=menos de 1 litro, 2= entre 1 a 2 litros, 3=mais de 2 litros)", [1, 2, 3], index=1)
scc = yesno_map[st.selectbox("Monitora calorias?", yesno_map, key="scc")]

faf = st.selectbox("Atividade física (0=nunca, 1= as vezes, 2=frequentemente, 3=sempre)", [0, 1, 2, 3], index=1)
tue = st.selectbox("Uso de tecnologia (0=as vezes, 1= frequentemente, 2=sempre)", [0, 1, 2], index=1)

calc = freq_map[st.selectbox("Consumo de álcool", freq_map, key="calc")]
mtrans = transporte_map[st.selectbox("Meio de transporte", transporte_map)]

# IMC

imc = peso / (altura ** 2)
st.metric("IMC", round(imc, 2))

# DataFrame para predição

X = pd.DataFrame([{
    "Gender": genero,
    "Age": idade,
    "Height": altura,
    "Weight": peso,
    "family_history": hist,
    "FAVC": favc,
    "FCVC": fcvc,
    "NCP": ncp,
    "CAEC": caec,
    "SMOKE": smoke,
    "CH2O": ch2o,
    "SCC": scc,
    "FAF": faf,
    "TUE": tue,
    "CALC": calc,
    "MTRANS": mtrans,
    "IMC": imc
}])

# Carregar modelo e encoder

BASE_DIR = Path(__file__).resolve().parent

model = joblib.load(BASE_DIR / "modelo" / "xgb.joblib")
label_encoder = joblib.load(BASE_DIR / "modelo" / "label_encoder.pkl")

# Tradução final
label_map = {
    "Insufficient_Weight": "Abaixo do peso",
    "Normal_Weight": "Peso normal",
    "Overweight_Level_I": "Sobrepeso (Nível I)",
    "Overweight_Level_II": "Sobrepeso (Nível II)",
    "Obesity_Type_I": "Obesidade (Tipo I)",
    "Obesity_Type_II": "Obesidade (Tipo II)",
    "Obesity_Type_III": "Obesidade (Tipo III)"
}

# Predição

if st.button("Enviar"):
    y_pred = int(model.predict(X)[0])
    label_en = label_encoder.classes_[y_pred]
    label_pt = label_map[label_en]

    st.subheader("Resultado da predição")
    st.markdown(f"### Classe prevista {y_pred}: **{label_pt}**")

    # Probabilidades

    try:
        probs = model.predict_proba(X)[0]
        df_prob = pd.DataFrame({
            "Classe": [label_map[c] for c in label_encoder.classes_],
            "Probabilidade": probs
        }).sort_values("Probabilidade", ascending=False)

        st.dataframe(df_prob.style.format({"Probabilidade": "{:.3f}"}), use_container_width=True)
    except:
        pass

    st.success("Predição realizada com sucesso.")

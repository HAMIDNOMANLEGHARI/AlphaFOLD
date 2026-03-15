import streamlit as st
import py3Dmol
from protein_predictor import predict_structure
from ai_assistant import ask_ai

st.title("AI Protein Lab")

sequence = st.text_area(
    "Enter Protein Sequence",
    "MKTFFVLLLCTFTVVLA"
)

if st.button("Predict Structure"):

    st.write("Running AlphaFold prediction...")

    pdb_file = predict_structure(sequence)

    if pdb_file:

        with open(pdb_file) as f:
            pdb_data = f.read()

        viewer = py3Dmol.view(width=700, height=500)
        viewer.addModel(pdb_data, "pdb")
        viewer.setStyle({"cartoon": {"color": "spectrum"}})
        viewer.zoomTo()

        st.components.v1.html(viewer._make_html(), height=500)

        st.success("Structure predicted!")

    else:
        st.error("Prediction failed.")

st.header("Ask AI about this protein")

question = st.text_input("Ask a biology question")

if st.button("Ask AI"):

    answer = ask_ai(question, sequence)

    st.write(answer)

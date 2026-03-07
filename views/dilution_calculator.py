import streamlit as st

from functions.verdunnung import berechne_verduennung

# Titel
st.title("🧪 Verdünnungsrechner")



st.divider()

st.header("Eingabe der Werte")

# Formular
with st.form("verdunnungs_form"):
    c1 = st.number_input(
        "Anfangskonzentration c1 (mol/L)",
        min_value=0.0,
        step=0.1
    )

    c2 = st.number_input(
        "Zielkonzentration c2 (mol/L)",
        min_value=0.0,
        step=0.1
    )

    v2 = st.number_input(
        "Zielvolumen V2 (mL)",
        min_value=0.0,
        step=1.0
    )

    berechnen = st.form_submit_button("Berechnen")

st.divider()

# Ergebnisbereich
if berechnen:

    v1, losungsmittel = berechne_verduennung(c1, c2, v2)

    if v1 is not None:

        st.success(f"Benötigtes Volumen der Stammlösung: {v1:.2f} mL")
        st.info(f"Benötigtes Volumen des Lösungsmittels: {losungsmittel:.2f} mL")

        st.subheader("Grafische Darstellung")

        chart_data = {
            "Stammlösung": v1,
            "Lösungsmittel": losungsmittel
        }

        st.bar_chart(chart_data)

        st.caption("Formel: c1 * V1 = c2 * V2")

    else:
        st.warning("Fehler: c1 darf nicht 0 sein.")


# mind. 5 von st.form etc !
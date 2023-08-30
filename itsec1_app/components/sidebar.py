import streamlit as st


def sidebar():
    with st.sidebar:
        st.markdown("## Ziel der App")
        st.markdown(
            "Diese App wurde entwickelt, um Studierenden dabei zu helfen, den Universitätskurs \"IT-Sicherheit 1\" zu verstehen, indem Fragen zu den Folien und Screencasts gestellt werden können."
        )
        st.markdown("---")
        st.markdown("## Haftungsausschluss")
        st.markdown(
            "Diese App sollte vorsichtig verwendet werden. Bei Verwendung solltest du dir bewusst sein, dass möglicherweise Antworten falsch sein könnten. Wir bitten dich daher darum, alle Fragen/Antworten sorgfältig zu prüfen."
        )
        st.markdown("---")
        st.markdown("## Wer ist für den Inhalt verantwortlich?")
        st.markdown(
            "Der Inhalt dieser App wird von dem [Lehrstuhl für Informationssysteme (Prof. Dr. Günther Pernul)](https://www.uni-regensburg.de/informatik-data-science/wi-pernul/startseite/index.html) an der Universität Regensburg gestellt."
        )
        st.markdown("## Kontaktperson")
        st.markdown(
            "Philip Empl (philip.empl@ur.de)"
        )


# IT Security 1 Chatbot

## Zielsetzung
Das Ziel dieses Projekts ist es, einen Chatbot für IT-Security 1 und VAWI Unterlagen zu entwickeln. Der Chatbot soll mithilfe von Vorlesungsfolien, Screencasts, PDFs und YouTube-Links in der Lage sein, dir bei Fragen relevante und hilfreiche Antworten unter Verwendung der genannten Quellen zu bieten. Der Chatbot sollte in jeder Antwort die entsprechenden Stellen aus den genannten Quellen (Vorlesungsfolien, Screencasts, PDFs, YouTube-Links) zitieren und einen Link zu der jeweiligen Quelle bereitstellen. Dies ermöglicht den Benutzern, die Antwort nachzuvollziehen und weitere Informationen zu erhalten.

## Anforderungen
1. **On-Premise Lösung**: Der Chatbot soll auf einer On-Premise-Infrastruktur betrieben werden, um Kosten zu minimieren und deine Datenhoheit zu wahren.

2. **Private Sprachmodelle**: Verwende private Sprachmodelle wie "GPT4All" anstelle von OpenAI GPT, um den Datenschutz zu gewährleisten.

3. **Docker Container**: Für das einfache Deployment, d.h. Starten/Stoppen der einzelnen Services, sollen Docker Container verwendet werden.

4. **Open Source**: Nutze ausschließlich Open Source Lösungen für die Entwicklung des Chatbots.

## Entwicklungsressourcen
- Python
- [Docker Compose](https://www.docker.com/blog/build-and-deploy-a-langchain-powered-chat-app-with-docker-and-streamlit/)
- [LangChain](https://github.com/langchain-ai/langchain)
- [Flowise JavaScript UI](https://github.com/FlowiseAI/Flowise)
- [Langflow Python UI](https://github.com/logspace-ai/langflow)
- GPT Modelle von [Hugging Face](https://huggingface.co)
- [UI Chainlit](https://github.com/Chainlit/chainlit)
- Lokales LLM (Local Language Model) von [GitHub Repository](https://github.com/imartinez/privateGPT)
- [Multi Modal Search](https://python.langchain.com/docs/use_cases/more/agents/agents/multi_modal_output_agent)
- [Citations](https://medium.com/@yotamabraham/in-text-citing-with-langchain-question-answering-e19a24d81e39)
- [Postgresql](https://www.postgresql.org)
- [pgvector](https://github.com/pgvector/pgvector)
- [Jina](https://github.com/jina-ai/jina)
- [Langchain Serve](https://github.com/jina-ai/langchain-serve)

## Schritte
1. **Vorbereitung**: Installiere die benötigten Abhängigkeiten wie Python und die erforderlichen Bibliotheken aus den bereitgestellten Links.

2. **Chain-Erstellung**: Nutze Flowise, um Chains aus den vorhandenen Materialien zu erstellen, die als Grundlage für den Chatbot dienen.

3. **Integration von GPT Modellen**: Verwende die GPT Modelle von Hugging Face, um intelligente Antworten zu generieren. Integriere dabei UI Chainlit, um die Nutzerschnittstelle zu gestalten.

4. **Integration von Local LLM**: Implementiere das lokale Sprachmodell aus dem Local Language Model Projekt, um private und datenschutzfreundliche Interaktionen zu ermöglichen.

5. **Produktivsetzung**: Setze den Chatbot in einer Produktivumgebung mit Jina und Langchain Serve auf, um den Chatbot für Kursteilnehmer:in zugänglich zu machen.
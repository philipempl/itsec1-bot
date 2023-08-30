# IT Security 1 Chatbot

## Zielsetzung
Das Ziel dieses Projekts ist die Entwicklung eines Chatbots für IT-Security 1 und VAWI Unterlagen. Der Chatbot wird durch Vorlesungsfolien, Screencasts, PDFs und YouTube-Links Informationen bereitstellen und bei Fragen hilfreiche Antworten generieren. Bei jeder Antwort werden passende Abschnitte aus den genannten Quellen (Vorlesungsfolien, Screencasts, PDFs, YouTube-Links) zitiert und verlinkt, um den Nutzern das Verständnis zu erleichtern und zusätzliche Informationen anzubieten.

## Anforderungen
1. **On-Premise Lösung**: Der Chatbot wird auf einer On-Premise-Infrastruktur betrieben, um Kosten zu minimieren und Datenschutz zu gewährleisten.

2. **Private Sprachmodelle**: Zum Schutz der Privatsphäre werden private Sprachmodelle wie "GPT4All" eingesetzt, anstelle von OpenAI GPT.

3. **Docker Container**: Für einfaches Deployment (Starten/Stoppen der Services) werden Docker Container verwendet.

4. **Open Source**: Die Entwicklung des Chatbots erfolgt ausschließlich mithilfe von Open Source Lösungen.

## Entwicklungsressourcen
- Programmiersprache: Python
- [Docker Compose](https://www.docker.com/blog/build-and-deploy-a-langchain-powered-chat-app-with-docker-and-streamlit/)
- [LangChain](https://github.com/langchain-ai/langchain)
- [Flowise JavaScript UI](https://github.com/FlowiseAI/Flowise)
- [Langflow Python UI](https://github.com/logspace-ai/langflow)
- GPT Modelle von [Hugging Face](https://huggingface.co)
- [UI Chainlit](https://github.com/Chainlit/chainlit)
- Lokales LLM (Local Language Model) von [GitHub Repository](https://github.com/imartinez/privateGPT)
- [Multi Modal Search](https://python.langchain.com/docs/use_cases/more/agents/agents/multi_modal_output_agent)
- [Citations](https://medium.com/@yotamabraham/in-text-citing-with-langchain-question-answering-e19a24d81e39)
- Datenbank: [Postgresql](https://www.postgresql.org)
- Vektorähnliche Daten in Postgresql: [pgvector](https://github.com/pgvector/pgvector)
- Suchplattform: [Jina](https://github.com/jina-ai/jina)
- Dienst für Langchain: [Langchain Serve](https://github.com/jina-ai/langchain-serve)

## Schritte
1. **Vorbereitung**: Installieren der benötigten Abhängigkeiten wie Python und die empfohlenen Bibliotheken.

2. **Chain-Erstellung**: Erstellen von Chains mit Flowise basierend auf vorhandenen Materialien als Grundlage für den Chatbot.

3. **GPT Modelle integrieren**: Integration der GPT Modelle von Hugging Face für intelligente Antworten, wobei die Benutzeroberfläche mit UI Chainlit gestaltet wird.

4. **Lokales LLM integrieren**: Einbinden des lokalen Sprachmodells aus dem Local Language Model Projekt für private und datenschutzfreundliche Interaktionen.

5. **Produktivsetzung**: Den Chatbot für Kursteilnehmer:innen mit Jina und Langchain Serve in einer Produktivumgebung bereitstellen.

## Deployment

Folgen Sie diesen Schritten, um die bereitgestellten Dienste mit Docker Compose auszuführen:

1. **Docker und Docker Compose installieren:**

   Stellen Sie sicher, dass Docker und Docker Compose auf Ihrem System installiert sind. Falls nicht, können Sie sie von der offiziellen Docker-Website herunterladen und installieren: [Docker](https://www.docker.com/) und [Docker Compose](https://docs.docker.com/compose/install/).

2. **Repository klonen:**

   Klonen Sie dieses Repository auf Ihre lokale Maschine.

3. **Dienste starten:**

   Starten Sie die in der Datei `docker-compose.yml` definierten Dienste mit dem folgenden Befehl:

   ```bash
   docker-compose up -d
   ```

   Die Option `-d` steht für den "detach"-Modus, der die Dienste im Hintergrund ausführt.

4. **Zugriff auf Benutzeroberflächen:**

   Nach dem Start der Dienste können Sie auf die verschiedenen Benutzeroberflächen über die folgenden URLs zugreifen:

### Erreichbare Benutzeroberflächen (UIs)

1. **IT-Sicherheitsbot-Benutzeroberfläche (`itsec1-bot`):**

   Die Benutzeroberfläche des IT-Sicherheitsbots ist über einen Webbrowser zugänglich, indem Sie folgende Adresse aufrufen:

   ```
   http://localhost:8080
   ```

   Diese Oberfläche ermöglicht die Interaktion mit dem IT-Sicherheitsbot.

2. **Benutzeroberfläche des Sprachverarbeitungstools (`langflow`):**

   Die Benutzeroberfläche des Sprachverarbeitungstools erreichen Sie unter:

   ```
   http://localhost:7860
   ```

   Hier stehen die Funktionen des `langflow` Dienstes für die Sprachverarbeitung zur Verfügung.

3. **Benutzeroberfläche der PostgreSQL-Datenbank:**

   Es gibt keine direkte Benutzeroberfläche für die PostgreSQL-Datenbank. Der Zugriff erfolgt über PostgreSQL-Client-Tools oder -Bibliotheken.

4. **Benutzeroberfläche für die Hervorhebung von Code-Syntax (`chroma`):**

   Die Benutzeroberfläche für den Dienst zur Hervorhebung von Code-Syntax ist erreichbar unter:

   ```
   http://localhost:8000
   ```

   Diese Oberfläche ermöglicht es, die Funktionen des `chroma` Dienstes zur Code-Syntax-Hervorhebung zu testen und zu nutzen.

### Beenden der Dienste

Um die Dienste zu stoppen und zu entfernen, führen Sie den folgenden Befehl im Verzeichnis aus, in dem sich die Datei `docker-compose.yml` befindet:

```bash
docker-compose down
```

Dadurch werden die Dienste gestoppt und die dazugehörigen Container, Netzwerke und Volumes entfernt.

## Lizenz
Dieses Projekt ist unter der [MIT Lizenz](https://github.com/philipempl/itsec1-bot/LICENSE) veröffentlicht.
#!/bin/sh

# Start the ollama server
./bin/ollama serve &

# Wait for the server to start (you can adjust the sleep time as needed)
sleep 5

# Add your custom commands here
curl -X POST http://ollama:11434/api/pull -d '{"name": "llama2"}'
./bin/ollama create alice -f ./Modelfile

tail -f /dev/null
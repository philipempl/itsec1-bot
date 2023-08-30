FROM python:3.10-slim

RUN apt-get update && apt-get install gcc g++ git make -y

RUN pip install langflow[local]

CMD ["langflow", "--host", "0.0.0.0", "--port", "7860"]
FROM python:3-alpine

RUN apk add --no-cache git
RUN git clone https://github.com/um-computacion-tm/ajedrez-2024-AgusCorren.git ajedrez-2024-aguscorren


WORKDIR /ajedrez-2024-aguscorren

RUN pip install -r requirements.txt

CMD ["sh", "-c", "coverage run -m unittest discover tests && coverage report -m && python main.py"]

# docker buildx build -t ajedrez-2024-aguscorren . --no-cache
# docker run -i ajedrez-2024-aguscorren
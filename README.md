# pratica-scapy
Este experimento tem como objetivo capturar e analisar pacotes de rede enquanto um vídeo é assistido pela Internet, utilizando a biblioteca Scapy. A partir dessa captura, será possível identificar parâmetros como latência, jitter, taxa de perda de pacotes e variação no throughput da conexão.

1. É preciso criar um ambiente virtual em python para poder instalar as bibliotecas:
```
python3 -m venv scapy-env
source scapy-env/bin/activate
pip install scapy
pip install numpy
```


# MyQRCode

Gerador de QRCode em Python. A imagem é salva na pasta `QR Base` que é criada pelo próprio programa e o usuário tem a autonomia para:

* Escolher o protocolo de navegação que gostaria de usar - `http://` ou `https://`;
* Nome do arquivo em PNG que será gerado com o QRCode;
* Escala de tamanho da imagem do QRCode.

>É recomendado o uso da escala de 1 até 100. Sendo:
<br> Escala 1 = Imagem QRCode de 41x41px.
<br> Escala 10 = Imagem QRCode de 410x410px.
<br> Escala 100 = Imagem QRCode de 4100x4100px.
<br><br> Quanto maior a escala, maior o tempo de salvamento do arquivo.

## Bibliotecas Necessárias:

É recomendado a execução do programa em ambiente virtual

### VirtualEnv:
`pip install virtualenv`

### PyQRCode:
`pip install pyqrcode`

### PyPNG:
`pip install pypng`
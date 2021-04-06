# Descrição do Hardware

##  1. Lista de Materiais:

### * NodeMCU ESP8266 x1;
<img src = "https://cdn.awsli.com.br/600x700/468/468162/produto/19414026/modulo-wifi-esp8266-nodemcu-esp-12f-nova-versao-1d9de0c2.jpg" alt = "NodeMCU ESP8266" width = "150" />

### * Sensor de umidade do solo x1;
<img src = "https://cdn.awsli.com.br/600x700/468/468162/produto/19414371/1ceaf2d245.jpg" alt = "Sensor de umidade do solo" width = "150" />

### * Resistor de 4,7 kΩ x1;
<img src = "https://cdn.iset.io/assets/00572/produtos/5047/resistor.jpg" alt = "Resistor" width="150"/>

### * Módulo relé SRD-05VDC-SL-C x1;
<img src = "https://gloimg.gbtcdn.com/gb/2014/201406/source-img/1401843493297-P-1752307.jpg" alt="Módulo relé SRD-05VDC-SL-C" width="150"/>

### * Mini bomba d'água de 5V x1;
<img src = "https://cdn.awsli.com.br/600x700/468/468162/produto/19414037/mini-bomba-submersa-5v-p-agua-26664ccb.jpg" alt = "Bomba d'água 5V" width = "150"/>

### * Jumper cables;
<img src = "https://cdn.sparkfun.com//assets/parts/1/2/2/4/2/13870-01.jpg" alt = "Jumper Cables" width = "150"/>


## 2. Esquemática:
<img src="https://github.com/digopp22/mackenzie-projeto-regador_automatico_nodemcu/blob/master/doc/Capturar.png" alt="NodeMCU ESP8266" width="50" height = "50"/>


## 3. Funcionalidade:
O sensor de umidade obtém os dados necessários que são enviados à plataforma Blynk. Na interface criada pelo grupo, 
há dois gráficos: um, mostra qual o nível da umidade e o outro mostra um gráfico com os níveis dela no último tempo.
Há um botão que, ao ser acionado, liga a bomba remotamente de forma que a água seja utilizada para regar o solo. 
Através do sensor de umidade e do display LCD, da interface, é possível saber se foi o suficiente a rega ou se ainda é necessária.


O projeto é totalmente escalável para diferentes situações: desde plantas com necessidades diferentes (no código original, o grupo fez
um caso geral) até sistemas que necessitam de maior volume de água - e então - a aplicação seria desenvolvida com outra bomba. Há a possibi
lidade de utilizar outros sensores, como o de temperatura e luminosidade, para que a experiência seja aprimorada.

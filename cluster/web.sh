#!/bin/bash
# Author: [Marcelino Macedo]
# Date: 2023-02-20
# Description: Script para instalação do Apache2 e criar um novo index.html padrao

# atualização dos repositorios no ubuntu
sudo apt update -y
# instalação do apache2
sudo apt install apache2 -y
# renomear o arquivo index.html padrão
sudo mv /var/www/html/index.html /var/www/html/index.html.bkp
#virar root
sudo -i
# criar um novo index.html padrão
sudo echo "<html><body><h1> servidor web 1</h1></body></html>" > /var/www/html/index.html
# reiniciar o serviço do apache2
sudo systemctl restart apache2

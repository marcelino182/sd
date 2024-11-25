#!/bin/bash
# Author: [Marcelino Macedo]
# Date: 2023-02-20
# Description: Script para instalação do HAPROXY no ubuntu 22.04

# atualização dos repositorios no ubuntu
sudo apt update -y
# instalação do haproxy
sudo apt install haproxy -y
# copiar o conteudo do modelo e adicionar ao final do arquivo
# por motivo de segurança fazer um backup do arquivo original do haproxu
sudo cp /etc/haproxy/haproxy.cfg /etc/haproxy/haproxy.cfg.bkp
# editar o arquivo com o conteúdo do modelo
sudo cat haproxy.cfg >> /etc/haproxy/haproxy.cfg
#editar o arquivo substituindos os ips corretos das máquinas do servidores web
sudo nano /etc/haproxy/haproxy.cfg
#reiniciar o servidor haproxy
sudo systemctl restart haproxy
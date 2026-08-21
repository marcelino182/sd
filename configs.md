# ⚙️ Configurações básicas do servidor

## ⌨️ Mudar layout do teclado para ABNT2
```bash
sudo -i
nano /etc/default/keyboard
```
Conteúdo do arquivo
```ini
XKBMODEL="pc105"
XKBLAYOUT="br"
XKBVARIANT="abnt2"
XKBOPTIONS=""
```
CTRL + X e confirme para salvar com ENTER
Reiniciar o servidor para que as alterações sejam aplicadas
```bash
reboot
```
## Mudar o endereço IP do servidor
Aproveitando o arquivo padrão de configuração com modelo
```bash
mv /etc/netplan/00-installer-config.yaml /etc/netplan/01-netcfg.yaml
nano /etc/netplan/01-netcfg.yaml
```
conteúdo do arquivo
```yaml
network:
  version: 2
  renderer: networkd
  ethernets:
    enp3s0:                  # Substitua pelo nome da sua placa de rede
      dhcp4: yes             # Mantém IP dinâmico para DNS e Gateway
      addresses:
        - 192.168.20X.Y/24   # IP fixo desejado e máscara de rede (/24)
```
Aplicar as configurações
```bash
netplan apply
ip a
```

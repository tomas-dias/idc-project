# To install or update nvm, you should run the install script. 
# To do that, you may either download and run the script manually, or use the following cURL or Wget command:
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.1/install.sh | bash

# Installing Node-RED
sudo npm install -g --unsafe-perm node-red node-red-admin

# Open up a port on firewall. Node-RED defaults to using port 1880.
sudo ufw allow 1880

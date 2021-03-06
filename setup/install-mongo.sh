# Setup MongoDB

# Import the public key used by the package management system.
wget -qO - https://www.mongodb.org/static/pgp/server-5.0.asc | sudo apt-key add -

# Create a list file for MongoDB.
echo "deb [ arch=amd64,arm64 ] https://repo.mongodb.org/apt/ubuntu focal/mongodb-org/5.0 multiverse" | sudo tee /etc/apt/sources.list.d/mongodb-org-5.0.list

# Reload local package database.
sudo apt update

# Install the MongoDB packages.
sudo apt install -y mongodb-org

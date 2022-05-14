# Setup MongoDB

# Import the public key used by the package management system.
wget -qO - https://www.mongodb.org/static/pgp/server-5.0.asc | sudo apt-key add -

# Create a list file for MongoDB.
echo "deb [ arch=amd64,arm64 ] https://repo.mongodb.org/apt/ubuntu focal/mongodb-org/5.0 multiverse" | sudo tee /etc/apt/sources.list.d/mongodb-org-5.0.list

# Reload local package database.
sudo apt update

# Install the MongoDB packages.
sudo apt install -y mongodb-org

sudo apt install python3-pip

pip3 install pymongo

python3 setup-db.py

mongoimport --uri "mongodb://127.0.0.1:27017/" --db "battery-cycles" --file "offline_.json"

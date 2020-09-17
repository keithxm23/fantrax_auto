
sudo apt-get install firefox

wget https://github.com/mozilla/geckodriver/releases/download/v0.27.0/geckodriver-v0.27.0-linux64.tar.gz

tar xvzf geckodriver-v0.27.0-linux64.tar.gz

mv geckodriver ~/.local/bin

export PATH=$PATH:/home/vagrant/.local/bin
# fantrax_auto

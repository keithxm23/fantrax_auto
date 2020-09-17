
export PATH="/home/vagrant/.pyenv/bin:$PATH"
export FANTRAX_U=""
export FANTRAX_P=""


eval "$(pyenv init -)"
eval "$(pyenv virtualenv-init -)"

pyenv activate fantrax
python /home/vagrant/fantrax_auto/waive_em_all.py

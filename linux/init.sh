# these are the steps to initialize the app server
sudo su -
apt-get update
apt-get instally python3
apt-get install gunicorn3
apt-get install nginx
apt-get install pip
apt-get install awscli
apt install awscli
apt install python3-flask
pip3 install flask
pip3 install boto3


# configure aws cli
sudo su - ubuntu
# must input the keys manually
# No storing keys on github!
aws configure   


#create a madlib service manually using the files in git
sudo su -
vim /etc/systemd/system/madlib.service
sudo systemctl daemon-reload

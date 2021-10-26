# This file show how we setup the jenkins server

sudo su -
yum update -y
yum install jenkins java-1.8.0-openjdk-devel -y
yum install daemonize -y
amazon-linux-extras install epel -y
yum install jenkins java-1.8.0-openjdk-devel
yum-config-manager --enable epel
systemctl daemon-reload 
systemctl start jenkins
sudo systemctl status jenkins
less /var/lib/jenkins/secrets/initialAdminPassword
yum install git

yum install amazon-cloudwatch-agent
cd /opt/aws/amazon-cloudwatch-agent/
./amazon-cloudwatch-agent-config-wizard
systemctl enable amazon-cloudwatch-agent.service 
systemctl start amazon-cloudwatch-agent.service

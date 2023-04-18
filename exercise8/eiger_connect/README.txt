
cp config $HOME/.ssh
cp id_rsa $HOME/.ssh
chmod 644 $HOME/.ssh/id_rsa
chmod 644 $HOME/.ssh/config
chmod 700 $HOME/.ssh/id_rsa
ssh eiger

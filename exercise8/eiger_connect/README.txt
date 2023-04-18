
cp /cluster/scratch/danielep/Eiger_students/config $HOME/.ssh
cp /cluster/scratch/danielep/Eiger_students/id_rsa $HOME/.ssh
chmod 644 $HOME/.ssh/id_rsa
chmod 644 $HOME/.ssh/config
chmod 700 .ssh/id_rsa
ssh eiger


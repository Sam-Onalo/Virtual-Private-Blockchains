echo "INITIALISING THE VPBC COIN ASSET TRANSFER PROTOCOL..."

multichain-cli Node1 listassets  > assets-acc.txt

echo "GENERATING WALLET BALANCE"

multichain-cli Node1 gettotalbalances > NodeWallet.txt 

echo "WALLET BALANCE STORED IN >> NodeWallet.txt"

#echo "ENTER THE FOLLOWING COMMANDS TO SEND ASSETS TO NODE 2 >>multichain-cli Node1 sendasset 12kvaMoupcfYKaznexnhXkux56hQmnD8DiiJza VPBCcoin [ENTER AMOUNT]//"

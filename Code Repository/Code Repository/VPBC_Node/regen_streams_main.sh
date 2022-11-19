
echo 'INITIATING VPBC STREAM GENERATION...'
multichain-cli Node1 getinfo  > getinfo.txt

echo 'Details of the VPBC Node1 is stored in getinfo.txt'

multichain-cli Node1 liststreams > liststreams.txt

echo 'Details of the VPBC streams is stored in liststreams.txt'

#multichain-cli subscribe vpbc > vpbcsubscribe.txt

#echo 'Details of the VPBC streams is stored in liststreams.txt'

multichain-cli Node1 liststreamitems vpbc > vpbcliststreamitems.txt

multichain-cli Node1 liststreamitems vpbc

echo 'Details of the VPBC stream items is stored in vpbcliststreamitems.txt'

echo 'USE THE COMMAND >> python3 sss_srecon.py << TO INITIATE SECRET RECONSTRUCTION'

echo 'Follow the prompting to enter the secret according tot he coordinates (X,Y)'

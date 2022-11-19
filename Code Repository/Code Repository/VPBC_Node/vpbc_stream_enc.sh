
echo 'INITIATING THE VPBC STREAM ENCODING PROCEDURE...'
multichain-cli Node1 getinfo  > getinfo.txt

#echo 'Details of the VPBC Node is stored in getinfo.txt'

#multichain-cli create stream vpbc '{"restrict":"write"}' > streamtxn.txt

#echo 'transaction ID of the VPBC stream is stored in streamtxn.txt'

#multichain-cli listpermissions vpbc.* > vpbclistedpermissions.txt

#echo 'Details of the VPBC Node stream persmissions is stored in vpbclistedpermissions.txt'

echo 'transaction ID of the published txn on VPBC stream is stored in streamtxn.txt'

multichain-cli Node1 liststreams > liststreams.txt

echo 'Details of the VPBC streams is stored in liststreams.txt'

#multichain-cli subscribe vpbc > vpbcsubscribe.txt

#echo 'Details of the VPBC streams is stored in liststreams.txt'

multichain-cli Node1 liststreamitems vpbc > vpbcliststreamitems.txt 

echo 'Details of the VPBC stream items is stored in liststreams.txt'

#multichain-cli grant ... send 

echo " ENTER THE FOLLOWING COMMANDS TO ENCODE THE SECRET SHARES TO THE  VPBC STREAM >> multichain-cli Node1 publish vpbc msg1 '{''json'':{''ENTER SHARE X'':''ENTER SHARE Y''}}' > vpbctxn1.txt//"

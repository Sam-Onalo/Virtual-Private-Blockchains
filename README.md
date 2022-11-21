# Virtual Private Blockchains

##Introduction
Blockchain technology, while maturing, is still lacking features that would be considered indispensable in realworld business applications. In particular, the lack of transaction confidentiality in a public blockchain is a challenging problem. A possible solution might be the concept of a private blockchain. However, maintaining such permissioned blockchains requires resources, depends on a central authority and contradicts the original philosophy of pioneering blockchain systems such as Bitcoin. In this paper, the concept of a Virtual Private Blockchain (VPBC) is proposed as a mechanism to create a blockchain architecture with properties akin to those of a private blockchain, however leveraging existing public blockchain functionality. A VPBC can be set up between individuals or organisations, does not require any significant administrative maintenance, inherits all the functionality from the public blockchain, and achieves anonymity and transaction confidentiality with respect to any public blockchain node who does not belong to the VPBC. Building on this theoretical concept, it is then shown how the cryptographic technique of secret sharing can be used in order to implement a simple VPBC architecture. This project presents a proof-of-concept architecture desgned on the Mulitchain blokchain environment to indicate the prospect of the VPBCs for potential real-world application scenarios.


## Technologies
***
A list of technologies used within the project:
* [Multichain](https//wwww.multichain.com): Version 2.3.1 
* [Python](https://www.python.org/): Version 3.11
* [Linux-Ubuntu Desktop](https://ubuntu.com/): Version 16.04 
* [Oracle VirtualBox](https://www.oracle.com/virtualization/): Version 6.2
* [Link to Download Ubuntu Seed Virtual Machines ](https://drive.google.com/drive/folders/1B-Srhl2rZsEQ39SAG-5jGtmb5ByP0mfu?usp=sharing): Last update: 20/11/2022

## How to Run the VPBC implementation based on predefined Seed Virtual Machines
Follow these instructions to initiate the process.

### NODE 1
```
$ Start Node 1
$ Open the terminal in the  ./Desktop  directory
$ Enter the command sudo su 
$ Username: vpbc
$ password: abc123
```
#### Enter the following commands to run the Random Splitting process:
```
$ ./init_node.sh
$ ./begin_rsg.sh
$ ./asset_transfer.sh
$ ./check_balance.sh
```
#### Enter the following commands to run the Secret Sharing process:
```
$ ./sss_sg_main.sh
$ ./vpbc_stream_enc.sh
$ ./stream_check.sh
```
### NODE 2
```
$ Start Node 2
$ Open the terminal in the  ./Desktop  directory
$ Enter the command sudo su 
$ Username: vpbc
$ password: abc123
```
#### Enter the following commands to run the secret recovery process:
```
$ ./init_node.sh
$ ./check_balance.sh
```
#### Enter the following commands to run the secret reconstruction process:
```
$ ./regen_stream_main.sh
```
 

## How to Build the VPBC Architecture from Source Codes

### Dependencies
Download and install Multichain:
 #### LINUX
Open a terminal in the desktop and enter the following commands:
```
$ sudo su -
# cd /tmp
# wget https://www.multichain.com/download/multichain-2.3.1.tar.gz 
# tar -xvzf multichain-2.3.1.tar.gz
# cd multichain-2.3.1
# mv multichaind multichain-cli multichain-util /usr/local/bin
# exit
```
#### WINDOWS
***
* Multichain is compatible with Windows 7-10, howvever Windows 10 is the recommended version for this project.
* Go to the Multichain website and download the 'Community Download' version from: https://www.multichain.com/download-install/
* To Install and Run :
> 1. Find download folder
> 2. Copy to target directory (e.g. on H: drive)
> 3. Change directory to target folder
* Use e.g. cd "\DATA\CI7100\MultiChain"
* Check out the online (documentation)[https://www.multichain.com/getting-started/]
***

#### Create Private Blockchain Nodes
***
* Use the `multichain-util create Node1` command to create the first node with sample chain name Node1. 
* Repeat on the second node with a different chain name, say Node2.
* Use  `multichaind Node1 -daemon ` to activate Node1, 
* Repeat on Node2 with Node2 as chain name.2
* Both nodes should publish connection addresses in the follwing format - `chainname@IP address:Port number`
* Use `multichaind Node1@IPaddress:PortNumber` on Node2 to connect to Node1
* Now check the wallet address published on node 2 (say wallet address is Y) and use address to grant permissions on Node1 to connect to Node2
* Use  `multichain-cli Node1 grant Y connect,send,receive` on Node1 to grant connectivity and transactional permissions
* Use `multichaind Node1 -daemon` on Node2 to connect to Node1. Node2 should connect successfully.
* Use `multichain-cli Node1 getinfo` on Node1 and Node2 to view full blockchain parameters and further confirm that Node2 is connected to Node1.
***

#### Connecting Multichain Blockchain Nodes as shown:
***
* Create and send Assets on  Multichain nodes assuming both nodes have been set up and are running smoothly and connected.
* Use the `multichain-cli Node1 listpermissions issue`command to view the wallet ID of the first node with sample chain name Node1.Let's call the wallet ID of Node1 = X 
* Now we’ll create a new asset on this node with 1000 units, each of which can be subdivided into 100 parts, sending it to itself: Use`multichain-cli Node1 issue X  asset1 1000 0.01`
* On both servers, verify that the asset named asset1 is listed: Use `multichain-cli Node1 listassets` on Node1 and change the chain name for the second node.
* Now check the asset balances on each server. The first should show a balance of 1000, and the second should show no assets at all: Use `multichain-cli Node1 gettotalbalances` 
* Use `multichain-cli Node2 getpeerinfo`  on Node2 to call up the wallet ID and use for the next command. Let's call that Y
* On the Node1, now try sending 100 units of the asset to the second server’s wallet: `multichain-cli Node1 sendasset Y asset1 100 `
* Use `multichain-cli Node1 grant Y receive` to accept the transaction if not already done when initially connecting Node1 and Node2
* Now try sending the asset again, and it should go through: `multichain-cli Node1 sendasset Y asset1 100` 
* Now check the asset balances on each server, including transactions with zero confirmations. They should be 900 and 100 respectively: Use `multichain-cli Node1 gettotalbalances 0`
* You can also view the transaction on each node and see how it affected their balances: `multichain-cli Node1 or Node2 listwallettransactions 1` 
#### Definition I - Generating the Random splits of Asset
* Create a python module with the following code
```
> Random Asset.py
import random
def random_by_number(number, min_random, max_random, spaces=1, precision=2):
if spaces <= 0:
return number
random_numbers = [random.uniform(min_random, max_random) for i in range(0, spaces)]
increment_number = (number - sum(random_numbers)) / spaces
return [round(n + increment_number, precision) for n in random_numbers]
number = int(input ("Enter the secret amount:"))
spaces = int(input ("Enter the number of shares:"))`
max_random = number / spaces
min_random = max_random * 0.6
random_numbers = random_by_number(number, min_random, max_random, spaces=spaces, precision=2)
print(random_numbers)
print(len(random_numbers))
print(sum(random_numbers))
```
#### Defition II - Generating the Shares from the Secret
* Create a python module with the following node
```

```


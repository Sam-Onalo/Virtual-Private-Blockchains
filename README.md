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
 

## How to Build the VPBC Architecture from Source Code

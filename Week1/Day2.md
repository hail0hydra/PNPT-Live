# Day 2 Notes

<br>
<br>

## Starting and Stopping services
<br>
<br>

- `ifconfig` for `ip address` ironic huh! 

- Entered IP Address in `Firefox` and redirected because nothing there.

<br>

### Starting a Web server

>#### Apache2 web server

- `service apache2 start` : staring it

 - `refresh` the page at firefox. Bingo! (Default page of apache2)

  - default location `/var/www/html` and there is `index.html`

<br>

>#### python web server

- `python -m http.server 80` (as sudo I guess)

- go to `firefox`. Jackpot!


<br>
<br>

---

>- `sudo systemctl enable/disable <service name>` load/unload on reboot/startup.

---

<br>

### Computer Networking

<br>
<br>

- Critical Foundation is Networking

- New version of `ifconfig` is  `ip a`

    - getting lot of information `ipv4, ipv6, mac, etc`

<br>

### Layer 3
- We talked about IP address and `(25:15) - ipv4`

```text
128 64 32 16 8 4 2 1
 1   1  1  1 1 1 1 1 = 255

128 64 32 16 8 4 2 1
 0   0  0  0 0 1 1 1 = 7
```

- total  IPV4s = 2**32


- We are using something called as `NAT` - `Network Address Translation`.

- We are taking `private IP addresses` and passing those as `one` IP address. That is `NAT`.


- Private IP addresses are - ___Class - A,B,C___

- Routing

<br>
<br>


### Layer 2 

 - MAC Addresses. First Half `(3 parts)`. Do Mac Addres lookup and it will tell you `Details of Hardware`

 - Switching 

<br>
<br>

## TCP vs UPD

- TCP - `Connection Oriented`   ||  UDP - `Connection less`

---

>___Three Way Handshake___ : SYN > SYN-ACK > ACK 


---


- type `sudo wireshark`  and check the traffic.


<br>

### Common Ports and Protocols

- TCP 
    - FTP (21)
    - SSH (22)/ Telnet (23)
    - SMTP (25)
    - DNS (53)
    - HTTP (80)/ HTTPS (443)
    - POP3 (110)
    - SMB (139+445)
    - IMAP (143)
    - RDP (3389)

<br>

- UDP
    - DNS (53)
    - DHCP (67,68)
    - TFTP (69)
    - SNMP (161) - Simple Network Managemnet Protocol


### OSI LAYER

1. __P__ hysical - data cables, cat6
2. __D__ ata - Switching, MAC Address
3. __N__ etwork - routing, IP Address
4. __T__ ransport - TCP/UDP
5. __S__ ession - 
6. __P__ resentation - 
7. __A__ application - 


<br>
<br>

- we did `ping <our ip>` . Not ___All computers have `ICMP` enabled___ 

- `arp -a` : associates IP address with MAC Address. Alternative `ip n` - neighbour


- `routing table` -  `ip r` or `route`




<br>
<br>

## Scripting

<br>

- We will be scripting `pingsweep.sh` - to do a ping sweep.

     - Pre
    ```bash
    ──(kali㉿kali)-[~]
    └─$ ping 10.0.2.15 -c 1 > ip.txt
                                                                                    
    ┌──(kali㉿kali)-[~]
    └─$ cat ip.txt         
    PING 10.0.2.15 (10.0.2.15) 56(84) bytes of data.
    64 bytes from 10.0.2.15: icmp_seq=1 ttl=64 time=0.039 ms

    --- 10.0.2.15 ping statistics ---
    1 packets transmitted, 1 received, 0% packet loss, time 0ms
    rtt min/avg/max/mdev = 0.039/0.039/0.039/0.000 ms
                                                                                    
    ┌──(kali㉿kali)-[~]
    └─$ cat ip.txt | grep "64.bytes"
    64 bytes from 10.0.2.15: icmp_seq=1 ttl=64 time=0.039 ms
                                                                                    
    ┌──(kali㉿kali)-[~]
    └─$ cat ip.txt | grep "64.bytes" | cut -d " " -f 4
    10.0.2.15:

        ┌──(kali㉿kali)-[~]
    └─$ cat ip.txt | grep "64.bytes" | cut -d " " -f 4 | tr -d ":"
    10.0.2.15
    ```

<br>

`ipsweep.sh` now

```bash
        #!/bin/bash

    for ip in `seq 1 254`; do
    ping -c 1 10.0.2.$ip | grep "64.bytes" | cut -d " " -f 4 | tr -d ":" &
    done
```

now `chmod`

```bash

    ┌──(kali㉿kali)-[~]
    └─$ chmod +x ipsweep.sh

    ┌──(kali㉿kali)-[~]
    └─$ ./ipsweep.sh 
    10.0.2.4
    10.0.2.3
    10.0.2.2
    10.0.2.15
                                                                                    
    ┌──(kali㉿kali)

```

<br>

modded

```bash
    #!/bin/bash

    if [ "$1" == "" ]
    then
        echo "You forgot an IP Address!"
        echo "Usage: ./ipsweep.sh 10.0.2"

    else
    for ip in `seq 1 254`; do
    ping -c 1 $1.$ip | grep "64.bytes" | cut -d " " -f 4 | tr -d ":" &
    done

    fi
```  



<br>
<br>

`one-liner` now

```bash
    ──(kali㉿kali)-[~]
    └─$ cat ip.txt                                                
    10.0.2.2
    10.0.2.4
    10.0.2.3
    10.0.2.15
                                                                                    
    ┌──(kali㉿kali)-[~]
    └─$ 
    ┌──(kali㉿kali)-[~]
    └─$ for ip in $(cat ip.txt); do nmap $ip; done
```



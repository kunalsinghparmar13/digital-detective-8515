# Mission 7 — How computers communicate

## 1. Task / objective

Explain basic network types and concepts, observe network lookup and connectivity information, and describe what happens when a website opens.

## 2. Work completed

### Task 7.1 — Explain network concepts

| Concept | Explain it in my own words | Example |
|---|---|---|
| LAN | A Local Area Network connects devices in a small area like one home, lab or office | The Wi-Fi in my home connecting my laptop, phone and printer |
| MAN | A Metropolitan Area Network covers a whole city or a big campus by joining many LANs | A city cable TV / internet network, or a university spread across a city |
| WAN | A Wide Area Network covers very large areas like countries or the whole world | The Internet |
| DNS | Domain Name System works like a phone book: it changes a website name into the IP address the computer needs | `example.com` is turned into its IP address |
| Router | A device that connects different networks and sends data packets on the right path to reach their destination | The Wi-Fi router at home that connects my devices to the internet |
| Protocol | A set of rules that devices follow so they understand each other when they communicate | HTTP/HTTPS for websites, TCP/IP for sending data |
| Packet switching | Data is broken into small packets, each packet travels across the network (maybe by different paths) and they are joined back together at the end | Sending a photo on WhatsApp — it is split into packets and rebuilt on the other phone |
| Client-server | The client asks for a service or data and the server provides it | My browser (client) asks a web server for a web page and the server sends it |

### Task 7.2 — Observe network information

Commands used in Terminal:

```
ping -c 4 example.com
nslookup example.com
```

**Connectivity test (`ping`)**
- `ping` checks if my computer can reach another computer on the network or internet.
- It sends small test packets and waits for a reply. It shows if the replies come back, how long each one took (time in ms) and if any packets were lost.
- My observation: replies came back from example.com with 0% packet loss, so my computer is connected to the internet. (IP address: [redacted])

**DNS lookup (`nslookup`)**
- `nslookup` asks a DNS server which IP address belongs to a domain name.
- It displays the DNS server that answered, the domain name I asked for, and the IP address(es) of that domain (both IPv4 and sometimes IPv6).
- My observation: it showed the name `example.com` and the addresses it points to. The DNS server address of my network is [redacted].

**Role of DNS when I type a website name**
When I type a website name in the browser, the computer does not know where that name is. DNS translates the name into an IP address, and then the browser uses that IP address to connect to the correct server. Without DNS, I would have to remember numbers instead of names.

### Task 7.3 — What happens when you open a website?

1. I type `example.com` in the **browser** (the **client**) and press Enter.
2. The browser asks **DNS** for the IP address of `example.com`, and DNS replies with the server's IP address.
3. My computer sends the request through the **network/router**, which forwards the data packets across the internet towards that IP address.
4. The browser connects to the **server** and sends a request using the **HTTP/HTTPS protocol** ("please send me the home page").
5. The **server** finds the page and sends back a response (HTML, CSS, images) split into packets.
6. The packets come back through the routers to my computer and are joined together again.
7. The **browser** reads the HTML and CSS and displays the web page to me.

## 3. Commands / tools used

| Command / tool | Purpose |
|---|---|
| `ping -c 4 example.com` | Checks if my computer can reach the example website and how long replies take |
| `nslookup example.com` | Finds the IP address of the domain using DNS |
| Terminal | Where I typed the commands |
| VS Code | To write this README |
| Git | To commit and push the mission |

## 4. My understanding

Networks are groups of connected devices. LAN is small (home), MAN is a city, and WAN is huge like the internet. Devices talk using protocols, and data travels in small packets through routers. DNS changes names into IP addresses so the browser (client) can find the right server, and the server sends the website back.

## 5. Difficulties faced

At first I did not understand why `nslookup` showed more than one IP address for the same website.

## 6. How I resolved them

I read about it and understood that big websites can have more than one server and both IPv4 and IPv6 addresses, so DNS can return several addresses.

## 7. Evidence / files

- This README with the network-concepts table, observations and website steps.
- No screenshots added, because the outputs contain my IP and network details (redacted above).

## 8. Commit details

Commit message: `Explain networking concepts and website communication` — pushed to GitHub on the `main` branch.

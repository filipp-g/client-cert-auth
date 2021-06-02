# client-cert-auth
Authentication using Client-side Certificates


- generate self-signed server cert using
```
openssl req -x509 -newkey rsa:4096 -nodes -out cert.pem -keyout key.pem -days 365
```

- create pfx for importing into firefox
```
openssl pkcs12 -export -inkey client.key -in client.crt -name 'fi
refox' -out firefox.pfx
```

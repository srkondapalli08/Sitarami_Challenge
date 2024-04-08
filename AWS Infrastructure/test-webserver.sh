#!/bin/bash

# Check if web server is accessible
curl -s http://example.com | grep "Hello World"

# Check if HTTP redirects to HTTPS
curl -s -I http://example.com | grep "HTTP/1.1 301"

# Check SSL certificate
openssl s_client -connect example.com:443 -servername example.com < /dev/null | openssl x509 -text -noout

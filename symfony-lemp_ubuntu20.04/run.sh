#!/bin/bash
docker run -dit -p 22:22 -p 8080:80 --rm --name node-1 node-ssh
docker run -dit -p 2222:22 -p 8081:80 --rm --name node-2 node-ssh

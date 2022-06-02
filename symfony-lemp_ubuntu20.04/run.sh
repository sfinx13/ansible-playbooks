#!/bin/bash
docker run -dit -p 22:22 -p 8080:80 --rm --name node-1 node-ssh

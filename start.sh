#!/bin/sh
i=$1

let WEB=7442+${i}
let API=7081+${i}

echo "$i $WEB $API"
docker run -d --name jupyterhub${i} \
        -v /canon/jupyterhub${i}:/srv/jupyterhub \
	-v /etc/httpd/conf.d/certificates:/certs \
        -e APIPORT=${API} \
	-p 128.55.210.148:${WEB}:8000 \
        -p 128.55.210.148:${API}:8082 jupyterhubbs

#docker run -it --rm -v /canon/jupyterhubtest2:/srv/jupyterhub -e 7444:8000 -e 7002:8002 --entrypoint bash  jupy

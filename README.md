# Project
Create Prometheus exporter what export custom metrics.

The exporter should get the rsync log as parameter

The project written in Python 2.

I have no experience in Python 3(I can convert the script with 2to3.py) 

and Go but I have a strong openess to learn them.



## Prerequisits
Pythone 2.7 insalled

The following packages installed top of the default set: pygtail, prometheus_client

the exporter file should have rights to read the rsync log file

## Files

prometheus.py	# Main file. You should start this file

argchecker.py	# This file contains the argument checks. 

metrics.py	# This file store the method what used to fill the metrics


## Metrics

all_conn	# Count all started connections since agent start 

all_conn_unique_cource # Count all unique connections

all_bytes_transferred # Count all bytes whattransferred since agent started


## Application

Exporter port: 9376 Referring to [Prometheus_Ports](https://prometheus.io/docs/instrumenting/writing_exporters/)

Start the application with the following command

```
$ ./prometheus_exporter /var/log/rsync.log
```


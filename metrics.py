active_connections = []

def metrics_exporter(logline):
	metrics = {
	"rsync_all_conn": 0,
	"rsync_all_conn_unique_source": 0,
	"rsync_all_bytes_transfered": 0
	}

        splitted_line = logline.split()
        if (str(splitted_line[3])) == "connect":
                active_conn_source = str(splitted_line[5])
                if active_conn_source not in active_connections:
                        active_connections.append(active_conn_source)
			metrics["rsync_all_conn"] = 1
			metrics["rsync_all_conn_unique_source"] = 1
                else:
			metrics["rsync_all_conn"] = 1
        if "total" in splitted_line:
		metrics["rsync_all_bytes_transfered"] = int(splitted_line[-1])

	return metrics


from prometheus_client import start_http_server, Gauge
from kubernetes import client, config
import signal
import time

number = Gauge('custom_nodes_number', 'Get number pods')

def get_k8s_nodes():
    """
    Returns number of kubernetes nodes
    """
    try:
        config.load_incluster_config()
    except config.ConfigException:
        try:
            config.load_kube_config()
        except config.ConfigException:
            raise Exception("Could not configure kubernetes python client")
            
    v1 = client.CoreV1Api()

    ret = v1.list_pod_for_all_namespaces(watch=False)
    a = 0
    for i in ret.items:
        a = a + 1
    return a
              
def gather_metrics(t):
    number.set(get_k8s_nodes())
    print("Number of pods: %d" % number._value.get())
    time.sleep(t)

if __name__ == '__main__':
    # Start up the server to expose the metrics.
    start_http_server(8000)
    # Generate some requests.
    while True:
        gather_metrics(1)
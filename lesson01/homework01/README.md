### Задача №1 ###
--------------------
Запустить
node-exporter с помощью Deployment в minikube. С помощью kubectl пробросить любой порт с localhost на рабочий порт node-exporter внутри minikube.

Итог - скриншот браузера с результатом запроса на localhost:port/metrics, манифест Deployment и строка запуска kubectl

До 3 баллов

--------------------

1) ```node-exporter``` запущен с помощью ```Deployment``` в ```minikube```.

2) С помощью ```kubectl``` проброшен порт с ```localhost``` на рабочий порт ```node-exporter``` внутри ```minikube```

3) Строка запуска ```kubectl``` - ``` minikube start --addons=ingress --cpus=20 --cni=flannel --install-addons=true --kubernetes-version=stable --memory=16g```

4) Строка проброса порта - ```kubectl port-forward node-exporter-s8884 9100:9100 --namespace=monitoring --address='0.0.0.0' &```

```monitoring-namespace.yaml``` - создание ```namespace 'monitoring'```

```node_exporter.png``` - скриншот браузера с результатом запроса на localhost:port/metrics

```node-exporter-daemonset.yml``` - манифест Deployment



Сначала создадим пространство имен мониторинга: ```kubectl apply -f monitoring-namespace.yaml```

```kubectl apply -f node-exporter-daemonset.yml``` - запуск NodeExporter
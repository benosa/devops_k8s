### Задача №2 ###
--------------------
Запустить prometheus и grafana с помощью Deployment'ов в minikube. Доработать манифест из задачи №1 так, чтобы prometheus начал собирать метрики с node-exporter. В grafana настроить дашборд с отображением потребления ЦП и ОЗУ хоста. С помощью kubectl пробросить любой порт с localhost на рабочий порт grafana.

Итог - скриншот дашборда, манифесты 3-х Deployment'ов, строка запуска kubectl и JSON дашборда.

До 7 баллов

--------------------

1) Запущен ```prometheus``` и ```grafana``` с помощью ```Deployment```'ов в ```minikube```

2) ```Prometheus``` - собирает метрики с ```node-exporter```

3) В ```grafana``` настроен дашборд с отображением потребления ЦП и ОЗУ хоста.

4) С помощью ```kubectl``` проброшен любой порт с localhost на рабочий порт grafana.

Строка проброса порта - ```kubectl port-forward grafana-7f94688dff-kmxw7 3000:3000 --namespace=monitoring --address='0.0.0.0' &```

Строка запуска ```kubectl``` - ``` minikube start --addons=ingress --cpus=20 --cni=flannel --install-addons=true --kubernetes-version=stable --memory=16g```

```dashboard_grafana.json``` - JSON дашборда

```grafana-deployment.yaml``` - манифест deployment grafana

```grafana-service.yaml``` - манифест сервиса grafana

```prometheus-config.yaml``` - конфиг прометеуса

```prometheus-deployment.yaml``` - манифест deployment prometheus

```prometheus-service.yaml```- манифест сервиса prometheus

```dashboard.png``` - скриншот дашборда

### Конфигурация Prometheus ###

```Prometheus``` будет получать конфигурацию из ```Kubernetes ConfigMap```. Сможем обновлять конфигурацию отдельно от образа.

```prometheus-config.yaml``` - секция ```data/prometheus.yml``` - встроенная конфигурация ```Prometheus``` в манифест. Далее нужно развернуть в кластере командой
```kubectl apply -f prometheus-config.yaml```. Конфигурацию можно посмотреть командой ```kubectl get configmap --namespace=monitoring prometheus-config -o yaml```.

Далее развернем Prometheus - ```kubectl apply -f prometheus-deployment.yaml```

Можем проверить командой - ```kubectl get deployments --namespace=monitoring```

Создадим службу ```Prometheus``` - ```kubectl apply -f prometheus-service.yaml```

Проверим - ```kubectl get services --namespace=monitoring prometheus -o yaml```

Сделаем сервис доступным - ```minikube service --namespace=monitoring prometheus```

### Конфигурация Grafana ###

Развернем графану - ```kubectl apply -f grafana-deployment.yaml```

Создадим службу  - ```kubectl apply -f grafana-service.yaml```

Сделаем сервис доступным - ```minikube service --namespace=monitoring grafana```

Далее нам нужно пробросить порт к графане. и перейти к настройке.

Добавим Prometheus в качестве источника данных.
* Нажмем на иконку вверху слева от grafana и перейдем в «Источники данных».
* Нажмите «Добавить источник".
* В качестве имени используем "prometheus"
* Выберем «Prometheus» в качестве типа
* В качестве URL-адреса мы будем использовать [DNS Kubernetes](http://kubernetes.io/docs/user-guide/services/#dns). Введем урл `http://prometheus:9090`. Графана найдет службу `prometheus`, работающую в том же пространстве имен, что и она.
  
 Создадим дашбоард и графики.

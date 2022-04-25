### Задача №3 ###
--------------------
Написать приложение, которое будет в формате prometheus возвращать метрику "кол-во подов в кластере". Приложение должно брать информацию по HTTP напрямую 
из API кластера. Можно использовать стандартные библиотеки. Приложение запустить как под в minikube. График по полученной метрике добавить на дашборд из 
предыдущего задания. Желательно, но не обязательно, если приложение будет на python (это не повлияет на оценку).

Итог - исходный код приложения, dockerfile, манифест пода

До 5 баллов

--------------------

1) ```count_nodes_exporter.py``` - приложение написанное на Python, которое возвращает метрику "кол-во подов в кластере" и которое берет 
информацию по HTTP напрямую из API кластера с использованием стандартной библиотеки. 

2) Приложение запущено как под в minikube.

3) График по полученной метрике добавлен на дашборд из предыдущего задания

```dashboard_cpu_mem_pods.png``` - отображение полученной метрики на дашбоарде из предыдущего задания.

```deployment.yaml``` - манифест Deployment нашего приложения, манифест сервиса, находится внутри.

```Dockerfile``` - dockerfile для построения нашего образа с прогаммой для сбора метрики

```requirements.txt``` - список зависимостей для установки через pip докерфайла 



Сначала создадим Docker image ```docker build -f Dockerfile -t py-exporter:latest .```

Поскольку мы не заливали наш образ на докер хаб нам придется исправить ситуацию

```> minikube docker-env
export DOCKER_TLS_VERIFY=”1"
export DOCKER_HOST=”tcp://172.17.0.2:2376"
export DOCKER_CERT_PATH=”/home/user/.minikube/certs”
export MINIKUBE_ACTIVE_DOCKERD=”minikube”
# To point your shell to minikube’s docker-daemon, run:
# eval $(minikube -p minikube docker-env)```

запустим команду ```eval $(minikube -p minikube docker-env)``` и пересоберем образ ```docker build -f Dockerfile -t py-exporter:latest .``` - 
образ попадет в реестр minikube.

Изменим конфигурацию ```Prometheus``` - ```prometheus-config.yaml``` - добавим новую работу для сбора статистики от нашей программы

Применим новую конфигурацию - ```kubectl apply -f prometheus-config.yaml``` 

Перезапустим POD - ```kubectl rollout restart deployment prometheus -n monitoring``` - перезапуск пода

Добавим в графане новую панель с нашей статистикой по количеству POD


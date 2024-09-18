# pizza-app
## Small application to register Pizza orders from a webform.
Application to register Pizza Orders and display them in a web form
On your machine withe Kubernetes installed simply:

To run the application in a docker container with a persitent volume, simply 
```
docker run -dp 8000:8000  balat2020/pizza-app:latest
```
## Kubernetes Cluster setup

1.-Create PV and PVC
```
kubectl apply -f pv.yaml
kubectl apply -f pvc.yaml
```
2.-Create Kubernetes cluster
```
kubectl apply -f kb.yaml
```

Visit Create order page
[http://localhost:30001/order](http://localhost:30001/order)

Visit Main Order Page
[http://localhost:30001](http://localhost:30001)

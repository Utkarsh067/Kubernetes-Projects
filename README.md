# 🐳 Python Flask App on Kubernetes (Minikube)

This repository demonstrates how to containerize a Python Flask application and deploy it locally to a Kubernetes cluster using Minikube. Follow the steps below to build, deploy, and verify your app.

---

## 📁 Directory Structure

```
.
├── app.py
├── Dockerfile
├── requirements.txt
├── deployment.yaml
├── service.yaml
└── README.md
```

---

## 📥 Clone the Repository

```
git clone https://github.com/Utkarsh067/Kubernetes-Projects.git
cd Kubernetes-Projects
```

---

🔧 Prerequisites

Make sure you have the following tools installed on your local machine:

[Docker](https://docs.docker.com/get-docker/)

[Minikube](https://minikube.sigs.k8s.io/docs/start/)

[Kubectl](https://kubernetes.io/docs/tasks/tools/)

---

## 🚀 Step-by-Step Instructions

### 📌 1. Install Prerequisites

Ensure Docker, Minikube, and kubectl are installed and available in your PATH. You can verify each installation with:

+ ``` docker --version ```
+ ``` minikube version ```
+ ``` kubectl version --client ```

### 📌 2. Start the Minikube Cluster

```minikube start```

Verify that the Minikube node is up and running:

```kubectl get nodes```

### 📌 3. Build and Load Your Docker Image

In the root of this repository, build your Flask app Docker image:

```docker build -t python-flask-app .```

Load the image into Minikube’s Docker registry:

```minikube image load python-flask-app```

⚠️ Minikube runs its own Docker daemon. Using minikube image load ensures your local image becomes available inside the Minikube cluster.

### 📌 4. Deploy to Kubernetes

If you've cloned this repository, the required Kubernetes YAML files (deployment.yaml and service.yaml) are already included. You can apply them directly:

```kubectl apply -f deployment.yaml```
```kubectl apply -f service.yaml```

✅ OR if you're writing your own from scratch, you can manually create the files using the content below.

Deployment.yml
```
apiVersion: apps/v1
kind: Deployment
metadata:
  name: flask-deployment
spec:
  replicas: 2
  selector:
    matchLabels:
      app: flask-app
  template:
    metadata:
      labels:
        app: flask-app
    spec:
      containers:
      - name: flask-container
        image: python-flask-app
        ports:
        - containerPort: 5000
```

Service.yml
```
apiVersion: v1
kind: Service
metadata:
  name: flask-service
spec:
  type: NodePort
  selector:
    app: flask-app
  ports:
    - port: 5000
      targetPort: 5000
      nodePort: 30008
```

### 📌 5. Verify Pods and Services

Check that your pods are running:

```kubectl get pods```

✅ Sample output:

![image](https://github.com/user-attachments/assets/de6d0146-cbb1-4258-ba15-9d8dc6b21e29)


Check that your service is up and exposes a NodePort:

```kubectl get services```

You should see something like 5000:30008/TCP under PORT(S).

✅ Sample output:

![image](https://github.com/user-attachments/assets/7664745c-ee3f-4e7b-8e36-62aafd3b5762)

        
### 📌 6. Access Your Flask App

You can test your deployed Flask application using curl:

```curl http://$(minikube ip):30008```

If everything is set up correctly, you should see the following HTML output:

![image](https://github.com/user-attachments/assets/60186419-fde6-42bf-ae8c-f2d87b35bd7c)

✅ You can also open ```http://$(minikube ip):30008``` in your browser to view the app.

### 📌 7. Scale the Deployment

Scale your Deployment up (or down) as needed. For example, to scale to 4 replicas:

```kubectl scale deployment flask-deployment --replicas=4```
```kubectl get pods```

✅ Updated pods after scaling:

![image](https://github.com/user-attachments/assets/30f277db-9592-40ea-8fe9-821810185e41)


### 📌 8. Inspect Deployment and Logs

```kubectl describe deployment flask-deployment```

View logs from one of the running pods:

```kubectl logs <pod-name>```

Replace <pod-name> with one of the pod names listed under kubectl get pods.

---

## 🧾 Conclusion

This project walks through deploying a simple Flask web application to a local Kubernetes cluster using Minikube. It covers the entire lifecycle of containerizing the app with Docker, deploying it using YAML configurations, scaling it, and validating service exposure with kubectl and curl. This setup provides a solid foundation for learning Kubernetes and container orchestration in a local development environment.

## 👤 Author

Utkarsh Jain

[LinkedIn](https://www.linkedin.com/in/utkarsh-jain02/)

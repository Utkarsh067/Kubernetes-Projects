# Steps - 
#### 1. Install [Kubectl](https://kubernetes.io/docs/tasks/tools/) from the given link. 
+ Kubectl, short for "kube-control," is a command-line tool primarily used for interacting with Kubernetes clusters.
+ You can use Kubectl to deploy applications, inspect and manage cluster resources, and view logs.

![image](https://github.com/user-attachments/assets/5ef1eaa2-d953-4914-af08-010bbacf0cb7)

#### 2. Install [Minikube](https://minikube.sigs.k8s.io/docs/start/?arch=%2Fwindows%2Fx86-64%2Fstable%2F.exe+download) from the given link.
+ Minikube is a tool designed to facilitate the creation and management of a single-node Kubernetes cluster on a local machine.
+ All you need is Docker (or similarly compatible) container or a Virtual Machine environment, and Kubernetes is a single command away: Minikube start

![image](https://github.com/user-attachments/assets/1458d654-71f2-4c6d-90b3-a0ef4ef8644f)

#### 3. Install [Docker](https://docs.docker.com/engine/install/) from the link, based on your system requirements.

![image](https://github.com/user-attachments/assets/1294ae8e-adfa-4071-a8d1-de59bcf41c78)

#### 4. Start Docker
#### 5. Open your terminal like Ubuntu, Powershell, etc.
![image](https://github.com/user-attachments/assets/145b6067-6538-4e97-96d5-8934c97662ca)  ![image](https://github.com/user-attachments/assets/a61b52c2-14fb-46b0-834b-2a9c608accfa)

#### 6. To check your Minikube is running, type the command ``` Minikube version ```
#### 7. Similarly, to check your Kubectl is running, type the command ``` Kubectl version ```

#### 8. Now, we will be deploying our application. I created a Web Applicaton using Docker, you can check its steps in the given link of my [GitHub repo](https://github.com/Utkarsh067/Docker-Projects-/tree/a3269ec91c28d8db2df181fdb5b2de833e984636/Containerizing%20a%20Static%20website)
#### Or you can can run this command ``` kubectl create deployment kubernetes-bootcamp --image=gcr.io/google-samples/kubernetes-bootcamp:v1 ```. It is a demo image provided by the Kubernetes community.

#### 9. To check your app has been deployed, run the command ```kubectl get deployments```. It will show that your app is running.

#### 10. Open the second terminal and run the command ``` kubectl proxy ```
#### 11. Now, paste this URL in the browser ```(http://localhost:8001/version) ```, here you can see all those APIs hosted through the proxy endpoint.

#### 12. Now, we will expose our app
+ Write command ``` kubectl get pods ```, If no Pods are running then it means the app has not been created, go through all steps again.
+ Run command ``` kubectl get services ```
+ Run ``` kubectl describe services/[Your_Image_Name] ```
+ Now, run this URL in the browser ```(http://"$(minikube ip):$NODE_PORT")```, and you will be able to see that your application has been exposed.

#### 13. To delete service
+ Run ```kubectl delete service -l app=[Your_Image_Name]```
+ To confirm that sevice has gone, run ```kubectl get services ```
+ To confirm service has been removed, run this URL in the browser ```(http://"$(minikube ip):$NODE_PORT")```
+ This proves that the application is not reachable anymore from outside of the cluster.

### Congratulations 🎉🎉🎉, you have successfully Deployed a Containerized application on a Kubernetes Cluster.

# Integrating Machine Learning & DevOps
<br/>

**Workflow**

<br/>

![mlops](https://user-images.githubusercontent.com/48363834/95820559-e6bd4400-0d45-11eb-9513-6a8c36c39cf3.png)

<br/>
STEP-1: Creating a machine learning code to train a model to distinguish between car and truck using images as a dataset.<br/>
STEP-2: Create container image that’s has Python3 and Keras or numpy installed using Dockerfile.<br/>
STEP-3: Creating a job chain of job1, job2, job3, job4 and job5 using build pipeline plugin in Jenkins.<br/>
STEP-4: Job1- Pull the Github repo automatically when some developers push repo to Github.<br/>
STEP-5: Job2- By looking at the code or program file, Jenkins should automatically start the respective machine learning software installed interpreter install image container to deploy code and start training.<br/>
STEP-6: Job3- Training model and predicting accuracy or metrics.<br/>
STEP-7: Job4- If metrics accuracy is less than 80% , then tweak the machine learning model architecture.<br/>
STEP-8: Job5- Sending a mail that the best model is being created.<br/>
STEP-9: Job6: If container where app is running fails due to any reason then this job should automatically start the container again from where the last trained model left.<br/>

***For More Details->*** https://medium.com/@mansi.dadheech22/integrating-machine-learning-devops-a75cc896e18c

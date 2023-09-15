# Cil-Academy

## Description
## Project
I created an EC2 instance and an S3 bucket using a cloud formation stack giving a role to only SSM into my EC2 with other permission too.
I SSM into the EC2 and copy the content into my directory called **mys3backup**
I wrote a python script to copy the **BUCKET** content to my directory on execution.

### EC2
Amazon Elastic Compute Cloud (Amazon EC2) provides on-demand, scalable computing capacity in the Amazon Web Services (AWS) Cloud. Using Amazon EC2 reduces hardware costs so you can develop and deploy applications faster. You can use Amazon EC2 to launch as many or as few virtual servers as you need, configure security and networking, and manage storage. You can add capacity (scale up) to handle compute-heavy tasks, such as monthly or yearly processes, or spikes in website traffic. When usage decreases, you can reduce capacity (scale down) again.

![Web capture_11-9-2023_22527_us-east-1 console aws amazon com](https://github.com/123-Daniel/Cil-Academy/assets/96403532/98f46c92-e736-41d4-8060-b9b8bc7d1b89)
### IAM
An IAM role is an IAM identity that you can create in your account that has specific permissions. An IAM role is similar to an IAM user, in that it is an AWS identity with permission policies that determine what the identity can and cannot do in AWS. However, instead of being uniquely associated with one person, a role is intended to be assumable by anyone who needs it. Also, a role does not have standard long-term credentials such as a password or access keys associated with it. Instead, when you assume a role, it provides you with temporary security credentials for your role session.
You can use roles to delegate access to users, applications, or services that don't normally have access to your AWS resources. For example, you might want to grant users in your AWS account access to resources they don't usually have, or grant users in one AWS account access to resources in another account. 

![Web capture_11-9-2023_221719_us-east-1 console aws amazon com](https://github.com/123-Daniel/Cil-Academy/assets/96403532/f6adb0ce-cb04-4291-afa4-f1c821772382)
### S3 Bucket 
Amazon Simple Storage Service (Amazon S3) is an object storage service that offers industry-leading scalability, data availability, security, and performance. Customers of all sizes and industries can use Amazon S3 to store and protect any amount of data for a range of use cases, such as data lakes, websites, mobile applications, backup and restore, archive, enterprise applications, IoT devices, and big data analytics. Amazon S3 provides management features so that you can optimize, organize, and configure access to your data to meet your specific business, organizational, and compliance requirements.

![Web capture_12-9-2023_121928_s3 console aws amazon com](https://github.com/123-Daniel/Cil-Academy/assets/96403532/042ac022-683f-4885-be39-6d456934e1f5)

### Cloud Formation Code and Python Script
![Capture](https://github.com/123-Daniel/Cil-Academy/assets/96403532/a4960e8b-760f-46fe-b467-490e80da50d0)






### Architectural Diagram
![Cloud-1 (2)](https://github.com/123-Daniel/Cil-Academy/assets/96403532/1b3961cc-02e3-4a68-9279-b07bf5f1e2ad)

# Smart-shopping-cart-using-object-detection-and-flask-web-app
Unstaffed stores have grown in popularity recently and significantly changed traditional purchasing patterns in the modern day. In this context, unmanned retail containers are crucial since they can impact on the consumer shopping experience, this project aims to transform the traditional shopping experience, making it more efficient, personalized, and enjoyable for customers. <br />
The core of the Smart Shopping Cart system is an integrated object detection model based on YOLO architecture, which enables real-time identification of products placed in the cart. cameras are used to capture and verify the items, ensuring accurate detection and preventing errors.<br />
The Flask framework serves as the backbone of the application, managing the communication between the hardware components and the user interface.A responsive frontend interface, developed with HTML, CSS, and JavaScript, provides real-time updates to the user, displaying a Qr code that has item details, total cost, and the available ways of payment.<br />
## Requirements:
● YOLOv8 model<br />
● OpenCV library<br />
● Flask framework<br />
● Web camera<br />
## Part one: Object detection
While using a dataset consisting of about 5000 images we bulit a YOLOv8 model which is a significant improvement over previous versions, as it incorporates several new features and improvements by Ultralytics,  We were able to detect the products reaching a precision of about 97%.<br />
In our project we integrated the YOLO model with OpenCV library, this integration demonstrates how YOLO model handles the complex task of object detection, while OpenCV as cv2 facilitates the visualization and graphical representation of the detected objects in the video frames.<br />
![yolo-comparison-plots](https://github.com/user-attachments/assets/bb56c3fd-8bb5-4180-afc9-0957c996ffc4).<br />
## Part two: Deployment using flask framework
Flask is a lightweight web framework for Python, provides a simple yet powerful environment for serving machine learning models. Model deployment in machine learning integrates a model into an existing production environment, enabling it to process inputs and generate outputs. <br />
Using flask and HTML , CSS and JavaScript we were able to build an interactive user interface to make the checkout process easier for customers.<br />
![ui1](https://github.com/user-attachments/assets/382700f0-d197-46f6-902a-dd8be6fcf99b)
![5555](https://github.com/user-attachments/assets/7905508f-f669-4343-8bdf-9bb684000a5b)<br />
We built two pages which are:<br />
Instructions page to provide customer with the important instructions related to shopping cart so that the check out process is seamless and successful.<br />
Live Web Camera page to do the live object detection for the products purchased by the user.<br />
After this step is done the live camera detection waits for 30 seconds until the process of detection is done then redirect to a Qr-code that fetches the data of the products from database, The Qr-code will be scanned by user using our mobile application and redirect the user to a payment page.<br />
![photo_2024-08-04_00-05-10](https://github.com/user-attachments/assets/b9d9258d-8127-43d2-b7d5-363857e4b128)

## System flow chart:
![image](https://github.com/user-attachments/assets/dc59a578-8232-4ef3-afc5-02c719a7d1e6)










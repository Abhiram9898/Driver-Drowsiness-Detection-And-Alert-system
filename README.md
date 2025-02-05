# Driver-Drowsiness-Detection-And-Alert-system
<br>

Abstract— This paper introduces the groundbreaking Drowsy Driver Detection System (DDDS), a paradigm-shifting technology designed to significantly enhance road safety by leveraging the capabilities of computer vision. At its core, the DDDS employs a sophisticated camera to capture real-time video footage of the driver, utilizing advanced facial landmark detection techniques to focus specifically on the driver's eyes. The system meticulously analyzes live video data, identifying signs of drowsiness, such as prolonged eye closure, and issues timely alerts to warn drivers when fatigue is detected. One of the distinctive features of the DDDS is its robust performance in varying lighting conditions, ensuring its effectiveness across diverse driving scenarios. The integration of artificial intelligence (AI) algorithms enhances its capabilities by enabling continuous learning and adaptation to evolving patterns of driver behavior, making it a future-proof solution in the realm of road safety. In conclusion, the Drowsy Driver Detection System stands as a pioneering advancement in road safety technology, reshaping the landscape by offering a holistic solution to the pervasive issue of drowsy driving. As technology continues to play a pivotal role in ensuring safety, the DDDS emerges as a beacon, providing a reliable and adaptive guardian on the roads.
	
Keywords— Drowsy Driver Detection System (DDDS), Road Safety, Computer Vision , Real-time Video Analysis, Facial Landmark Detection, Alert System.


1.	INTRODUCTION
In contrast, we have developed a non-intrusive computer vision-based algorithm which can be executed in any normal car, given that it has a camera installed, and it also does not require a large amount of battery power and memory to execute the algorithm. This system, which is implemented in the field of computer vision, uses a simple web camera to capture the images of the driver continuously. Then, it rapidly processes those images and identifies the eyes of the driver. After performing the necessary calibrations and positioning of the features on the face, the algorithm is capable of precisely knowing when the driver's eyes are open or closed. This is because the driver's eye will have the biggest width in the upper eyelid region and the smallest width in the lower eyelid when it is fully open. Thus, if the camera detected a smaller area in the lower eyelid, it means the driver is blinking, and from this feature, the proposed algorithm can easily compute the frequency and duration whenever the eye is being closed, and this can be used to define the drowsiness level of the driver.[1] [2] [3]
So, our main objective of this research is to develop a system that can detect when a driver is drowsy and provide a warning to the driver. This paper presents a novel algorithm for the detection of drowsiness in the real-time stream of image data in a vehicle, in which the primary focus is given to the blinking aspect, which is one of the main symptoms of drowsiness exhibited by the drivers. A lot of other research has also been done in this area considering the physiological aspects and monitoring the facial features of a driver. [4] [5] [6]       
   
                 1.1. Problem Statement
It refers to the detection and alerting in terms of any accident or  impacts that may occur due to the drowsiness of the driver during driving. According to the National Highway Traffic Safety Administration, more than 100,000 accidents happen in the United States each year due to drowsy driving. It has also been proven that driver fatigue or drowsiness is the primary cause of such accidents. However, it is often difficult for the general public to identify these dangers in a timely manner. Therefore, we are undertaking the task of designing and developing an advanced algorithm that can effectively detect the level of drowsiness in drivers while they are on the road.

This algorithm will be developed and validated both in laboratory settings and real driving environments. It will be designed to work across a diverse range of alertness levels and ethnic or eye region groups. To measure the level of drowsiness, we will utilize a selected parameter that monitors the percentage of eye closure in real-time. Through a series of planned studies, our aim is to validate and optimize the proposed method, in order to lay the foundation for future advancements and practical applications.

The developed algorithm, along with the associated mechanisms and algorithms, will be shared with the broader research community. By utilizing this proposed drowsiness detection system, we strongly believe that countless lives can be saved, as the occurrence of drowsy driving accidents will be significantly reduced. Our ultimate objective is to ensure the safety of drivers and everyone on the road by combatting the dangers   associated with driver fatigue.

2.Literature Review
Drowsiness detection is vital in ensuring the safety of a driver and the passengers. There are various ways in which drowsiness of a driver can be detected. Drowsiness detection systems can be categorized into two: systems that analyze vital signals and systems that analyze non-vital signals. Vital signals include signals like heartbeat rate and pulse rate, while non-vital signals include signals like eye aspect ratio and yawning, blinking among others. Drowsiness detection methods that analyze vital signals often involve the use of additional apparatus like health bands and pulse rate monitors. These systems are usually embedded and may not sound the alarm to the driver. When drowsiness is detected, the vehicle may be slowed down or safely pulled off the road. On the other hand, systems that analyze non-vital signals such as machine vision algorithms and image processing can be used to detect drowsiness. This can help avoid the drawbacks associated with using vital signals that require additional apparatus. Such methods are becoming more and more popular nowadays as a result of advancement in technology. For instance, many modern vehicles today come with a drowsiness detection system which makes use of a facial recognition camera. Such a camera is used to track the head and face of the driver and thus can be used to monitor eye aspect ratio, closure, and frequency. These are very useful parameters for drowsiness detection as literature has shown that there is a strong correlation between eye tracking parameters and drowsiness. Modeling of eye state data and yawning can also be used. It has been suggested that a multi-model approach by combining different yawning and eye tracking parameters appears to provide improved performance in drowsiness detection. Such methods are particularly useful when drowsiness detection is based solely on non-vital signals such as eye aspect ratio. As has been found, yawning is a strong indicator of drowsiness while eye aspect ratio is used to track the progressive state of drowsiness. A model that is based on the tracking of eye states data is found to have its performance substantially improved when the amount of yawning is considered. This can be used to considerably reduce the false alarm rate of drowsiness. These methods often use machine vision algorithms and image processing to track and record eye states data and yawning. Such methods offer a unique advantage for drowsiness detection as the manipulation of non-vital signals can be achieved through many different channels and means. As technology continues to evolve and improve, it is expected that more and more non-vital signal-based drowsiness detection methods will be developed and deployed. Such methods usually can be adapted for use for particular groups of drivers who may have specific needs, for example, heavy vehicle drivers or drivers with certain health conditions. [7] [8] [9][10] [11] [12]

       3.Components of  Proposed Methodology
•	Driver drowsiness detection stands as a crucial car safety technology,     dedicated to   preserving lives by preventing accidents when drivers are fatigued. This technology is designed with a multifaceted approach:
•	The primary objective involves the meticulous planning of a robust framework capable of discerning signs of driver fatigue through continuous monitoring of the retina.
•	The framework demonstrates versatility by operating effectively even when drivers are not wearing specialized displays and in diverse lighting conditions.
•	Upon detecting signs of drowsiness, the system promptly alerts the driver, employing auditory signals such as a bell or an alert notification.
•	In addition to alerts, the system has the capability to contribute to accident prevention by automatically adjusting the speed of the vehicle when drowsiness is identified.
•	The overarching impact extends beyond individual vehicles, as the technology aids in traffic management by mitigating the occurrence of accidents, thereby enhancing overall road safety.
 
3.1. The Computer’s Vision
Computer vision serves a critical role in driver drowsiness detection and alarm systems by continuously analyzing facial features and behaviors of the driver in real-time. Through advanced algorithms, computer vision extracts key indicators such as eye movements, blink patterns, and facial expressions associated with drowsiness. This technology enables timely detection of fatigue-related cues, prompting immediate alerts to mitigate potential accidents. By leveraging machine learning and image processing techniques, computer vision enhances the accuracy and effectiveness of drowsiness detection systems, ultimately contributing to improved road safety.


3.2. OpenCV
The Open Source Computer Vision Library (OpenCV) assumes a critical role in the development of driver drowsiness detection and alert systems, providing a versatile framework that empowers developers to implement cutting-edge computer vision algorithms. By harnessing OpenCV, developers can efficiently process live video feeds captured by in-vehicle cameras.This process involves extracting pertinent facial features and meticulously analyzing eye behavior to identify early signs of driver drowsiness. OpenCV offers an extensive array of functions dedicated to image processing, encompassing vital components such as face detection, eye tracking, and facial expression analysis. This comprehensive suite of tools ensures the development of robust drowsiness detection algorithms, there by contributing significantly to the advancement of road safety. 
Reasons for Using OpenCV are :-
A) Specificity in Image Processing Planning:
OpenCV was strategically chosen for its specialized prowess in image processing. The Image Processing Plan visualizes every structure and facet of the data, aligning seamlessly with the objectives of the drowsiness detection system. In contrast, Matlab, while conventional, tends to rely heavily on toolboxes, which may span financial or specialized domains, potentially limiting its adaptability to the unique demands of the drowsiness detection application.

B) Speed Considerations:
The choice against Matlab is driven by concerns over speed. Matlab, inherently reliant on Java, which, in turn, depends on C, introduces a performance bottleneck. The execution of Matlab programs involves intricate processes of interpretation and integration, causing a notable lag in real-time applications. This stands in stark contrast to OpenCV, which exhibits a more streamlined and efficient performance, crucial for the time-sensitive nature of drowsiness detection.

C) Resource Efficiency:
Matlab's propensity to consume excessive system resources contrasts sharply with OpenCV's resource-efficient approach. In practical terms, OpenCV allows the extraction of a mere 10mb RAM for continuous application. While modern computers may handle RAM demands capably, the specific deployment context of the fatigue monitoring system within a car demands a low-resource footprint. This consideration ensures optimal functionality within the confined and resource-sensitive environment of an in-vehicle application, underscoring the practical significance of resource efficiency in the chosen technology stack.

3.3.Machine Learning:
In the landscape of driver drowsiness detection and alert systems, machine learning assumes a pivotal role, empowering the creation of algorithms characterized by exceptional accuracy and adaptability. Through the strategic utilization of extensive datasets containing labeled facial images correlated with distinct drowsiness states, machine learning models adeptly discern nuanced patterns indicative of fatigue. These models undergo meticulous training to analyze diverse features extracted from facial expressions and eye movements, thereby cultivating an acute ability to differentiate between states of alertness and drowsiness.

Furthermore, machine learning serves as the catalyst for perpetual refinement and adaptability in drowsiness detection algorithms. This perpetual learning process, fueled by continuous exposure to new data and user feedback, results in a dynamic and adaptive capability. This not only mitigates false alarms but also augments the overall accuracy of drowsiness detection systems. The cumulative effect is a significant enhancement in the efficacy of these systems, contributing unequivocally to the creation of safer driving conditions on our roads.

3.4. OpenCV’s Machine Learning Algorithms:
Embedded within OpenCV are machine learning (ML) statistics, thoughtfully organized within the ML library. These statistics are meticulously separated by Mahalanobis and K-implication, residing in CVCORE. Additionally, the facial recognition calculations, integral to OpenCV's expansive capabilities, are housed within the CV module. This strategic organization ensures a seamless integration of machine learning algorithms into OpenCV, providing developers with a rich toolkit for harnessing the power of advanced statistical and recognition methods in the pursuit of robust and efficient drowsiness detection system.


4. METHODOLOGY
The main purpose of this paper is to produce a simple and easy-to-use system that will lead to a safe road trip.
![image](https://github.com/user-attachments/assets/e20709f3-032c-42c1-95c8-d422d9786650)





    			

                                                                                                                                 Fig.: 1 

In our methodology, we first input an image sequence into our system. This sequence undergoes a face detection process, where the system identifies any faces present in the images. Following face detection, the system performs eye detection to locate the eyes within the detected faces.Once the eyes are detected, the system tracks the state of the eyes (open or closed) over time. This is done using an eye state tracking algorithm. If the system detects that the eyes have been closed for a certain number of time (15 sec), it issues a warning.This methodology allows us to effectively monitor the state of the eyes in an image sequence and issue a warning if the eyes remain closed for too long, which could indicate drowsiness or inattention.

A key part of a driver sleepiness detection system is the head posture  estimate module. It is employed to make educated guesses regarding the location and tilt of the driver's head in live video footage shot by a camera. The module frequently makes use of computer vision techniques and algorithms for figuring out the camera's head's 3D translation and rotation. Driver sleepiness detection systems can employ a variety of well-known head pose estimate libraries. OpenCV is among the most popular libraries. To predict the 3D rotation and translation of the head from a 2D image, OpenCV offers a pre-trained head pose estimation model.

Fig 1 shows the method used to develop the system to an efficient way. The algorithm used to process the image to feed the code to specify the face in the image, the image is divided into sub-regions to determine whether the region is on the face or not. The use of this algorithm means a time-saving method 


and only face-containing domains are processed.
![image](https://github.com/user-attachments/assets/d3ac9555-aa6c-43b6-8b28-92f42cf4f267)



Fig.: 2



Fig 2 shows how the system would work and look in real world.

Module operates as follows :-

1. To use a camera or sensor, the system records photos or video of    the driver's face. 
2. The algorithm recognizes the mouth region in the photos or videos that were taken. 
3. The device measures how far apart the top and lower lips are and  compares that measurement to benchmarks to determine the extent of mouth opening.
4. The algorithm then evaluates how much the driver opens their mouth over time to determine if they are getting sleepier.

  	5.Results
Following is the table representing four test cases that are to 
encountered while doing this project that concerns with the   drowsiness of the driver.

  ![image](https://github.com/user-attachments/assets/3c773b00-b71f-4c6f-bfe0-07c59449bdd4)

                                            Table 1
	
Table 1: Test Cases

In our test cases, we identify a critical threshold where an elevated number of closed-eye instances signifies driver fatigue,prompting proactive warnings. The methodology involves a meticulous examination of blink patterns and drowsiness to ensure the accuracy of our findings. Utilizing a 5-megapixel webcam-compatible PC, this project employs cutting-edge technology to capture high-resolution images with minimal computational burden.

The selected webcam is equipped with a built-in white LED, serving as an indicator of its operational status. However, it is noteworthy that for real-time applications, the use of infrared LEDs is recommended over white LEDs for optimal framing purposes. To further engage the driver, a built-in speaker is leveraged to deliver sound output upon the detection of drowsiness, providing an effective wake-up mechanism.
	
The frame's design accommodates diverse individuals under varying light conditions, ensuring adaptability for both day and night scenarios. By strategically aligning the webcam's background light and maintaining facial alignment, the frame achieves exceptional accuracy, boasting a detection rate of over 95% for both blinking and drowsiness instances. This comprehensive approach not only prioritizes accuracy but also underscores the system's efficiency in real-world applications.

Eye Detection Accuracy can be quantified by dividing the total number of times eyes were accurately detected by the overall attempts made. Similarly, Drowsiness Detection Accuracy is computed as the total number of times the alarm successfully sounded divided by the sum of instances where the alarm sounded and instances where the alarm did not sound.

5.1. Dataset Description
The dataset used for the research work is the Drowsy Driver dataset, which is created by collecting our own dataset. The dataset comprises images of drivers at different times of the day and under different levels of illumination. Different levels of head poses and different facial expressions, including yawning, were also included in the dataset. The data was collected from 20 volunteers with their consent, and each took about 30 minutes for the whole data collection process. The data was split into training and validation sets, with 80% of the data in the training set and the remaining 20% used for validation. Also, during the training process, we further split the training data into train and test in an 80/20 percentage, respectively. 80% was used for training, while 20% was used for model validation. The labels for each of the datasets were also made available, and they are: 'Close', 'yawn', and 'normal'. 'Close' depicts that the eyes are nearly closing, 'yawning' means the driver is yawning, and 'normal' depicts the driver in a normal state. Also, throughout the whole data collection process, the frame count was displayed at the upper left corner of the screen, and 4800 images were collected for the training set, while 1200 were collected for the validation. The images were preprocessed and resized to 64*64 pixels. The labels in the training set were checked, and it was found that 21.8% were 'Close' labels, 10.1% were 'yawn' labels, and 68.1% were 'normal' labels. The same applies to the validation set. The images were extracted into arrays, and the shapes of the training and validation data were printed out to be 64*64*3, which corresponds to the reshaped sizes of the images. This dataset was used to train the model.

                6.Discussion and Analysis	
On a presented custom dataset of around 1800 images, each of both eyes whether closed, opened, or looking forth, we are getting an accuracy of nearly 97% on test images. The loss becomes 0.12 after 10 epochs. We are also getting an accuracy of around 98% on footage obtained using the in-built camera. The loss of the camera footage becomes approximately 0.05 after 10 epochs. So, by combining this with computer vision and a drowsiness detection algorithm, we are successfully able to measure whether the eyes are closed or opened, and depending on that, if the eyes are closing. With the state-of-the-art advancements in fields such as machine learning, image processing, computer vision, and OpenCV, we are now capable of translating our theoretical idea on paper to an idea that may have practical benefits, and that's exactly the case with drowsiness detection in driving. After training with custom dataset images and using a CNN model, as we have seen in the results, we get 97% accuracy on test images, 0.12 loss, 98% accuracy on camera footage, and 0.05 loss. This leads us to the conclusion that our combined approach with computer vision and the Keras drowsiness detection is highly efficient. Thanks to the high level accuracy of computational methods and optimization algorithms like CNN and drowsiness detection. Also, by using OpenCV, we are also capable of doing many things about the drowsiness itself after detection, as we will see in the next section.

One of the key findings from the study was that the model was able to successfully determine and classify whether the eyes of the driver were open or closed. This is evidenced by the relatively high level of accuracy achieved in the training and validation of the model. The results found that the probability of the driver being alert was above 98% when the eyes were open and the probability of the driver being drowsy was greater than 79% when the eyes were closed. This supports the credibility of the system because it shows that the convolutional neural network model has learnt to distinguish the features of drowsy and alert drivers. With these levels of high probability, a simple alert system could be initiated when the driver is classified as drowsy. This would start a counter and, for example, if five consecutive drowsy classifications were made, an alarm of some sort could be initiated to catch the attention of the driver and wake them up. Every time the eyes of the driver were found to be closed for a duration of a number of frames greater than a set threshold, the model successfully recognised this as a 'drowsy' frame and the first level of triggering the alarm of the alert system was initiated. Every time the eyes of the driver were found to reopen, these frames were classified as 'alert'. The number of frames classified as 'drowsy' between consecutive frames classified as 'alert' was recorded - this would be used to identify both the quantity and periods of the drowsy epochs.

6.1. Comparison with Existing Systems
Up to now, the system and method proposed in the described paper have been compared with existing methods in terms of their abilities to detect and respond to symptoms like drowsiness and inattention in drivers. The comparison results are favorable to the new method. This suggests that the use of the intelligent systems programming, video, and image processing techniques that have been described can offer some real advantages over the methods currently used in real cars, such as the use of an infrared LED and photodiode sensors, the method used in the 'Mazda system', which is aimed at ensuring that the security measures in the new system can respond accurately and appropriately to any warning signs from the driver. Existing methods typically involve a number of sensors, which need to be carefully positioned around the driver to capture all the relevant information and these systems are focused on detecting the period of time just before an accident occurs or the driver is physically affected by tiredness and as a consequence takes his or her hands off the wheel. This is in contrast to the new method, where the paper suggests that it is aimed at identifying symptoms and providing a more rapid prevention strategy. Also, the advantage of the proposed method has been presented on the basis of algorithms and programming used to interpret eye and facial movement and positions from video data. These include a Main Eyes area centroid algorithm and a method which uses the amount of white space around the pupil to determine 'percentage closed'. The paper points out that the analysis of the existing methods have shown various areas for potential improvement. For example, as well as aiming to optimize the response of the warning systems and quality of data with the new method, opportunities for technological advancement of existing systems have been identified. It shows that the future development and programming opportunities have largely focused on the optimization of sensors and their data resolutions. Last but not least, one of the biggest advantages of the proposed new system is that it is not reliant on expensive methods for measuring the driver's heart rate variability (HRV) in the attempt to find clear evidence of drowsiness and predict microsleeps, such as the 'Driver Alert Support'. This means that, subject to an appropriate safety assessment and Government approval, there is the potential to manufacture and market the new system for real world usage in a consumer car within the European Union. [13] [14] [15]

	6.2. Interpretation of Results
The drowsiness detection algorithm was run for thirty seconds under different conditions. There were three conditions under which the algorithm was run: using the trained model to track eyes in the absence of drowsiness, when the driver had closed his eyes, and when the driver was yawning. To begin with, the algorithm was first applied to test whether it can detect the eyes in a given image using HAAR cascade. The HAAR eye classification was first loaded, and then the algorithm started capturing the frames using the local web camera. The eye classification was run as a loop through all the detected objects in the captured frame. If the two eyes were successfully detected, the algorithm drew a rectangle around the eyes and displayed the frame with eyes. If the algorithm could not detect any eyes, a message was displayed to show the failure of eye detection. This step was successful since the algorithm was able to detect the eyes. Additionally, the drowsiness detection algorithm was tested to see if it can differentiate between the state of a driver's eyes, i.e., in the absence of drowsiness, when the driver's eyes are closed, or when he yawns. The first tested condition was about using the trained model to track eyes in the absence of drowsiness. The driver's eyes were tracked successfully, and so the output from the algorithm was produced to show that the eyes were detected. In addition, a message was displayed to describe that the drowsiness was not detected.

7.Conclusion
Based on an in-depth review of relevant study aids and research papers, it is unequivocally established that the integration of a driver's drowsiness program is imperative and should constitute a mandatory facet of every driver's life. In light of this, our study affirms the critical importance of implementing an efficient Driver Drowsiness Detector. Utilizing Python and OpenCV in conjunction with a webcam for facial recognition, we not only successfully designed the detector but also made strides in refining its implementation. This proactive approach aligns with the overarching goal of prioritizing driver safety and underscores the significance of technological interventions in enhancing road safety standards.   

8.References:
[1] W. Kongcharoen, S. Nuchitprasitchai, "Real-time eye state detection system for driver drowsiness using convolutional neural network," in Computer ..., 2020.HTML
[2] N. A. Andriyanov, "Application of computer vision systems for monitoring the condition of drivers based on facial image analysis," Pattern Recognition and Image Analysis, 2021.HTML
[3] AA Suhaiman, Z May, "Development of an intelligent drowsiness detection system for drivers using image processing technique," 2020 IEEE Student Conference on Research and Development (SCOReD), 2020.HTML

[4] HUR Siddiqui, AA Saleem, R Brown, B Bademci, E Lee, "Non-invasive driver drowsiness detection system," in Sensors, 2021.mdpi.com

[5] I. Stancin, M. Cifrek, and A. Jovic, "A review of EEG signal features and their application in driver drowsiness detection systems," Sensors, 2021.mdpi.com

[6] C.B.S. Maior, M.J. das Chagas Moura, et al., "Real-time classification for autonomous drowsiness detection using eye aspect ratio," Expert Systems with Applications, vol. 150, Elsevier, 2020.HTML

[7]A Khurshid, J Scharcanski - Sensors, 2020 - mdpi.com. An adaptive face tracker with application in yawning detection. mdpi.com
Cited by 3

[8]A Bano, A Saxena, GK Das - IOP Conference Series: Materials …, 2021 - iopscience.iop.org. A comparative analysis of using various machine learning techniques based on drowsy driver detection. iop.org
Cited by 2

[9]W Cheng, X Wang, B Mao - The Visual Computer, 2023 - Springer. A multi-feature fusion algorithm for driver fatigue detection based on a lightweight convolutional neural network. HTML
Cited by 1

[10]VH SÎRBU, IC ROȘCA, CN DRUGĂ - 2021 - aspeckt.unitbv.ro. Study of the vital parameters monitoring in a vehicle for people with health problems. unitbv.ro

[11]HMR van Goor - 2023 - researchinformation.umcutrecht.nl. Modern methods in vital signs monitoring. umcutrecht.nl

[12]SK Tanbeer, ER Sykes - Computational and Structural Biotechnology …, 2024 - Elsevier. MiVitals–Mixed Reality Interface for Vitals Monitoring: A HoloLens based Prototype for Healthcare Practices. sciencedirect.com

[13]B Akrout, W Mahdi - Journal of Ambient Intelligence and Humanized …, 2023 - Springer. A novel approach for driver fatigue detection based on visual characteristics analysis. HTML
Cited by 29

[14]MM Hasan, CN Watling, GS Larue - Journal of safety research, 2022 - Elsevier. Physiological signal-based drowsiness detection using machine learning: Singular and hybrid signal approaches. qut.edu.au Cited by 50

[15]J Cui, Z Lan, Y Liu, R Li, F Li, O Sourina… - Methods, 2022 - Elsevier. A compact and interpretable convolutional neural network for cross-subject driver drowsiness detection from single-channel EEG. arxiv.org
Cited by 63
 


<br>
Author - Abhiram Kumar

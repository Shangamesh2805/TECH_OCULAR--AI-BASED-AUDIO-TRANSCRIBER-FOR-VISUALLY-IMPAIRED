# Smart-Glass


**Field of the invention:**

Vision plays a major role in our day today life.Vision is a essential factor which helps us to survive. Our main idea is  to develop a smart glass for visually challeged people toread books without any guide to dictate. Our project helps visualy impaired people as a artificial eye and scans the books using camera fixed on smart glass which is connect to a H-computing device jetson-nano  it extracts the text from the taken image and give it as audio output to the visually challenged people.
Visually impaired people can gain more knowledge independently by using our project idea. So, we design a spectacle which is different from ordinary one, it consists of a camera, earphones, microphone and ultrasonic sensor. We get a voice command to access camera and scan the book or any other document which the user wants to read. We extract the text from the image using OCR (Tesseract model) and using gTTs the extracted text is converted into voice output and we pass the output using headphones to the user.  We run this model in raspberry pi. This can be implemented for multiple language based on the users need. Children with slight or severe impairments of any physical organ or children who are mentally unstable are given special talents to aid them in absorbing the normal life process. According to UNESCO's report on children with disabilities, 27% of impaired children between the ages of 5 and 19 do not have access to education. We consider providing them with a supportive and growing environment where they can live and grow. In the educational ecosystem, the needs of such an environment need to be catered according to the category of ailments that exist in the students and provisions need to be made to make them feel special, and cared for and set the right mindset while they grow. Vision plays a major role among all senses. With just little aid to the visually impaired people existing currently, there is a need to implement a device that aids them in their educational purpose. The goal is to provide inexpensive solutions to the visually impaired and make their lives better and more self-sufficient. Techocular is made to aid school children with total or partially impaired eyesight without needing a guardian to improve their knowledge. The configuration of hardware and software units is to be designed, which leads to the recognition of texts from the given source and converts it to audio input for the user. We present a method, which uses Optical Character Recognition on the live stream of images and Natural language  Processing for further conversion for expected output.

**Modules Used:**

• pygame

• speech_recognition

• pyttsx3

• speech_recognition 

• wikipedia

• webbrowser

• smtplib

• cv2

• pytesseract

• gtts 

**WORKING:**

The developed product has an edge computing device- Jetson nano playing a major role. The microphone is used to recognize the voice and it is connected to the jetson nano which accesses the camera and takes pictures. By reconizes voice command from the user by specific keywords. The model can be static where the camera can be fixed to the stand and the books are placed under or it can be a portable mobile one where the whole setup is made as a wearable device like normal glass. After capturing the picture of book or document the image is processed using NN to get a clear clarity of text in the picture.Then the extracted text from the image is then converted into an audio file . The output is given via headphones or through a speaker which has been connected. The power supply is given through a Power bank to make it portable and simple. Wi-fi module and Bluetooth module are installed inside the Jetson nano which helps in wifi and bluetooth connectivity. The audio command are prefined commands which should informed to users early and they are customisable commands according to user needs. To improve the clarity of image which the model processes we made a alogorithm to increase thr focus time of camera as focusing the image before a image is taken plays a import role. As a of it our model would 
wait for 5 seconds and capture the image.



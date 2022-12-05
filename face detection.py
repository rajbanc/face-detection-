import cv2

# define a video capture object
cap = cv2.VideoCapture(0)
face_classifier = cv2.CascadeClassifier(cv2.data.haarcascades +
                                       'haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml')									   

while True:
    # Capture the video frame
    # by frame
    ret, frame = cap.read()
    faces =face_classifier.detectMultiScale(frame)
    for face in faces:
        # extract
        x, y, width, height = face
        x2 = x + width
        y2 = y + height
        # draw a rectangle over the pixels
        frame_d = frame.copy()
        cv2.rectangle(frame_d, (x, y), (x2, y2), (255, 0, 0), 1)
		  # show the image

        cv2.imshow('frame', frame_d)
		# Display an original image
	    
        cv2.imshow('Original',frame)



      # Detects eyes of different sizes in the input image
    eyes = eye_cascade.detectMultiScale(frame) 
  
        #To draw a rectangle in eyes
    for (ex,ey,ew,eh) in eyes:
        cv2.rectangle(frame_d,(ex,ey),(ex+ew,ey+eh),(0,0,255),2)
  

        # show the image

        cv2.imshow('frame', frame_d)
		
        # Display an original image
	    
        
        cv2.imshow('Original',frame)  



    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
# close the window
cv2.destroyAllWindows()
    
	
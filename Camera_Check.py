# This code is used for automatic collection of Image Dataset for Creating Custome Model Training 
import cv2

def main():
    # Open the video camera (default camera or the one specified)
    cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)  # Change the parameter to the camera index if you have multiple cameras
    
    # Check if the camera opened successfully
    if not cap.isOpened():
        print("Error: Could not open camera.")
        return
    
    # Loop to continuously read frames from the camera
    while True:
        # Capture frame-by-frame
        ret, frame = cap.read()
        
        # Check if the frame was successfully captured
        if not ret:
            print("Error: Could not read frame.")
            break
        
        # Display the captured frame
        cv2.imshow('Video Feed', frame)
        
        # Check for the 'q' key to quit the program
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    
    # Release the camera and close the OpenCV windows
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()

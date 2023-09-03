import jetson.inference
import jetson.utils


# Load the object detection model
net = jetson.inference.detectNet("ssd-mobilenet-v2", threshold=0.5)

# Initialize the camera
camera = jetson.utils.gstCamera(1280, 720, "/dev/video0")

# Initialize the display
display = jetson.utils.glDisplay()

while display.IsOpen():
    img, width, height = camera.CaptureRGBA()

    # Detect objects in the image
    detections = net.Detect(img, width, height)

    for detection in detections:
        print("Class ID: {}, Confidence: {}, Area: {}"
              .format(detection.ClassID, detection.Confidence, detection.Area))

    display.RenderOnce(img, width, height)
    display.SetTitle("Object Detection | Network {:.0f} FPS".format(net.GetNetworkFPS()))

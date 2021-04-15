import cv2
import argparse
import random

path='./train/'
caffemodel=f'{path}/snapshots/_iter_40000.caffemodel'
prototxt=f'{path}/deploy_dpe_220_v4.prototxt'
labels=["White", "Black", "Asian", "Indian"]

def get_random_file():
    """

    Returns:
        random filename of image and its class.
    """

    filename=f'{path}/test.txt'
    lines=[]

    with open(filename) as f:
        lines=f.readlines()
    
    line=f'{path}/{random.choice(lines)}'.split(' ')
    filename=line[0]
    label=int(line[1])
    return filename, labels[label]

# main
parser=argparse.ArgumentParser()
parser.add_argument("-i", "--image", type=str, required=False, help="input image")
args=parser.parse_args()

# image
if args.image is None:
    filename, label=get_random_file()
else:
    filename=args.image; label=None

print(f'Image: {filename}')
print(f'Original label: {label}')

# racenet
racenet=cv2.dnn.readNet(caffemodel, prototxt)
image=cv2.imread(filename)
blob=cv2.dnn.blobFromImage(image, 1.0, (224,224), (104, 117, 123), swapRB=False)
racenet.setInput(blob)
predictions=racenet.forward()

# results
print(f'Predicted label: {labels[predictions[0].argmax()]}')

while True:
    cv2.imshow('Output', image)

    # Press 'q' to quit
    if cv2.waitKey(1) == ord('q'):
        break
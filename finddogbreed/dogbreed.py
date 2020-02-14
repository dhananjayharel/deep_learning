from keras.models import load_model
from keras.preprocessing import image
import numpy as np
from keras.applications.resnet50 import ResNet50
from keras.applications.resnet50 import preprocess_input, decode_predictions
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

# Load your trained model
#probably don't need this as the h5 model already used Resnet
from keras.applications.resnet50 import ResNet50
#define ResNet50 model
ResNet50_model = ResNet50(weights='imagenet')
#ResNet50_model.save('resnet50dogbreed.h5')
#model = load_model(MODEL_PATH)
#model._make_predict_function()  

################################
ImageToTest = "White_Persian_Cat.jpg"
###############################

img = image.load_img(ImageToTest, target_size=(224, 224))

# Preprocessing the image
x = image.img_to_array(img)
# x = np.true_divide(x, 255)
x = np.expand_dims(x, axis=0)

 # Be careful how your trained model deals with the input
# otherwise, it won't make correct prediction!
x = preprocess_input(x, mode='caffe')

preds = ResNet50_model.predict(x)
decoded = decode_predictions(preds, top=1)[0]
print('Predicted:', decoded)
l = list(decoded[0])
img = mpimg.imread(ImageToTest)
plt.imshow(img)
plt.axis('off')
plt.suptitle('Breed: '+l[1]+ ' ', fontsize=20)
plt.savefig('output.png')
print("SUCCESS")
print("")



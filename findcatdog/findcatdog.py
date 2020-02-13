from keras.models import load_model
from keras.preprocessing import image
import numpy as np

import matplotlib.pyplot as plt
import matplotlib.image as mpimg


################################
ImageToTest = "testcat.jpg"
###############################


#processing code
model = load_model('model.h5')
labelNames = ["cat", "dog"]
dog_img = image.load_img(ImageToTest, target_size=(64, 64))
dog_img = image.img_to_array(dog_img)
dog_img = np.expand_dims(dog_img, axis=0)
dog_img = dog_img/255


result = model.predict_classes(dog_img)

print('')
print("-------------------------------------------------------")
print("The machine has found "+labelNames[result[0]]+" in the image!")
img = mpimg.imread(ImageToTest)
plt.imshow(img)
plt.axis('off')
plt.suptitle('found '+labelNames[result[0]]+ ' in the image!', fontsize=20)
plt.savefig('output.png')
print("SUCCESS")
print("")


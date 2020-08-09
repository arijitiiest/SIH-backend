from .mrcnn import visualize
from .mrcnn.visualize import display_instances
from .mrcnn.visualize import display_images
from .mrcnn import utils
from .mrcnn.config import Config
from .mrcnn import model as modellib
import skimage
import scipy
from .custom import CustomConfig

import tensorflow as tf
from tensorflow.python.keras.backend import set_session
import string
import random

result_path = "media/model/"

class_names = ['Background', 'PotHole']


class InferenceConfig(CustomConfig):
    GPU_COUNT = 1
    IMAGES_PER_GPU = 1


config = InferenceConfig()
config.display()

# global graph
sess = tf.Session()
graph = tf.compat.v1.get_default_graph()


class Model:
    """model for 
    importing and saving the predicted image
    """

    def __init__(self):
        # self.model = 0
        pass

    def load(self):
        set_session(sess)
        self.model = modellib.MaskRCNN(
            mode="inference", model_dir="", config=config)

        # define the correct path of the model
        self.model.load_weights(
            "/home/arijitiiest/Desktop/Workspace/Project/SIH/Backend/backend/roads/model/mask_rcnn_damage_0160.h5", by_name=True)

    def predict(self, image_path):
        image = skimage.io.imread(image_path)

        # Run detection
        global sess
        global graph
        with graph.as_default():
            set_session(sess)
            results = self.model.detect([image], verbose=1)

            res = ''.join(random.choices(string.ascii_uppercase +
                                         string.digits, k=15))

            # Visualize results
            r = results[0]
            # result_path = result_path + str(res)
            display_instances(image, r['rois'], r['masks'], r['class_ids'],
                              class_names, r['scores'], save_path=result_path + str(res))

            if len(r['scores']) == 0:
              PCI = 0
            else:
              PCI = 139-(sum(r['scores']*100)/len(r['scores']))

        return result_path + str(res), r['scores']*100, PCI
        # r['scores'] defines the risk level and it has to be showed: 80-90 low risk, 91-95 moderate risk, 95-100 high risk


#######example############
'''
m = Model()
m.load()
result_path , scores = m.predict('sampleimage.jpg')

'''

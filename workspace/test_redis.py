from src.providers import RedisService
from src.utils import image_manage
import numpy as np
import cv2


RS = RedisService.CacheService()

img = cv2.imread("assets/123.jpg", cv2.IMREAD_COLOR)
np_img = np.array(img)
base64_img = image_manage.convert_np_2_base64(np_img)


### Insert byte img
RS.set_hash(field = 'img1',value=base64_img)


### Query 
base64_img = RS.get_hash(field = 'img1')

### Decode
image_np = image_manage.convert_base64_2_np(base64_img)



cv2.imshow("image", image_np)
cv2.waitKey(0)
cv2.destroyAllWindows()
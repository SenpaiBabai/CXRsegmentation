import numpy as np
import torch
from torch.utils.data import Dataset, DataLoader
import cv2
import imageio


class LungSegmentationDataset(Dataset):
    def __init__(self, image_list, path, parts_of_body=('left lung', 'right lung'), transformations=None):
        self.path = path
        self.images = image_list
        self.transformations = transformations
        self.parts_of_body = parts_of_body

    def __len__(self):
        return len(self.images)

    def __getitem__(self, index):
        filename = self.images[index]
        image = cv2.imread(str(self.path / 'Images' / filename), cv2.IMREAD_COLOR)
        mask_name = filename.split(".")[0] + ".gif"
        result = {'image': image, 'heart': None, 'left clavicle': None, 'left lung': None, 'right clavicle': None,
                  'right lung': None}

        for part in self.parts_of_body:
            img = imageio.imread(str(self.path / 'scratch' / 'masks' / part / mask_name))
            if len(img.shape) == 2:
                img = np.repeat(img[..., None], 3, -1)
            result[part] = img

        result = {key: value for key, value in result.items() if value is not None}

        if self.transformations:
            result = self.transformations(**result)
        to_stack = []
        for key, value in result.items():
            if key != 'image':
                mask = value[0] if isinstance(value, torch.Tensor) else torch.tensor(value[..., 0])
                mask -= mask.min()
                mask = mask / mask.max()
                mask = torch.round(mask)
                to_stack.append(mask)

        result['image'] -= result['image'].min()
        result['image'] = result['image'] / result['image'].max()

        return result['image'], torch.stack(to_stack)

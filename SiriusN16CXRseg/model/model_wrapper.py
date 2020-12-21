import torch
from albumentations.augmentations.transforms import Resize
from albumentations.pytorch import ToTensorV2
from albumentations import Normalize, Compose


def return_masks(model, img, threshold=0.5,
                 device=torch.device("cuda:0")):
    transforms = Compose([Resize(224, 224), Normalize(), ToTensorV2()])
    img = transforms(image=img)['image']
    #img = torch.tensor(img)
    img -= img.min()
    img = img / img.max()
    img = img[None, ...]
    img = img.to(device)
    model = model.to(device)
    model.eval()
    prediction = (model(img) > threshold).cpu().numpy().astype(int)[0]
    answer = {'Heart': prediction[0], 'Left lung': prediction[1], 'Right lung': prediction[2]}
    return answer

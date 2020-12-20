import torch
from time import time


def train_one_epoch(model, train_dataloader, criterion, optimizer, device=torch.device("cuda:0")):
    model.train()
    running_loss = 0.0
    for i, data in enumerate(train_dataloader):
        inputs, labels = data
        inputs, labels = inputs.to(device), labels.to(device)

        optimizer.zero_grad()

        outputs = model(inputs)
        loss = criterion(outputs, labels)
        loss.backward()
        optimizer.step()

        running_loss += loss.item()

    return running_loss / len(train_dataloader)


def predict(model, val_dataloder, criterion, device="cuda:0"):
    model.to(device)
    model.eval()
    running_loss = 0.0
    with torch.no_grad():
        for i, data in enumerate(val_dataloder):
            inputs, labels = data
            inputs, labels = inputs.to(device), labels.to(device)
            outputs = model(inputs)

            loss = criterion(outputs, labels)
            running_loss += loss.item()

    return running_loss / len(val_dataloder)


def train(model, train_dataloader, val_dataloader, criterion, optimizer, device=torch.device("cuda:0"), n_epochs=10,
          scheduler=None):
    model.to(device)
    for epoch in range(n_epochs):
        start = time()
        train_loss = train_one_epoch(model, train_dataloader, criterion, optimizer, device=device)
        val_loss = predict(model, val_dataloader, criterion, device=device)
        print('{:.2f}s === Epoch [{}] - Loss: {} - Val_loss: {}'.format(time() - start, epoch, train_loss, val_loss))
        if scheduler is not None: scheduler.step(val_loss)

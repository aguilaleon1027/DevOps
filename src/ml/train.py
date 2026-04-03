import torch
import torch.nn as nn
import torch.optim as optim
import mlflow
import os

class SimpleWorkoutNet(nn.Module):
    def __init__(self, input_dim, output_dim):
        super(SimpleWorkoutNet, self).__init__()
        self.fc1 = nn.Linear(input_dim, 64)
        self.relu = nn.ReLU()
        self.fc2 = nn.Linear(64, output_dim)

    def forward(self, x):
        out = self.fc1(x)
        out = self.relu(out)
        out = self.fc2(out)
        return out

def train_model():
    print("Initializing training for the Workout Recommender Model...")
    mlflow.set_tracking_uri("sqlite:///mlruns.db")
    mlflow.set_experiment("Workout-Recommender")
    
    with mlflow.start_run():
        # Hyperparameters
        input_dim = 5 # age, gender(encoded), weight, target_muscle, goal
        output_dim = 10 # Assuming 10 workout templates to classify into
        learning_rate = 0.001
        epochs = 100
        
        mlflow.log_param("learning_rate", learning_rate)
        mlflow.log_param("epochs", epochs)
        
        model = SimpleWorkoutNet(input_dim, output_dim)
        criterion = nn.CrossEntropyLoss()
        optimizer = optim.Adam(model.parameters(), lr=learning_rate)
        
        # Dummy data for demonstration
        # In reality, you'll load data from data/processed
        inputs = torch.randn(100, input_dim)
        targets = torch.randint(0, output_dim, (100,))
        
        # Training loop
        for epoch in range(epochs):
            optimizer.zero_grad()
            outputs = model(inputs)
            loss = criterion(outputs, targets)
            loss.backward()
            optimizer.step()
            
            if (epoch+1) % 20 == 0:
                print(f"Epoch [{epoch+1}/{epochs}], Loss: {loss.item():.4f}")
                mlflow.log_metric("loss", loss.item(), step=epoch)
                
        # Save model
        os.makedirs("models", exist_ok=True)
        torch.save(model.state_dict(), "models/current_model.pt")
        mlflow.pytorch.log_model(model, "model")
        print("Model trained and logged to MLflow.")

if __name__ == "__main__":
    train_model()

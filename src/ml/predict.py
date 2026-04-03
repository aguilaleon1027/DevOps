import torch
from src.ml.train import SimpleWorkoutNet

def load_model(model_path="models/current_model.pt"):
    input_dim = 5
    output_dim = 10
    model = SimpleWorkoutNet(input_dim, output_dim)
    try:
        model.load_state_dict(torch.load(model_path))
        model.eval()
        return model
    except FileNotFoundError:
        print("Model file not found. Please train the model first.")
        return None

def predict(model, input_features: list):
    """
    input_features might be: [age, gender_encoded, current_weight, target_muscle]
    """
    with torch.no_grad():
        tensor_input = torch.tensor([input_features], dtype=torch.float32)
        outputs = model(tensor_input)
        _, predicted_class = torch.max(outputs.data, 1)
        return predicted_class.item()

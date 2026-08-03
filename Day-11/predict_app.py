import pickle

model = pickle.load(open('score_predictor.pkl', 'rb'))

print("=== Student Score Predictor ===")

while True:
    user_input = input("\nEnter weekly study hours (or 'exit' to quit): ")

    if user_input.lower() == 'exit':
        print("Goodbye!")
        break

    try:
        hours = float(user_input)
        if hours < 0:
            print("Study hours can't be negative. Try again.")
            continue

        predicted_score = model.predict([[hours]])[0]
        predicted_score = max(0, min(100, predicted_score))

        print(f"Predicted Average Score: {round(predicted_score, 2)}")

        if predicted_score >= 85:
            print("Excellent! Keep up the great study habits.")
        elif predicted_score >= 60:
            print("Good work — a bit more study time could push this higher.")
        else:
            print("Consider increasing your study hours for better results.")

    except ValueError as e:
        print("Please enter a valid number.")
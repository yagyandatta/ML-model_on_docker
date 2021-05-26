import joblib

model = joblib.load('exp.pk1')
x = float(input("Enter Years of Experience(in decimal): "))
result = int(model.predict([[x]]))
print(f"Salary will be : ₹{result}") 

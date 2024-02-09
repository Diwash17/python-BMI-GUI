import tkinter as tk

def calculate_bmi():
    # Get user input for weight in kilograms and height in centimeters
    weight = float(entry_weight.get())
    height = float(entry_height.get())

    # Convert height from centimeters to meters for BMI calculation
    height_in_meters = height / 100

    # Calculate BMI using the formula: BMI = weight / height^2
    bmi = weight / (height_in_meters ** 2)

    # Display the calculated BMI
    result_label.config(text=f"Your BMI is: {bmi:.2f}")

    # Determine the BMI category and provide a message
    if bmi < 18.5:
        category_label.config(text="You are underweight.")
    elif 18.5 <= bmi < 25:
        category_label.config(text="You have a normal weight.")
    elif 25 <= bmi < 30:
        category_label.config(text="You are overweight.")
    else:
        category_label.config(text="You are obese.")

# Create the main window
window = tk.Tk()
window.title("BMI Calculator")

# Create and place widgets in the window
label_weight = tk.Label(window, text="Weight (kg):")
label_weight.grid(row=0, column=0, padx=10, pady=10,)

entry_weight = tk.Entry(window)
entry_weight.grid(row=0, column=1, padx=10, pady=10)

label_height = tk.Label(window, text="Height (cm):")
label_height.grid(row=1, column=0, padx=10, pady=10)

entry_height = tk.Entry(window)
entry_height.grid(row=1, column=1, padx=10, pady=10)

calculate_button = tk.Button(window, text="Calculate BMI", command=calculate_bmi)
calculate_button.grid(row=2, column=0, columnspan=2, pady=10,)

result_label = tk.Label(window, text="")
result_label.grid(row=3, column=0, columnspan=2, pady=10)

category_label = tk.Label(window, text="")
category_label.grid(row=4, column=0, columnspan=2, pady=10)

# Start the GUI event loop
window.mainloop()

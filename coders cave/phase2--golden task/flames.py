import tkinter as tk


def calculate_flames(name1, name2):
    name1 = name1.lower()
    name2 = name2.lower()

    # Remove common characters
    common_chars = []
    for char in name1:
        if char in name2:
            common_chars.append(char)
            name2 = name2.replace(char, '', 1)

    for char in common_chars:
        name1 = name1.replace(char, '', 1)

    total_chars = len(name1) + len(name2)

    # Define FLAMES letters
    flames_letters = ['F', 'L', 'A', 'M', 'E', 'S']

    # Start removing letters based on the FLAMES count
    current_index = 0
    while len(flames_letters) > 1:
        current_index = (current_index + total_chars - 1) % len(flames_letters)
        flames_letters.pop(current_index)

    return flames_letters[0]


def calculate_button_click():
    player_one_name = player_one_entry.get()
    player_two_name = player_two_entry.get()

    result = calculate_flames(player_one_name, player_two_name)

    history_listbox.insert(tk.END, f"{player_one_name} and {player_two_name} -> {result} ({meanings[result]})")


# Create the tkinter app
app = tk.Tk()
app.title("FLAMES Calculator")

# Create labels and entry fields
player_one_label = tk.Label(app, text="Enter your name:")
player_one_label.grid(row=0, column=0)
player_one_entry = tk.Entry(app)
player_one_entry.grid(row=0, column=1)

player_two_label = tk.Label(app, text="Enter your partner's name:")
player_two_label.grid(row=1, column=0)
player_two_entry = tk.Entry(app)
player_two_entry.grid(row=1, column=1)

calculate_button = tk.Button(app, text="Calculate", command=calculate_button_click)
calculate_button.grid(row=2, column=0, columnspan=2)

history_label = tk.Label(app, text="History:")
history_label.grid(row=3, column=0, columnspan=2)

history_listbox = tk.Listbox(app, width=50)
history_listbox.grid(row=4, column=0, columnspan=2)

meanings = {
    'F': 'Friendship',
    'L': 'Love',
    'A': 'Affection',
    'M': 'Marriage',
    'E': 'Enemy',
    'S': 'Sibling',
}

app.mainloop()

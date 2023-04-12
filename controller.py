import pylirc
import time

# Define the IR codes for each button press
IR_CODES = {
    'POWER': 'KEY_POWER',
    'VOLUME_UP': 'KEY_VOLUMEUP',
    'VOLUME_DOWN': 'KEY_VOLUMEDOWN',
    'CHANNEL_UP': 'KEY_CHANNELUP',
    'CHANNEL_DOWN': 'KEY_CHANNELDOWN',
    'MENU': 'KEY_MENU',
    'HOME': 'KEY_HOME',
    'INPUT': 'KEY_SOURCE',
}

# Connect to the LIRC daemon
pylirc.init()

# Define a function to send an IR signal
def send_ir_signal(ir_code):
    pylirc.send_once("samsung", ir_code)

# Define the main function that handles the button clicks
def button_click(ir_code):
    # Send the IR signal
    send_ir_signal(ir_code)
    
    # Wait a moment before sending the next signal
    time.sleep(0.1)

# Create a GUI window
window = tk.Tk()
window.title("Samsung AU7100 75 Remote")

# Create buttons for each function
for function_name, ir_code in IR_CODES.items():
    button = tk.Button(window, text=function_name, font=("Arial", 24), width=10, height=2, command=lambda ic=ir_code: button_click(ic))
    button.pack()

# Start the main event loop
window.mainloop()

# Disconnect from the LIRC daemon
pylirc.exit()

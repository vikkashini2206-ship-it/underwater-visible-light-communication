import random
import time

def simulate_underwater_vlc(message, water_clarity=0.9, distance_meters=5):
    """
    water_clarity: 1.0 (Crystal Clear) to 0.1 (Muddy)
    distance_meters: Distance between virtual LED and Receiver
    """
    print(f"--- STARTING VIRTUAL UVLC TRANSMISSION ---")
    print(f"Message: '{message}' | Distance: {distance_meters}m | Clarity: {water_clarity}")
    
    received_message = ""
    
    for char in message:
        # Calculate 'Probability of Success' for each letter
        # Light intensity drops exponentially: I = I0 * e^(-k * d)
        success_chance = (water_clarity ** distance_meters)
        
        time.sleep(0.1) # Simulate transmission speed
        
        if random.random() < success_chance:
            received_message += char
            print(f"  [PASS] Transmitted '{char}' successfully.")
        else:
            received_message += "?" # Data lost underwater
            print(f"  [LOST] Signal for '{char}' scattered by particles.")
            
    print(f"\n--- RESULTS ---")
    print(f"Original: {message}")
    print(f"Received: {received_message}")
    
    accuracy = (len([c for c in received_message if c != '?']) / len(message)) * 100
    print(f"Link Accuracy: {accuracy:.1f}%")

if __name__ == "__main__":
    msg = input("Enter message to send through virtual water: ")
    # Try changing clarity to 0.5 to see what happens!
    simulate_underwater_vlc(msg, water_clarity=0.85, distance_meters=3)
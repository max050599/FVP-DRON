class AdaptiveHopper:
    def __init__(self, frequencies):
        self.frequencies = frequencies
        self.current_frequency = frequencies[0]
        self.interference_threshold = 0.7  # Example threshold for interference detection

    def detect_interference(self, signal_strength):
        return signal_strength < self.interference_threshold

    def switch_frequency(self):
        current_index = self.frequencies.index(self.current_frequency)
        next_index = (current_index + 1) % len(self.frequencies)
        self.current_frequency = self.frequencies[next_index]
        print(f"Switched to frequency: {self.current_frequency}")

    def operate(self, signal_strength):
        if self.detect_interference(signal_strength):
            print("Interference detected. Switching frequency...")
            self.switch_frequency()
        else:
            print("Signal is clear. Operating on current frequency.")
class PIDController:
    def __init__(self, kp, ki, kd):
        self.kp = kp
        self.ki = ki
        self.kd = kd
        self.previous_error = 0
        self.integral = 0

    def update(self, setpoint, measured_value, dt):
        error = setpoint - measured_value
        self.integral += error * dt
        derivative = (error - self.previous_error) / dt

        output = (self.kp * error) + (self.ki * self.integral) + (self.kd * derivative)

        self.previous_error = error
        return output

    def reset(self):
        self.previous_error = 0
        self.integral = 0

    def set_gains(self, kp, ki, kd):
        self.kp = kp
        self.ki = ki
        self.kd = kd
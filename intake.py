import wp
import wpilib.drive
import rev


class Intake:

    def __init__(self):
        
        self.intake_motor = rev.SparkMax(1, rev.SparkLowLevel.MotorType.kBrushless)
        self.intake_retract_motor = rev.SparkMax(2, rev.SparkLowLevel.MotorType.kBrushless)

     
     

    def turnOnIntake(self):
       
        self.intake_motor.set(1)
        self.intake_retract_motor.set(-0.5)

    def raiseIntake(self):
        self.intake_retract_motor.set(0.4)
        self.intake_motor.set(0)

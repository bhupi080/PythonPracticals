class Human:
    legs=2
    @classmethod
    def walk(cls,name):
        print(f'{name} walks with {cls.legs} legs...')
Human.walk('Bhupi')
Human.walk('Deepti')

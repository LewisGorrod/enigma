
import os
alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

class Rotor:
    def __init__(self, internal_wiring, turnover_notch):
        self.internal_wiring = internal_wiring
        self.turnover_notch = turnover_notch
        self.ring_setting = 0 # permanent offset
        self.position = 0 # additional temporary offset

    def encipher(self, char):
        return self.internal_wiring[(alphabet.index(char) + self.position + self.ring_setting) % 26]
    
    def decipher(self, char):
        return alphabet[(self.internal_wiring.index(char) - self.position - self.ring_setting) % 26]
    
    def setRingSetting(self, ring_setting):
        self.ring_setting = ring_setting

    def setStartingPosition(self, starting_position):
        self.position = starting_position

    def rotate(self):
        self.position = (self.position + 1) % 26

    def charVisible(self):
        return self.internal_wiring[(self.position + self.ring_setting) % 26]

class Enigma:
    def __init__(self):
        self.reflector = Rotor('QYHOGNECVPUZTFDJAXWMKISRBL', None)
        self.rotorI = Rotor('EKMFLGDQVZNTOWYHXUSPAIBRCJ', 'Q')
        self.rotorII = Rotor('AJDKSIRUXBLHWTMCQGZNPYFVOE', 'E')
        self.rotorIII = Rotor('BDFHJLCPRTXVZNYEIWGAKMUSQO', 'V')
        self.rotorIV = Rotor('ESOVPZJAYQUIRHXLNFTGKDCMWB', 'J')
        self.rotorV = Rotor('VZBRGITYUPSDNHLXAWMJQOFECK', 'Z')
        self.rotors = []

    def setRotorOrder(self, rotor_orders):
        for rotor in rotor_orders.split(' '):
            self.rotors.append(self.__dict__[f'rotor{rotor}'])

    def setRingSettings(self, ring_settings):
        ring_settings = [int(i) for i in ring_settings.split(' ')]
        for i in range(3):
            self.rotors[i].ring_setting = ring_settings[i]

    def setStartingRotorPositions(self, starting_rotor_positions):
        starting_rotor_positions = [int(i) for i in starting_rotor_positions.split(' ')]
        for i in range(3):
            self.rotors[i].setStartingPosition(starting_rotor_positions[i])

    def keypress(self, char):
        # turn rotors
        self.rotors[2].rotate()
        if self.rotors[2].charVisible() == self.rotors[2].turnover_notch:
            self.rotors[1].rotate()
        if self.rotors[1].charVisible() == self.rotors[1].turnover_notch:
            self.rotors[0].rotate()
        return self.rotors[2].decipher(self.rotors[1].decipher(self.rotors[0].decipher(self.reflector.encipher(self.rotors[0].encipher(self.rotors[1].encipher(self.rotors[2].encipher(char)))))))

    def printRotorCharsVisible(self):
        for rotor in self.rotors:
            print(rotor.charVisible(), end=' ')
        print()

e = Enigma()
e.setRotorOrder('III IV I')
e.setRingSettings('1 1 1')
e.setStartingRotorPositions('1 2 3')
e.printRotorCharsVisible()
cipher_text = ''
while True:
    os.system('cls')
    e.printRotorCharsVisible()
    print(cipher_text)
    cipher_text += e.keypress(input())
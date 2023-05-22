# Enigma.py (UNFINISHED)

A simple python implementation of the notorious WW2 Enigma Machine.
https://www.wikiwand.com/en/Enigma_machine

## Overview

The Enigma machine may be used to both encipher and decipher messages, provided the user knows the machine settings (aka. the 'cipher key').

Settings consist of:
1. Rotor selection and order
2. Ring settings
3. Starting rotor positions
4. Plugboard configuration

## Instructions

The program may be run on Python 3.x with no additional dependencies.

### Machine Settings

The machine settings may be set inside the script itself:
1. Set rotor selection and order in e.setRotorOrder('III IV I')
2. Set ring settings in e.setRingSettings('1 1 1')
3. Set starting rotor positions in e.setStartingRotorPositions('1 2 3')

### Enciphering/ Deciphering Messages

Once the machine settings have been saved, run the program and enter characters in upper case one at a time (just like the real thing).

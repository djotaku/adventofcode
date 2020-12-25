# Day 25

## Part 1

The handshake used by the card and the door involves an operation that transforms a subject number. To transform a subject number, start with the value 1. Then, a number of times called the loop size, perform the following steps:

- Set the value to itself multiplied by the subject number.
- Set the value to the remainder after dividing the value by 20201227.


The cryptographic handshake works like this:

- The card transforms the subject number of 7 according to the card's secret loop size. The result is called the card's public key.
- The door transforms the subject number of 7 according to the door's secret loop size. The result is called the door's public key.
- The card and door use the wireless RFID signal to transmit the two public keys (your puzzle input) to the other device. Now, the card has the door's public key, and the door has the card's public key. Because you can eavesdrop on the signal, you have both public keys, but neither device's loop size.
- The card transforms the subject number of the door's public key according to the card's loop size. The result is the encryption key.
- The door transforms the subject number of the card's public key according to the door's loop size. The result is the same encryption key as the card calculated.

If you can use the two public keys to determine each device's loop size, you will have enough information to calculate the secret encryption key that the card and door use to communicate;

## Part 2

d
#!/usr/bin/env python3

import soundfile as sf
import matplotlib.pyplot as plt
import time


def center_wave(wave, target_size):
    new_wave = []
    missing_size = target_size - len(wave)
    new_wave = [0] * (missing_size // 2)
    new_wave += [w[0] for w in wave]
    new_wave += [0] * (missing_size // 2)
    if len(new_wave) < target_size:
        new_wave.append(0)
    return new_wave

def get_wave(samples):
    size = len(samples)
    quarter = size // 4
    i = size // 4
    sample = samples[i][0]

    while i < (quarter * 3) and sample >= 0.002:
        sample = samples[i][0]
        i += 1

    while i < (quarter * 3) and sample < 0.002:
        sample = samples[i][0]
        i += 1

    i_mid = i
    i_start = i_mid - quarter
    i_end = i_mid + quarter

    print("Start Mid End", i_start, i_mid, i_end)

    return center_wave(samples[i_start:i_end+1], size)

def old_get_wave(samples):
    if samples[0][0] >= 0 and samples[1][0] < 0:
        return samples
    raise ValueError

def print_soundwave(samples, line):
    try:
        wave = get_wave(samples)
    except ValueError:
        return

    line.set_xdata([i for i in range(len(wave))])
    line.set_ydata([e for e in wave])

def main():
    sig, samplerate = sf.read('test.wav')

    print("Samplerate", samplerate)

    plt.ion()

    for i in range(0, len(sig), samplerate//50):
        chunk = sig[i:i+(samplerate//50)]

        if i > 0:
            print_soundwave(chunk, line)
            figure.canvas.draw()
            figure.canvas.flush_events()
        else:
            figure, ax = plt.subplots(1, 1, figsize=(10, 8))
            line,_ = ax.plot([i for i in range(len(chunk))], [(c[0], 0) for c in chunk])

        time.sleep(0.01)

        if i > samplerate*40:
            break


if __name__ == "__main__":
    main()

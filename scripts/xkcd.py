#!/usr/bin/env python3


def gammaCorrection(val):
    if val < 0.03928:
        return val / 12.92
    return ((val + 0.055) / 1.055)**2.4


def getRelativeLuminance(rgb):

    r = gammaCorrection(float(int(rgb[1:3], 16)) / 255) * 0.2126
    g = gammaCorrection(float(int(rgb[3:5], 16)) / 255) * 0.7152
    b = gammaCorrection(float(int(rgb[5:7], 16)) / 255) * 0.0722

    return round(r + g + b, 4)


def getContrastRatio(background, foreground):
    lum_background = getRelativeLuminance(background)
    lum_foreground = getRelativeLuminance(foreground)

    if lum_background < lum_foreground:
        lum_foreground, lum_background, = lum_background, lum_foreground

    return (lum_background + 0.05) / (lum_foreground + 0.05)


def xkcd(at_least):

    import requests
    r = requests.get("https://xkcd.com/color/rgb.txt")

    lines = r.text.split("\n")
    for line in lines[1:]:

        s = line.rstrip("\t ").split("\t")
        if len(s) < 2:
            continue

        name, color = s[0], s[1]

        cr = getContrastRatio("#101010", color)

        if cr > at_least:
            print("{0:<30} # cr({2:02.3f})  {1}".format(
                f"{name.replace(' ', '_')}: \"{color}\"", name, cr))


if __name__ == "__main__":

    # xkcd(3.0)
    print(getContrastRatio("#101010", "#DAC25C"))

# rpi-os-tools

Tools to work with raspberry pi os

# install

Install from pypi with

```pip install rpios-tools```

# usage

## raspios image downloading

To download operating system images you can use the installed command line 
tool `rpios-dl` and specify `--version` and `--release`

To get information on the available versions and releases you can use `rpios-dl`
options like below:

```
$ rpios-dl --list-os-versions
Listing raspios versions available:
        raspios_arm64
        raspios_armhf
        raspios_full_armhf
        raspios_lite_arm64
        raspios_lite_armhf
$ rpios-dl --list-version-releases --version raspios_armhf
Listing {args.version} releases:
        raspios_armhf-2021-05-28
        raspios_armhf-2021-03-25
        raspios_armhf-2021-01-12
        raspios_armhf-2020-12-04
        raspios_armhf-2020-08-24
        raspios_armhf-2020-05-28
```

By default the images will download to an application storage directory
you'll see printed out when the command runs

```
$ rpios-dl --version raspios_lite_armhf --release raspios_lite_armhf-2021-05-28
Downloading raspios:
        version: raspios_lite_armhf
        release: raspios_lite_armhf-2021-05-28
        url: https://downloads.raspberrypi.org/raspios_lite_armhf/images/raspios_lite_armhf-2021-05-28/2021-05-07-raspios-buster-armhf-lite.zip
        path: /Users/michaelsobczak/.local/share/rpi-os-tools/images/2021-05-07-raspios-buster-armhf-lite.zip
 |██████----------------------------------------------------------------------------------------------| 6.4% 
```
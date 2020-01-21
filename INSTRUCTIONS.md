1) Setup - Download Raspbian 

```
2019-09-26-raspbian-buster.zip
Raspbian Buster with desktop
Image with desktop based on Debian Buster
Version: September 2019
Release date: 2019-09-26
Kernel version: 4.19
Size: 1123 MB
```

2) Flash with balenaEtcher

3) Add empty file called `ssh` in the boot partition

4) SSH into the Pi  
> Credentials - `pi:raspberry`

5) Change the password with `passwd`

6) Install screen with `sudo apt install screen`

7) Download the soundboard application  
> `git clone https://github.com/featherbear/pi-soundboard`

8) Add a crontab reboot entry  
`echo "@reboot /home/pi/pi-soundboard/run.sh" | crontab -`

9) Restart the Pi, or start `/home/pi/pi-soundboard/run.sh`

from flet import *
import subprocess
# FOR DETECT INTERFACE WIFI
import netifaces
import time


def main(page:Page):
    page.window_width = 300

    # NOW CREATE TEXT STATUS FOR SHOW CONNECT OR NOT CONNECT
    status = Text(size=30,weight="bold",color="green")

    # NOW I WILL CREATE FUNCTION FOR DETECT SSID 
    # AND YOU CONNECT OR NOT FROM WIFI
    def you_detect():
        youInterface = netifaces.interfaces()
        connected_interface = None
        for iface in youInterface:
            if iface != "lo" and netifaces.AF_INET in netifaces.ifaddresses(iface):
                connected_interface =  iface
                break
        # AND NOW GET SSID NAME YOU CONNECT WIFI
        if connected_interface:
            output = subprocess.check_output(["iwgetid","-r",connected_interface])
            ssid = output.decode("utf-8").strip()
            return ssid

        return None   

    # NOW I WILL CHECK YOU INTERNET CONNECTIN
    # YOU CONNECT INTERNET OR NOT EVERY 2 SECONDS
    def update_status():
        ssid = you_detect()
        if ssid:
            print("you connect ssid is :",ssid)
            status.value = f"you connect ssid is :{ssid}"
            # AND CHANGE TEXT COLOR
            status.color = "green"

        else:
            print("you Not connect !!! ")
            status.value = f"you Not Connect"
            # AND CHANGE TEXT COLOR
            status.color = "red"





    page.add(
        Column([
             status
             ],alignment="center")
        )

    # NOW I WILL CREATE FUNCTION FOR EVERY 2 SECOND
    # FOR MONITOR YOU PC IS ONLINE OR OFFLINE
    def realtime():
        while True:
            update_status()
            # AND UPDATE TEXT STATUS
            status.update()
            # EVERY 2 SECONDS
            time.sleep(2)

    realtime()


flet.app(target=main)

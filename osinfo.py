import subprocess
import socket

class Info():

    def __init__(self) -> None:
        self._host = socket.gethostname()
        self._ip = socket.gethostbyname(self._host)
        self.__output: list[str] = []
        self._devices: list[str] = []
        self._sizes: list[str] = []
        self._useds: list[str] = []
        self._availables: list[str] = []
        self._percents: list[str] = []
        self._mountpoints: list[str] = []
        self._space()

    def __repr__(self) -> str:
        """cette fonction affiche les informations de l'objet"""
        return f"Info: {self.host}"

    def _space(self) -> None:
        df = subprocess.Popen(["df"], stdout=subprocess.PIPE)
        output = df.communicate()[0].decode().split('\n')

        for line in output[1:]:
            if not line:
                continue

            parts = line.split()
            self._devices.append(parts[0])
            self._sizes.append(parts[1])
            self._useds.append(parts[2])
            self._availables.append(parts[3])
            self._percents.append(parts[4])
            self._mountpoints.append(parts[5])
    
    def disks(self) -> dict[str, dict]:
        """
        This function returns information about all the disks on a PC.

        :return: disks
        :rtype: dict
        """
        disks: Dict[str, dict] = {}

        for i in range(len(self._percents)):
            disks[self._devices[i]] = {
                "device": str(self._devices[i]),
                "size": str(self._sizes[i]),
                "used": str(self._useds[i]),
                "available": str(self._availables[i]),
                "percent": str(self._percents[i]),
                "mountpoint": str(self._mountpoints[i])
            }

        return disks

    @property
    def host(self) -> str:
        """la propriété hostname de l'objet"""
        return self._host

    @host.setter
    def host(self, hostname: str) -> None:
        """modification de la propriété host de l'objet
        
        @:param: hostname, le nom du pc
        """
        self._host = hostname

    @property
    def ip(self) -> str:
        """la propriété IP de l'objet"""
        return self._ip

    @ip.setter
    def ip(self, ip: str) -> None:
        """modification de la propriété host de l'objet
        
        @:param: ip, la nouvelle ip
        """
        self._ip = ip
    
    def update(self)->None:
        """
        cette fonction met à jour les données de l'objet
        """
        self._host = socket.gethostname()
        self._ip = socket.gethostbyname(self._host)
        self.space()


# Create an instance of the Info class
info = Info()

# Call the disks method and print the result
disks = info.disks()
print(f"disks: {disks}")

for device, disk_info in disks.items():
    print(f"PREVIOUS")
    print(f"device: {disk_info['device']}")
    print(f"size: {disk_info['size']}")
    print(f"used: {disk_info['used']}")
    print(f"available: {disk_info['available']}")
    print(f"percent: {disk_info['percent']}")
    print(f"mount: {disk_info['mountpoint']}")
    print(f"NEXT")

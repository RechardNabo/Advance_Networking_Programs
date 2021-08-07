import socket


class Port_Service_Names:
    def __init__(self):
        self.ports_list = 65535

    def list(self):
        print("===========================[TCP services]============================")
        for port in range(self.ports_list):
            try:
                print(f"Port {port} >> Service Name: "
                      f"{socket.getservbyport(port, 'tcp')}")
            except OSError:
                pass
        print("==========================[UDP services]==============================")
        for port in range(self.ports_list):
            try:
                print(f"Port {port} Service Name: "f"{socket.getservbyport(port, 'udp')}")
            except OSError:
                pass
        # print(f"Port {port} >> Service Name: Not found")


def main():
    run = Port_Service_Names()
    run.list()


if __name__ == "__main__":
    main()

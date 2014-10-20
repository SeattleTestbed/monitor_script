import sys
import subprocess
import monitor_processes

#pragma out All critical processes on -seattleclearinghouse are up and running

"""
Trying to build dummy lockserver_daemon.py process
in the local machine for unit test
"""
file=open("lockserver_daemon.py","w")
file.write('raw_input("enter something")')
file.close()
proc = subprocess.Popen([sys.executable, 'lockserver_daemon.py'])

monitor_process_list=['python lockserver_daemon.py']
command_list = ["ps auwx | grep python| grep -v grep"]
machine_name = "-seattleclearinghouse"
monitor_processes.monitor_processes(monitor_process_list, command_list, machine_name)

expected_out = "All critical processes on seattleclearinghouse are up and running"

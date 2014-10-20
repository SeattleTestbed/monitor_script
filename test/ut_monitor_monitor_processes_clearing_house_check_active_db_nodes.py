import sys
import subprocess
import monitor_processes

#pragma out All critical processes on -seattleclearinghouse are up and running

"""
Trying to build dummy check_active_db_nodes.py process
in the local machine for unit test
"""
file=open("check_active_db_nodes.py","w")
file.write('raw_input("enter something")')
file.close()
proc = subprocess.Popen([sys.executable, 'check_active_db_nodes.py'])

monitor_process_list=['python check_active_db_nodes.py']
command_list = ["ps auwx | grep python| grep -v grep"]
machine_name = "-seattleclearinghouse"
monitor_processes.monitor_processes(monitor_process_list, command_list, machine_name)

expected_out = "All critical processes on seattleclearinghouse are up and running"

import sys
import os
import subprocess
import monitor_processes
#pragma out All critical processes on -seattle are up and running

advertiseserver_file=open("advertiseserver.py","w")
advertiseserver_file.write('raw_input("enter something")')
advertiseserver_file.close()
os.system('python advertiseserver.py')

monitor_process_list = ['python advertiseserver.py']
command_list =["ps auwx | grep python | grep -v grep"]
machine_name ='-seattle'
monitor_output = monitor_processes.monitor_processes(monitor_process_list, command_list, machine_name)
expected_out = "All critical processes on seattle are up and running"

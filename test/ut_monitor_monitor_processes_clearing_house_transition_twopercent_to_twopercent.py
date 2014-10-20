import sys
import subprocess
import monitor_processes

#pragma out All critical processes on -seattleclearinghouse are up and running

"""
Trying to build dummy transition_twopercent_to_twopercent.py process
in the local machine for unit test
"""
file=open("transition_twopercent_to_twopercent.py","w")
file.write('raw_input("enter something")')
file.close()
proc = subprocess.Popen([sys.executable, 'transition_twopercent_to_twopercent.py'])

monitor_process_list=['python transition_twopercent_to_twopercent.py']
command_list = ["ps auwx | grep python| grep -v grep"]
machine_name = "-seattleclearinghouse"
monitor_processes.monitor_processes(monitor_process_list, command_list, machine_name)

expected_out = "All critical processes on seattleclearinghouse are up and running"

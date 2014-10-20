import sys
import subprocess
import monitor_processes

#pragma out All critical processes on -seattleclearinghouse are up and running

"""
Trying to build dummy transition_donation_to_canonical.py process
in the local machine for unit test
"""

monitor_process_list=['transition_donation_to_canonical.py']
command_list = ["ps auwx | grep python| grep -v grep"]
machine_name = "-seattleclearinghouse"
monitor_processes.monitor_processes(monitor_process_list, command_list, machine_name)

expected_out = "All critical processes on -seattleclearinghouse are up and running"

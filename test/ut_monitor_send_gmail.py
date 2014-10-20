import sys
import subprocess
import send_gmail

#pragma out loaded gmail info 


def main():
  gmail_file_name = "/home/abhishek/monitor_script/seattle_gmail_info"
  result = send_gmail.init_gmail('test21119@gmail.com','testmail')


if __name__ == "__main__":
    main()

# CruiseshIP

**CruiseshIP** is a tool for monitoring your dynamic public IP address so you don't
miss when it changes. It checks for a change each day and emails you if it has changed since the last check. Read about why I built it [here](http://jkjensen.me/).

### Setup

To set up **CruiseshIP**:

1. Clone or download this repository. 
2. Change the `receiver` in _cruiseshIP.py_ to the email you want to receive alerts on.
2. `cd` into the project directory
3. Run `setup.sh`

That's it! CruiseshIP will notify you via email when your public IP address changes.

### Uninstallation

**CruiseshIP** uses cron to handle time-based alerting. To stop these alerts from happening you will need to use crontab to remove the job that runs _cruiseshIP.py_. 

[This tutorial](https://help.1and1.com/hosting-c37630/scripts-and-programming-languages-c85099/cron-jobs-c37727/delete-a-cron-job-a757264.html) explains how to remove a specific cron job.
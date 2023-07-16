from paramiko import SSHClient,AutoAddPolicy
import csv

uname = ""
pword = ""

list_ip_file = open("ip.txt", "r")

with open('report.csv', 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    csv_header = ["IP", "Hostname"]
    writer.writerow(csv_header)

    for ip_with_enter in list_ip_file:
        ip = ip_with_enter.replace("\n", "")

        print (ip)

        try:
            client = SSHClient()
            #client.load_system_host_keys()
            #client.load_host_keys('~/.ssh/known_hosts')
            client.set_missing_host_key_policy(AutoAddPolicy())

            client.connect(ip, username = uname, password = pword)

            stdin, stdout, stderr = client.exec_command('hostname')

            output = stdout.read().decode("utf8").replace("\n", "")
            csv_data = [ip, output]

            writer.writerow(csv_data)

            stdin.close()
            stdout.close()
            stderr.close()
            client.close()
        except:
            csv_data = [ip, ""]
            writer.writerow(csv_data)

    f.close()

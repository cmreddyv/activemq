from functions import *

if not check_root():
    print('You must run ActiveMQ as root')
    exit()

# Disable Local Firewall and SELinux
print('Disabling Local Firewall and SELinux')
disable_local_fw()
disable_local_sel()

url = 'http://www.apache.org/dyn/closer.cgi?filename=/activemq/5.15.10/apache-activemq-5.15.10-bin.tar.gz&action=download'

r = requests.get(url, allow_redirects=True)

open('ActiveMQ.tar.gz', 'wb').write(r.content)

tar = tarfile.open("ActiveMQ.tar.gz", "r:gz")
tar.extractall()
tar.close()

if not os.path.exists("/opt/activemq"):
    copytree('apache-activemq-5.15.10', '/opt/activemq')
#subprocess.run(["/opt/activemq/bin/activemq", "start"])

    with open("service.txt") as f:
        with open("/usr/lib/systemd/system/activemq.service", "w") as f1:
            for line in f:
                f1.write(line)
    subprocess.call(["systemctl","start", "activemq"])

    subprocess.run(["firewall-cmd","--zone=public", "--permanent","--add-port=8161/tcp"])
    subprocess.run(["firewall-cmd","--reload"])
else:
    print("activemq already installed")
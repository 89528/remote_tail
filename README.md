# remote_tail
Remote tail is a tool which works on cli as well as web interface. CLI part is written in bash script and web interface is written in python and use django framework.
**To run remote_tail on cli**
clone repository
cd tail_logs_cli
change username in tail_log.sh
run ssh-keygen -t rsa 
copy public key to the server where you want tail logs.
execute script input IP and path of log file.
Press ctrl+c if you want to pause and then press y to continue tail logs and n to exit script.

**To run remote tail_tail on web interface**
clone repository
cd tail_logs_web
change username in tail_log.py and password if you want password based authentication
For passwordless
run ssh-keygen -t rsa 
copy public key to the server where you want tail logs.
cd remote_tail
execute  python3 manage.py runserver 127.0.0.1:8001
open browser and 127.0.0.1:8001
![image](https://user-images.githubusercontent.com/25869457/125240889-588fe180-e308-11eb-9c00-14700ec20a55.png)
Remote tail_log has many directories and files.
templates directory contains html file which is frontend and calls backend python script.
manage.py,wsgi.py,urls.py,settings.py  is automatically created in each django project.
urls.py is connects html file(fronrend) with backend python script.
The WSGI is a simple calling convention for web servers to forward requests to web applications or frameworks written in the Python

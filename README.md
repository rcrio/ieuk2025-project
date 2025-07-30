# Using the program
1. Install Docker: https://docs.docker.com/get-docker/
2. Open a terminal and navigate to the project folder:
   cd path/to/ieuk2025
You can also just right click inside the ieuk2025 folder and open terminal to be in the same position.
3. Build the Docker image:
   docker build -t ieuk2025 .
4. Run the main script:
   docker run ieuk2025
5. (Optional) Run tests:
   docker run ieuk2025 python test_analyser.py
# Situation
This is a small music media startup and due to their successful podcast and newsletter, it has led to a spike in traffic which has brought a welcome increase in subscriptions. However, there are concerns that the traffic is non-human and the servers are being overwhelmed.
Parts of the website go down every few days due to traffic. The downtime is affecting productivity of the small team of three people.
# Assumptions
We assume that there is an increased traffic from non-humans and the server downtime is being caused by the traffic of requests. In a normal environment, we should make checks to see if this is the case and it isn’t due to other reasons.
# Resources
We have only 3 engineers and it is a small startup, so we should aim for methods that are easier to implement and cheaper.
# Program and statistics
For the program, I have made a python script to parse through the logs folder provided by us and used Pandas to grab the statistics of most requests made by IPs.
Firstly, I looked at the median, mean, and standard deviation.
Mean requests per IP: 10.568
Median requests per IP: 9.0
Standard deviation: 51.26
The standard deviation is very high, and the mean is slightly higher than the median. This indicates there could be some request count heavily skewing the data which could indicate some IPs sending an abnormal amount of requests.

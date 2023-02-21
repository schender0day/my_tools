input_str = """Q: What is the purpose of the AWS X-Ray daemon in the AWS X-Ray SDK?
A: The AWS X-Ray SDK sends trace data to the AWS X-Ray daemon, which collects segments for multiple requests and uploads them in batches to the AWS X-Ray API.

Q: How do you properly instrument applications in Amazon ECS with AWS X-Ray?
A: To properly instrument applications in Amazon ECS with AWS X-Ray, you must create a Docker image that runs the X-Ray daemon, upload it to a Docker image repository, and then deploy it to your Amazon ECS cluster. You can use port mappings and network mode settings in your task definition file to allow your application to communicate with the daemon container.

Q: What is the AWS X-Ray daemon, and how does it work?
A: The AWS X-Ray daemon is a software application that listens for traffic on UDP port 2000, gathers raw segment data, and relays it to the AWS X-Ray API. The daemon works in conjunction with the AWS X-Ray SDKs and must be running so that data sent by the SDKs can reach the X-Ray service."""

output_str = ""

input_list = input_str.split("\n\n")
for i in input_list:
    lines = i.split("\n")
    q = lines[0][3:]
    a = "\n".join(lines[1:])[3:]
    output_str += q + ": " + a + "\n"
print(output_str)
with open('/Users/xinchen/flashcard/review.txt', 'a') as file:
    file.write(output_str)

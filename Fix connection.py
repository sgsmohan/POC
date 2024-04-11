def check_service_status(service_info):
    with open(service_info['logpath'], 'r') as file:
        lines = file.readlines()

    last_keyword_index = None

    for i in range(len(lines) - 1, -1, -1):
        if service_info['keyword'] in lines[i]:
            last_keyword_index = i
            break

    if last_keyword_index is not None:
        for line in lines[last_keyword_index:]:
            if any(error_keyword in line for error_keyword in ["error", "disconnecting", "exception"]):
                return "Service is down"
        return "Service is up"
    else:
        return "Keyword not found"


services = [
    {
        'service_name': 'Service1',
        'logpath': r"C:\WORK\FixConnection\Service1.log",
        'keyword': "Received logon"
    },
    {
        'service_name': 'Service2',
        'logpath': r"C:\WORK\FixConnection\Service2.log",
        'keyword': "Created session"
    },
    # Add more services as needed
]

for service_info in services:
    print(f"Service: {service_info['service_name']}")
    print(check_service_status(service_info))

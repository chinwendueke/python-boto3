import csv

def List_job(jenkins_url,jenkins_user, jenkins_pass):

    import jenkins
    jen_server = jenkins.Jenkins(jenkins_url, username=jenkins_user, password=jenkins_pass)
    #jen_server = jenkins.Jenkins('http://45.33.11.12:8080', username='utrains', password='devops')
    user = jen_server.get_whoami()
    #print(user)
    #print(dir(jen_server))
    jobs = jen_server.get_jobs()

    job_stats = []
    for job in jobs:
        job_name = job['name']
        job_url = job['url']
        job_status = job['color']
        job_stats.append([job_name,job_url,job_status])

    return job_stats

    #print(job['name'], "******", "url:- ", job['url'], "......" "job_status:", job['color']) # To filter data and get what you need
        #print("**************")
List_job('http://45.33.11.12:8080','utrains','devops')
#c=List_job('http://45.33.11.12:8080','utrains','devops')                 #the credentials declared as a variable
#print(c)                                                                 #then call the variable


#if we want to pull the data generated upthere into an excel file, we do the followint below...>
with open("example.txt" , 'a') as f:    #"a" here as in append
    content = "adding data into file\n"
    f.write(content)

with open("example.txt" , 'r') as file:    #"r" here as in read
    cont = file.read()
    print(cont)


#python built-in module csv

data=List_job('http://45.33.11.12:8080','utrains','devops')
with open("jenkins_object.csv", 'w') as j:
    write_row =csv.writer(j)
    write_row.writerow(['JOB_NAME', 'JOB_URL', 'JOB_STATUS'])
    for item in data:
        write_row.writerow(item)
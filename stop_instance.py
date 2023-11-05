#from aws_api import StartInstances,listInstances
import aws_api as a
a.StopInstances(a.listInstances())
from nornir import InitNornir
from nornir_scrapli.tasks import send_command
from nornir_utils.plugins.functions import print_result
from rich import print as rprint
from rich import pretty
from pprint import pprint

#pretty.install()
nr = InitNornir(config_file="config.yaml")

def show_command_test(task):
    task.run(task=send_command, command="show ip interface")

results = nr.run(task=show_command_test)

for device_name, device_data in results.items():
    print(device_name)
    hostNote = device_data[1].scrapli_response.genie_parse_output()
    pprint(hostNote)

    #pprint(host_result.scrapli_response.genie_parse_output())
#print_result(results)
#pprint(results)
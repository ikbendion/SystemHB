# SystemHB
Monitor systemd services and send a heartbeat to a custom endpoint if the service is alive.
## Usage
- install requirements
```
pip3 install -r requirements.txt
```
- edit the configuration (config.yaml)
```yaml
url: "your api endpoint"
service: "your monitored service"
interval: "monitor interval in seconds"
```
- run the script
```
python3 main.py
```
## Dependencies
- Python3
- Modules in requirements.txt
## License
This project is distributed under the GNU GENERAL PUBLIC LICENSE

# Setup
1. Clone repository
```bash
git clone https://github.com/yasirylmzcbn/tamu-registration-monitor.git
```
2. Change directory
```bash
cd tamu-registration-monitor
```
3. Create a virtual environment if on Linux or MacOS
```bash
python3 -m venv venv
```
4. Activate the virtual environment if on Linux or MacOS
```bash
source venv/bin/activate
```
5. Install the required packages
```bash
pip install -r requirements.txt
```
6. Create a `credentials.env` file in the root directory and add the following variables:
```bash
EMAIL=<your_netid_email>
PASSWORD=<your_netid_password>
```
7. Edit the crns dictionary in `main.py` to list the courses and specific section CRNs you want to monitor. It would be easier if I made a UI to select the CRNS but I'm too lazy. Example:
```python
crns = {"POLS 207": ["33048", "45758"], "VIST 386": ["59721"]}
```
8. Run the script
```bash
python main.py
```
# dualityMMR
Duality is a multi-modal rover created for AE 4322: Space System Design II.

To access the raspberry pi:
The computer from which you send commands must be on the same wifi network as the Raspberry PI.

type this command in:
ssh duality@[IP ADDRESS OF PI]

type in this password (it will not show the password, so type it in correctly):
duality2026

from there you open the github directory with this command:
cd dualityMMR

update the current software with this command:

git pull

open the virtual environment with this command:
source venv/bin/activate

now you can run any program for testing, to see a list of all the programs in any directory type this command:
ls

to move up a level in the directory:
cd ..

if you get an error like "some module isnt included" for some reason try this
install -r requirements.txt



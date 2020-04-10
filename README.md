### TKMP.os

# TODO:

### Functions:
	- Recheck functionality
	- Add new commands (MRI, MRW, JNE)
	- Finish unfinished old commands (RMW, RMI, JP, JE, JG, RDW, RDI)
	- Test if commands work with the new functionality (ADD, OUT tested)

### Code:
	- Do a code review
	- Some code must be moved to interrupts.py (insufficient privileges)
	- Fix VM.run_code function for variables that are not used

### Bugs:
	- Pressing enter without inputting any code on console mode 2 crashes the program

### Not implemented:
	- Delete or implement TI and timer (from the code and documentation)
	- Delete or implement paging (from documentation only)
	- Delete or implement IC (from the code and documentation)
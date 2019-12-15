# App Store Connect Library

## Installation
With each python project that you install, it's a good practice to set a virtual environment to avoid cluttering the system with dependencies that your project does not need.
So, in order to install a new environment just type in a console.

`$ python3 -m venv /path/to/new/virtual/environment`

Just upon execution, we must begin using the environment (only if we don't want to install our libraries system-wide). So, depending on the platform we currently are, we execute a different command, as stated in [venv docs](https://docs.python.org/3/library/venv.html#venv-def).

|Platform | Shell           |Command to activate virtual environment|
| ------- | --------------- | ------------------------------------- |
| POSIX   | bash/zsh        | `$ source <venv>/bin/activate`        |
|         | fish            | `$ . <venv>/bin/activate.fish`        |
|         | csh/tcsh        | `$ source <venv>/bin/activate.csh`    |
|         | PowerShell Core | `$ <venv>/bin/Activate.ps1`           |
| Windows | cmd.exe         | `C:\> <venv>\Scripts\activate.bat`    |
|         | PowerShell      | `PS C:\> <venv>\Scripts\Activate.ps1` | 

After that, you should setup the dependencies for the project, just with pip.

`(venv) pip install -r requirements.txt`

Then, we just need the private key to be into the `private_key` directory. It should be a *.p8 file.


## Usage

Finally, we could use the crawler by calling.

`(venv) python3 run.py <requested date>`

We only have to pass the requested date in the format `YYYY-MM-DD`. For example, like `2019-11-20`. 

The return value of this will be `None`, or a tuple with the values `(<requested date>, <number of sales>, <path of the downloaded complete report>)`.
 
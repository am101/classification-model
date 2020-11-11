import sys
import subprocess
subprocess.check_call([sys.executable, '-m', 'pip', 'install',
        'scikit-learn'])
subprocess.check_call([sys.executable, '-m', 'pip', 'install',
            'pandas'])
subprocess.check_call([sys.executable, '-m', 'pip', 'install',
            'matplotlib'])
subprocess.check_call([sys.executable, '-m', 'pip', 'install',
            'jupyter'])

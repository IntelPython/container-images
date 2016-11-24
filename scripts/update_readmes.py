import subprocess

import scripts.images

for dir in scripts.images.list:
    subprocess.check_call('cp docker_repo.README.md %s/README.md' % dir,shell=True)

from invoke import task
import re

@task
def test(c):
    c.run("coverage run -m unittest discover")

@task(test)
def cov(c):
    c.run("coverage report")
    c.run("coverage html")

@task
def setupstream(c, username="amgs"):
    remotes = c.run("git remote", hide=True).stdout
    if "upstream" not in remotes:
        origin_url = c.run("git remote get-url origin", hide=True).stdout.split("\n")[0]
        project_name = re.search(f"\/\/.+\/.+\/(.+?)\.git$", origin_url).group(1)
        c.run(f"git remote add upstream https://github.com/{username}/{project_name}.git")

@task
def sync(c):
    c.run("git fetch upstream")
    c.run("git merge upstream/develop")

@task
def pr(c):
    c.run("hub pr list --format='[%I] %cI %uI %t [%H] | %U%n'")

<<<<<<< HEAD
## Sem task
## Uma vez
# git remote add upstream https://github.com/amgs/aeda_ds.git

## Sempre
# invoke sync
=======
@task
def clean(c):
    c.run("if exist %CD%\dist rmdir /S /Q dist")
    c.run("if exist %CD%\\build rmdir /S /Q build")
    c.run("if exist %CD%\\aed_ds.egg-info rmdir /S /Q aed_ds.egg-info")

@task(clean)
def build(c):
    c.run("python setup.py bdist_wheel")

@task(build)
def install(c):
    c.run("pip uninstall -y aed-ds")
    c.run("pip install --find-links=%cd%\dist aed_ds")

@task
def xclean(c):
    c.run("rm -rf dist/ build/ *.egg-info/")

@task(xclean)
def xbuild(c):
    c.run("pip uninstall -y aed-ds")
    c.run("python setup.py bdist_wheel")

@task(xbuild)
def xinstall(c):
    c.run("pip install --find-links=./dist aed_ds")
>>>>>>> upstream/develop

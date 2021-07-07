from os import system as shell


def publish(commit= "commit"):
    shell('git add .')
    shell(f'git commit -m {commit}')
    shell('git push -u origin master')
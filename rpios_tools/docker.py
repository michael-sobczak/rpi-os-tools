import argparse
from .utils import run


docker_tag = 'rpios-tools/imagebuilder:latest'

def build_docker(version: str, release: str):
    run(
        'docker', 'build', '--no-cache', '-t', docker_tag, '--build-arg', f'VERSION={version}', '--build-arg', f'RELEASE={release}', '.'
    )

def build_wheel():
    run(
        'rm', '-rf', 'dist/'
    )
    run(
        'python', 'setup.py', 'bdist_wheel', '--universal'
    )


def run_docker():
    stdout, stderr = run(
        'docker', 'run', '--privileged', docker_tag
    )
    print(stdout)
    print(stderr)


def main():
    p = argparse.ArgumentParser()
    p.add_argument('version', type=str, help='raspios version')
    p.add_argument('release', type=str, help='raspios release')
    args = p.parse_args()

    print('packaging rpios_tools...')
    build_wheel()
    print('building docker...')
    build_docker(args.version, args.release)
    print('running docker...')
    run_docker()



if __name__ == '__main__':
    main()
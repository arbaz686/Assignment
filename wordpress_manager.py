import os
import subprocess
import argparse
import sys
import webbrowser


def check_dependency_installed(dependency):
    try:
        subprocess.check_output([dependency, '--version'])
        return True
    except OSError:
        return False


def install_dependency(dependency):
    print(f"Installing {dependency}...")
    subprocess.call(['pip', 'install', dependency])


def check_docker_installed():
    return check_dependency_installed('docker')


def check_docker_compose_installed():
    return check_dependency_installed('docker-compose')


def install_docker():
    if not check_docker_installed():
        install_dependency('docker')


def install_docker_compose():
    if not check_docker_compose_installed():
        install_dependency('docker-compose')


def create_wordpress_site(args):
    subprocess.call(['docker-compose', 'up', '-d'])
    open_browser(args.site_name)


def add_hosts_entry(args):
    hosts_entry = '127.0.0.1 ' + args.site_name
    hosts_file_path = '/etc/hosts' if sys.platform != 'win32' else r'C:\Windows\System32\drivers\etc\hosts'

    with open(hosts_file_path, 'a') as hosts_file:
        hosts_file.write(hosts_entry)


def open_browser(site_name):
    webbrowser.open('http://' + site_name)


def enable_disable_site(args):
    command = 'up' if args.enable else 'down'
    subprocess.call(['docker-compose', command])


def delete_site(args):
    subprocess.call(['docker-compose', 'down', '-v'])
    site_name = input("Enter the site name to delete: ")
    if sys.platform != 'win32':
        subprocess.call(['sed', '-i', f'"/{site_name}/d"', '/etc/hosts'])
    else:
        with open(r'C:\Windows\System32\drivers\etc\hosts', 'r') as hosts_file:
            lines = hosts_file.readlines()
        with open(r'C:\Windows\System32\drivers\etc\hosts', 'w') as hosts_file:
            for line in lines:
                if site_name not in line:
                    hosts_file.write(line)


def main():
    parser = argparse.ArgumentParser(description='WordPress site management script')
    parser.add_argument('site_name', help='Name of the WordPress site')
    subparsers = parser.add_subparsers(dest='subcommand', help='Subcommands')

    parser_create = subparsers.add_parser('create', help='Create a WordPress site')
    parser_create.set_defaults(func=create_wordpress_site)

    parser_enable_disable = subparsers.add_parser('enable_disable', help='Enable/Disable a WordPress site')
    group = parser_enable_disable.add_mutually_exclusive_group(required=True)
    group.add_argument('--enable', action='store_true', help='Enable the site')
    group.add_argument('--disable', action='store_true', help='Disable the site')
    parser_enable_disable.set_defaults(func=enable_disable_site)

    parser_delete = subparsers.add_parser('delete', help='Delete a WordPress site')
    parser_delete.set_defaults(func=delete_site)

    args = parser.parse_args()

    if args.subcommand == 'create':
        install_docker()
        install_docker_compose()
        add_hosts_entry(args)

    args.func(args)


if __name__ == '__main__':
    main()

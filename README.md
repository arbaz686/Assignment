# WordPress Site Management Script

This script allows you to manage WordPress sites using the command line interface.

## Installation

1. Clone the repository:

   `git clone <repository_url>`

2. Install the required dependencies:

   `pip install -r requirements.txt`

   **Note:** Make sure you have Python and pip installed on your system.

3. Set up Docker and Docker Compose:

   - Install Docker by following the instructions at [https://docs.docker.com/get-docker/](https://docs.docker.com/get-docker/).
   - Install Docker Compose by following the instructions at [https://docs.docker.com/compose/install/](https://docs.docker.com/compose/install/).

## Usage

`python wordpress_manager.py <site_name> <command> [options]`

Replace `<site_name>` with the name of your WordPress site.

### Commands

- `create`: Create a new WordPress site.

  `python wordpress_manager.py <site_name> create`

  This command will install and set up a new WordPress site using Docker and Docker Compose. It will create the necessary containers and start the services.

- `enable_disable`: Enable or disable a WordPress site.

  `python wordpress_manager.py <site_name> enable_disable [--enable | --disable]`

  Use the `--enable` option to enable the site, or use the `--disable` option to disable the site. This command will start or stop the services for the specified WordPress site.

- `delete`: Delete a WordPress site.

  python wordpress_manager.py <site_name> delete

  This command will remove the WordPress site, including all associated containers and volumes. You will be prompted to enter the site name to confirm the deletion.

**Note:** The `create` command requires Docker and Docker Compose to be installed and configured properly on your system.

## Examples

1. Create a new WordPress site named "myblog":

   `python wordpress_manager.py myblog creat`

   This command will set up a new WordPress site named "myblog" using Docker and Docker Compose.

2. Enable the "myblog" site:

   `python wordpress_manager.py myblog enable_disable --enable`

   This command will start the services for the "myblog" WordPress site.

3. Disable the "myblog" site:

   `python wordpress_manager.py myblog enable_disable --disable`

   This command will stop the services for the "myblog" WordPress site.

4. Delete the "myblog" site:

   `python wordpress_manager.py myblog delete`

   This command will remove the "myblog" WordPress site, including all associated containers and volumes.

import click
import shutil
import pkg_resources
import os
from pathlib import Path

@click.group()
def cli():
    """Flask API Starter CLI"""
    pass

@cli.command()
@click.argument("project_name")
def new(project_name):
    """Generate a new Flask API project from bundled template."""
    # resource_filename works with packages installed as wheels or source
    try:
        template_path = pkg_resources.resource_filename("flask_api_starter", "template")
    except Exception:
        # fallback: relative path while in development
        template_path = os.path.join(os.path.dirname(__file__), "template")

    dest = Path.cwd() / project_name
    if dest.exists():
        click.echo(f"Destination {dest} already exists. Aborting.")
        return

    shutil.copytree(template_path, dest)
    click.echo(f"Project created at ./{project_name}")
    click.echo("Next steps:")
    click.echo(f"  cd {project_name}")
    click.echo("  pip install -r requirements.txt")
    click.echo("  python run.py")

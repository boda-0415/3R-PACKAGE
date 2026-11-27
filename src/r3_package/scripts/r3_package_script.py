"""CLI script for the 3R-PACKAGE package."""

import click

from r3_package.r3_package import calculate_mean, hello_world


@click.command()
@click.option("--message", help="Type a message to say")
@click.option("--mean", help="Comma-separated numbers to calculate mean")
@click.version_option()
def r3_package_cli(message, mean):
    """Example script. This function is referenced in setup.cfg."""
    if mean is not None:
        try:
            numbers = [float(x.strip()) for x in mean.split(",")]
            result = calculate_mean(numbers)
            click.echo(f"Mean: {result}")
        except ValueError as exc:
            raise click.BadParameter(
                "Please enter valid comma-separated numbers.",
                param_hint="--mean",
            ) from exc
    else:
        if message is None:
            message = click.prompt("message")
        click.echo(hello_world(message))

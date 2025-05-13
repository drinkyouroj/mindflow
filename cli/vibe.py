#!/usr/bin/env python3
import click

PRESETS = {
    "focused": {
        "silenced_notifications": True,
        "pomodoro_enabled": True,
        "audio_cues": True,
    },
    "calm": {
        "silenced_notifications": True,
        "pomodoro_enabled": False,
        "audio_cues": False,
    },
}

@click.command()
@click.argument('preset', type=click.Choice(list(PRESETS.keys()), case_sensitive=False))
def vibe(preset):
    """
    Apply a vibe preset (focused or calm).
    """
    cfg = PRESETS[preset.lower()]
    click.echo(f"Applying '{preset}' preset:")
    click.echo(f" - Silenced Notifications: {'On' if cfg['silenced_notifications'] else 'Off'}")
    click.echo(f" - Pomodoro Enabled: {'On' if cfg['pomodoro_enabled'] else 'Off'}")
    click.echo(f" - Audio Cues: {'On' if cfg['audio_cues'] else 'Off'}")
    # TODO: integrate with system modules to apply these settings

if __name__ == '__main__':
    vibe()

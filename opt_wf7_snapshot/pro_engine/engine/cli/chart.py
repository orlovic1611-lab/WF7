from __future__ import annotations

import click
import pandas as pd
from pathlib import Path

from wf.cli.config import load_config
from wf.core.events import EventStore
from wf.utils.yamlio import read_yaml


@click.command()
@click.option("--audit", required=True, help="Audit JSON file")
@click.option("--out", default="outputs/charts/events.png", help="Output chart")
def chart(audit: str, out: str) -> None:
    """Generate event charts."""
    store = EventStore()
    
    # Load audit
    data = read_yaml(audit)
    for entry in data:
        store.add(Event(**entry))
    
    df = pd.DataFrame([{
        "timestamp": pd.to_datetime(e.timestamp),
        "kind": e.kind,
        "severity": e.severity
    } for e in store.events])
    
    # Event types pie chart
    fig, axes = plt.subplots(1, 2, figsize=(12, 5))
    
    df["kind"].value_counts().plot.pie(autopct="%1.1f%%", ax=axes[0])
    axes[0].set_title("Events by Kind")
    
    df["severity"].value_counts().plot.bar(ax=axes[1])
    axes[1].set_title("Events by Severity")
    
    plt.tight_layout()
    Path(out).parent.mkdir(parents=True, exist_ok=True)
    plt.savefig(out, dpi=300, bbox_inches="tight")
    print(f"✓ Chart saved: {out}")

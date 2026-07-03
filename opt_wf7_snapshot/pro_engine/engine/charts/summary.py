from __future__ import annotations

from pathlib import Path

import pandas as pd
import plotly.express as px


def chart_summary(csv_path: str | Path, output_path: str | Path) -> Path:
    """
    Create a simple operational chart from a CSV summary.

    The first chart should be simple and readable: a bar chart makes patterns
    visible quickly without hiding the underlying counts behind overdesign.
    """
    df = pd.read_csv(csv_path)
    fig = px.bar(df, x=df.columns[0], y=df.columns[1], title="WF Event Summary")
    out = Path(output_path)
    out.parent.mkdir(parents=True, exist_ok=True)
    fig.write_html(out)
    return out

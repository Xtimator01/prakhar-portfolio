
import plotly.graph_objects as go
from plotly.offline import plot


def create_stock_chart():

    dates = [
        "01 Nov", "05 Nov", "10 Nov", "15 Nov",
        "20 Nov", "25 Nov", "30 Nov"
    ]

    prices = [2450, 2510, 2480, 2590, 2550, 2670, 2720]

    fig = go.Figure()

    fig.add_trace(go.Scatter(
        x=dates,
        y=prices,
        mode="lines+markers",
        name="Stock Price",
        line=dict(color="#65a8ff", width=3),
        marker=dict(size=7)
    ))

    fig.update_layout(
        title="Stock Price Analysis",
        xaxis_title="Date",
        yaxis_title="Price (₹)",
        template="plotly_dark",
        paper_bgcolor="#111827",
        plot_bgcolor="#111827",
        font=dict(color="#ffffff"),
        margin=dict(l=50, r=30, t=60, b=50),
        height=400
    )

    chart = plot(
        fig,
        output_type="div",
        include_plotlyjs="cdn",
        config={"responsive": True}
    )

    return chart

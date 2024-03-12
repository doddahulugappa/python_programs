import pandas as pd


def color_failed(value):
    if value.startswith("A"):
        color = "red"
    else:
        color = "green"

    return f'<div style="color: {color}">{value}</div>'


data = {
    "one": ["Abhi", "Shek"],
    "two": ["Arjun", "Echo"],
    "three": ["Virat", "Gandalf"],
    "four": ["Emma", "Amma"]
}

df = pd.DataFrame(data)

print(df.to_html(formatters=[color_failed, color_failed, color_failed, color_failed], escape=False))

# --- show in web browser ---

df.to_html('index.html', formatters=[color_failed, color_failed, color_failed, color_failed], escape=False, index=False)

import webbrowser

webbrowser.open('index.html')

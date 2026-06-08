# Market Share Pie Chart Generator

## Project Overview

The **Market Share Pie Chart Generator** is a Python-based data visualization project that creates a presentation-ready pie chart showing the market share distribution of different smartphone companies.

This project demonstrates the use of **Matplotlib** for business data visualization and helps users understand how market share is distributed among competitors in a market.

## Objective

To visualize competitor market share data using a pie chart and present it in a professional and easy-to-understand format.

## Features

* Displays market share percentages for multiple companies.
* Uses a professional color palette for better presentation.
* Highlights the market leader using the explode effect.
* Shows percentage values directly on chart slices.
* Includes a title and legend for better readability.
* Saves the chart as an image file (`market_share.png`).

## Technologies Used

* Python 3
* Matplotlib

## Dataset

The project uses sample smartphone market share data:

| Company | Market Share (%) |
| ------- | ---------------- |
| Apple   | 28.4             |
| Samsung | 21.6             |
| Xiaomi  | 12.5             |
| Oppo    | 10.2             |
| Vivo    | 8.9              |
| Others  | 18.4             |

## Code Explanation

### 1. Import Library

```python
import matplotlib.pyplot as plt
```

### 2. Define Data

```python
companies = ['Apple', 'Samsung', 'Xiaomi', 'Oppo', 'Vivo', 'Others']
market_share = [28.4, 21.6, 12.5, 10.2, 8.9, 18.4]
```

### 3. Create Custom Colors

```python
colors = ['#FF6B6B', '#4ECDC4', '#45B7D1', '#96CEB4', '#FFEAA7', '#DDA0DD']
```

### 4. Highlight Market Leader

```python
explode = (0.05, 0, 0, 0, 0, 0)
```

### 5. Generate Pie Chart

```python
fig, ax = plt.subplots(figsize=(9, 6))

wedges, texts, autotexts = ax.pie(
    market_share,
    labels=companies,
    colors=colors,
    explode=explode,
    autopct='%1.1f%%',
    startangle=140,
    pctdistance=0.82,
    shadow=True
)
```

### 6. Customize Appearance

```python
for text in texts:
    text.set_fontsize(11)

for autotext in autotexts:
    autotext.set_fontsize(9)
    autotext.set_color('white')
    autotext.set_fontweight('bold')
```

### 7. Add Title and Legend

```python
ax.set_title(
    'Global Smartphone Market Share - 2024',
    fontsize=15,
    fontweight='bold',
    pad=20
)

ax.legend(
    wedges,
    companies,
    title="Companies",
    loc="center left",
    bbox_to_anchor=(1, 0, 0.5, 1)
)
```

### 8. Save Chart

```python
plt.tight_layout()
plt.savefig('market_share.png', dpi=150, bbox_inches='tight')
plt.show()
```

## Output

The program generates a pie chart displaying the market share distribution of smartphone companies and saves it as:

```text
market_share.png
```

## Learning Outcomes

After completing this project, you will be able to:

* Understand business data visualization concepts.
* Create pie charts using Matplotlib.
* Customize chart appearance with colors and labels.
* Highlight important data points using explode effects.
* Save visualizations as image files.
* Present market share information professionally.

## Future Enhancements

* Read data from CSV or Excel files.
* Add interactive charts using Plotly.
* Compare market share across multiple years.
* Create automated business reports.

## Author

RESHMA PRADHAN
NOOR SABA 
NAITIK KUMAR

## License

This project is created for educational and learning purposes.

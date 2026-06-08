import matplotlib.pyplot as plt

# --- DATA ---
companies = ['Apple', 'Samsung', 'Xiaomi', 'Oppo', 'Vivo', 'Others','Naitik chodu']
market_share = [28.4, 21.6, 12.5, 10.2, 8.9, 18.4]  # in percentages

# --- COLORS (presentation-ready palette) ---
colors = ['#FF6B6B', '#4ECDC4', '#45B7D1', '#96CEB4', '#FFEAA7', '#DDA0DD']

# --- EXPLODE (highlight top player) ---
explode = (0.05, 0, 0, 0, 0, 0)  # slightly pull out Apple slice

# --- PLOT ---
fig, ax = plt.subplots(figsize=(9, 6))

wedges, texts, autotexts = ax.pie(
    market_share,
    labels=companies,
    colors=colors,
    explode=explode,
    autopct='%1.1f%%',       # show % on each slice
    startangle=140,           # rotate for better visual
    pctdistance=0.82,
    shadow=True
)

# --- STYLING ---
for text in texts:
    text.set_fontsize(11)
for autotext in autotexts:
    autotext.set_fontsize(9)
    autotext.set_color('white')
    autotext.set_fontweight('bold')

# --- TITLE & LEGEND ---
ax.set_title('Global Smartphone Market Share - 2024', fontsize=15, fontweight='bold', pad=20)
ax.legend(wedges, companies, title="Companies", loc="center left", bbox_to_anchor=(1, 0, 0.5, 1))

plt.tight_layout()
plt.savefig('market_share.png', dpi=150, bbox_inches='tight')  # save as image
plt.show()
print("Chart saved as market_share.png")
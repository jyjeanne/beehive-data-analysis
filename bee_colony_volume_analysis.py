#!/usr/bin/env python3
"""
Bee Colony Volume and Mass Analysis
Calculate and visualize the physical dimensions of bee colonies throughout the year

Author: Bee Hive Analysis Project
Date: November 13, 2025
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path

# Set style
sns.set_style("whitegrid")
plt.rcParams['figure.figsize'] = (15, 12)
plt.rcParams['font.size'] = 10

# ============================================================================
# Constants
# ============================================================================

BEE_VOLUME_CM3 = 0.125  # cm³ per bee (middle range: 0.1-0.15)
BEE_VOLUME_MM3 = 125    # mm³ per bee
BEE_MASS_G = 0.1        # grams per bee
BEE_DENSITY = 1.0       # g/cm³ (approximately water density)

# ============================================================================
# Data
# ============================================================================

# Load bee population data
data_path = Path("data/bee_population_year.csv")
df_pop = pd.read_csv(data_path)

print("=" * 80)
print("BEE COLONY VOLUME AND MASS ANALYSIS")
print("=" * 80)
print(f"\nData loaded from: {data_path}")
print(f"Months analyzed: {len(df_pop)}")
print(f"\nBelativity Assumptions:")
print(f"  - Volume per bee: {BEE_VOLUME_CM3} cm³ ({BEE_VOLUME_MM3} mm³)")
print(f"  - Mass per bee: {BEE_MASS_G} g (100 mg)")
print(f"  - Bee density: {BEE_DENSITY} g/cm³")

# ============================================================================
# Calculations
# ============================================================================

# Calculate volume and mass
df_pop['Volume_cm3'] = df_pop['Bee_Population'] * BEE_VOLUME_CM3
df_pop['Volume_L'] = df_pop['Volume_cm3'] / 1000
df_pop['Mass_g'] = df_pop['Bee_Population'] * BEE_MASS_G
df_pop['Mass_kg'] = df_pop['Mass_g'] / 1000

# Calculate variations
df_pop['Volume_variation_%'] = (df_pop['Volume_L'] / df_pop['Volume_L'].mean() - 1) * 100
df_pop['Population_variation_%'] = (df_pop['Bee_Population'] / df_pop['Bee_Population'].mean() - 1) * 100
df_pop['Month_num'] = range(1, len(df_pop) + 1)

# Calculate frames needed (9 liters per frame)
LITERS_PER_FRAME = 9
df_pop['Frames_needed'] = df_pop['Volume_L'] / LITERS_PER_FRAME

print("\n" + "=" * 80)
print("MONTHLY COLONY VOLUME AND MASS")
print("=" * 80)
print(df_pop[['Month', 'Bee_Population', 'Volume_L', 'Mass_kg', 'Frames_needed']].to_string(index=False))

# ============================================================================
# Statistics
# ============================================================================

print("\n" + "=" * 80)
print("SUMMARY STATISTICS")
print("=" * 80)

print(f"\nPOPULATION:")
print(f"  Minimum: {df_pop['Bee_Population'].min():,} bees ({df_pop.loc[df_pop['Bee_Population'].idxmin(), 'Month']})")
print(f"  Maximum: {df_pop['Bee_Population'].max():,} bees ({df_pop.loc[df_pop['Bee_Population'].idxmax(), 'Month']})")
print(f"  Average: {df_pop['Bee_Population'].mean():,.0f} bees")
print(f"  Variation: {df_pop['Bee_Population'].max() / df_pop['Bee_Population'].min():.2f}x")

print(f"\nVOLUME:")
print(f"  Minimum: {df_pop['Volume_L'].min():.3f} L ({df_pop.loc[df_pop['Volume_L'].idxmin(), 'Month']})")
print(f"  Maximum: {df_pop['Volume_L'].max():.3f} L ({df_pop.loc[df_pop['Volume_L'].idxmax(), 'Month']})")
print(f"  Average: {df_pop['Volume_L'].mean():.3f} L")
print(f"  Variation: {df_pop['Volume_L'].max() / df_pop['Volume_L'].min():.2f}x")

print(f"\nMASS:")
print(f"  Minimum: {df_pop['Mass_kg'].min():.3f} kg ({df_pop.loc[df_pop['Mass_kg'].idxmin(), 'Month']})")
print(f"  Maximum: {df_pop['Mass_kg'].max():.3f} kg ({df_pop.loc[df_pop['Mass_kg'].idxmax(), 'Month']})")
print(f"  Average: {df_pop['Mass_kg'].mean():.3f} kg")
print(f"  Total annual: {df_pop['Mass_kg'].sum():.2f} kg")
print(f"  Variation: {df_pop['Mass_kg'].max() / df_pop['Mass_kg'].min():.2f}x")

print(f"\nFRAMES NEEDED (9 L per frame):")
print(f"  Minimum: {df_pop['Frames_needed'].min():.2f} frames")
print(f"  Maximum: {df_pop['Frames_needed'].max():.2f} frames")
print(f"  Average: {df_pop['Frames_needed'].mean():.2f} frames")

# ============================================================================
# Seasonal Analysis
# ============================================================================

print("\n" + "=" * 80)
print("SEASONAL ANALYSIS")
print("=" * 80)

seasons = {
    'Winter (Hivernage)': [0, 1, 10, 11],          # Jan, Feb, Nov, Dec
    'Spring (Développement)': [2, 3],              # Mar, Apr
    'Summer (Essaimage)': [4, 5, 6],               # May, Jun, Jul
    'Fall (Préparation)': [7, 8, 9]                # Aug, Sep, Oct
}

for season_name, indices in seasons.items():
    season_data = df_pop.iloc[indices]
    print(f"\n{season_name}:")
    print(f"  Months: {', '.join(season_data['Month'].values)}")
    print(f"  Avg Population: {season_data['Bee_Population'].mean():,.0f}")
    print(f"  Avg Volume: {season_data['Volume_L'].mean():.3f} L")
    print(f"  Avg Mass: {season_data['Mass_kg'].mean():.3f} kg")
    print(f"  % of maximum: {season_data['Volume_L'].mean() / df_pop['Volume_L'].max() * 100:.1f}%")

# ============================================================================
# Create Visualizations
# ============================================================================

fig = plt.figure(figsize=(16, 14))

# 1. Population and Volume
ax1 = plt.subplot(3, 3, 1)
ax1_twin = ax1.twinx()
ax1.bar(df_pop['Month_num'], df_pop['Bee_Population'], alpha=0.6, color='blue', label='Population')
ax1_twin.plot(df_pop['Month_num'], df_pop['Volume_L'], color='red', marker='o', linewidth=2, markersize=8, label='Volume')
ax1.set_xlabel('Month')
ax1.set_ylabel('Population (bees)', color='blue')
ax1_twin.set_ylabel('Volume (L)', color='red')
ax1.set_title('Colony Population and Volume by Month')
ax1.set_xticks(range(1, 13))
ax1.set_xticklabels([m[:3] for m in df_pop['Month']], rotation=45)
ax1.grid(True, alpha=0.3)
ax1.tick_params(axis='y', labelcolor='blue')
ax1_twin.tick_params(axis='y', labelcolor='red')

# 2. Volume by Month
ax2 = plt.subplot(3, 3, 2)
colors = ['#4169E1' if i in [0,1,10,11] else '#FF6347' if i in [2,3] else '#FFD700' if i in [4,5,6] else '#FFA500'
          for i in range(len(df_pop))]
ax2.bar(df_pop['Month'], df_pop['Volume_L'], color=colors, alpha=0.7)
ax2.axhline(y=df_pop['Volume_L'].mean(), color='black', linestyle='--', linewidth=2, label='Annual Average')
ax2.set_ylabel('Volume (Liters)')
ax2.set_title('Colony Volume by Month')
ax2.set_xticklabels(df_pop['Month'], rotation=45, ha='right')
ax2.legend()
ax2.grid(True, alpha=0.3, axis='y')

# 3. Mass by Month
ax3 = plt.subplot(3, 3, 3)
ax3.bar(df_pop['Month'], df_pop['Mass_kg'], color='brown', alpha=0.7)
ax3.axhline(y=df_pop['Mass_kg'].mean(), color='black', linestyle='--', linewidth=2, label='Annual Average')
ax3.set_ylabel('Mass (kg)')
ax3.set_title('Colony Mass by Month')
ax3.set_xticklabels(df_pop['Month'], rotation=45, ha='right')
ax3.legend()
ax3.grid(True, alpha=0.3, axis='y')

# 4. Volume Variation
ax4 = plt.subplot(3, 3, 4)
colors_var = ['green' if x > 0 else 'red' for x in df_pop['Volume_variation_%']]
ax4.bar(df_pop['Month'], df_pop['Volume_variation_%'], color=colors_var, alpha=0.7)
ax4.axhline(y=0, color='black', linewidth=1)
ax4.set_ylabel('Variation from Average (%)')
ax4.set_title('Volume Variation from Annual Average')
ax4.set_xticklabels(df_pop['Month'], rotation=45, ha='right')
ax4.grid(True, alpha=0.3, axis='y')

# 5. Monthly Change in Volume
ax5 = plt.subplot(3, 3, 5)
volume_change = df_pop['Volume_L'].diff()
colors_change = ['green' if x > 0 else 'red' for x in volume_change]
ax5.bar(df_pop['Month'][1:], volume_change[1:], color=colors_change[1:], alpha=0.7)
ax5.axhline(y=0, color='black', linewidth=1)
ax5.set_ylabel('Volume Change (L)')
ax5.set_title('Monthly Volume Change')
ax5.set_xticklabels(df_pop['Month'][1:], rotation=45, ha='right')
ax5.grid(True, alpha=0.3, axis='y')

# 6. Volume-Mass Relationship
ax6 = plt.subplot(3, 3, 6)
scatter = ax6.scatter(df_pop['Volume_L'], df_pop['Mass_kg'], s=100, c=range(len(df_pop)), cmap='viridis', alpha=0.6)
ax6.set_xlabel('Volume (L)')
ax6.set_ylabel('Mass (kg)')
ax6.set_title('Volume vs Mass Relationship')
plt.colorbar(scatter, ax=ax6, label='Month')
for i, txt in enumerate(df_pop['Month'].str[:3]):
    ax6.annotate(txt, (df_pop['Volume_L'].iloc[i], df_pop['Mass_kg'].iloc[i]), fontsize=8)
ax6.grid(True, alpha=0.3)

# 7. Frames Needed
ax7 = plt.subplot(3, 3, 7)
ax7.plot(df_pop['Month_num'], df_pop['Frames_needed'], marker='o', linewidth=2, markersize=8, color='darkgreen')
ax7.axhline(y=10, color='red', linestyle='--', linewidth=2, label='10-frame Langstroth')
ax7.axhline(y=8, color='orange', linestyle='--', linewidth=2, label='8-frame Langstroth')
ax7.fill_between(df_pop['Month_num'], 0, df_pop['Frames_needed'], alpha=0.3, color='green')
ax7.set_xlabel('Month')
ax7.set_ylabel('Frames Needed')
ax7.set_title('Frames Needed by Month')
ax7.set_xticks(range(1, 13))
ax7.set_xticklabels([m[:3] for m in df_pop['Month']], rotation=45)
ax7.legend()
ax7.grid(True, alpha=0.3)

# 8. Seasonal Comparison - Volume
ax8 = plt.subplot(3, 3, 8)
season_volumes = []
season_names_short = ['Winter', 'Spring', 'Summer', 'Fall']
for season_name, indices in seasons.items():
    season_volumes.append(df_pop.iloc[indices]['Volume_L'].mean())
bars = ax8.bar(season_names_short, season_volumes, color=['#4169E1', '#228B22', '#FFD700', '#FF8C00'], alpha=0.7)
ax8.set_ylabel('Average Volume (L)')
ax8.set_title('Average Volume by Season')
ax8.grid(True, alpha=0.3, axis='y')
# Add value labels on bars
for bar in bars:
    height = bar.get_height()
    ax8.text(bar.get_x() + bar.get_width()/2., height,
             f'{height:.2f}L', ha='center', va='bottom', fontsize=10, fontweight='bold')

# 9. Growth/Decline Rates
ax9 = plt.subplot(3, 3, 9)
monthly_growth = (df_pop['Volume_L'].pct_change() * 100).fillna(0)
colors_growth = ['green' if x > 0 else 'red' for x in monthly_growth]
ax9.bar(df_pop['Month'], monthly_growth, color=colors_growth, alpha=0.7)
ax9.axhline(y=0, color='black', linewidth=1)
ax9.set_ylabel('Growth Rate (%)')
ax9.set_title('Monthly Volume Growth/Decline Rate')
ax9.set_xticklabels(df_pop['Month'], rotation=45, ha='right')
ax9.grid(True, alpha=0.3, axis='y')

plt.tight_layout()
plt.savefig('bee_colony_volume_mass_analysis.png', dpi=150, bbox_inches='tight')
print("\n[OK] Visualization saved as: bee_colony_volume_mass_analysis.png")
plt.close()

# ============================================================================
# Additional Analysis
# ============================================================================

print("\n" + "=" * 80)
print("HIVE DESIGN IMPLICATIONS")
print("=" * 80)

min_volume = df_pop['Volume_L'].min()
max_volume = df_pop['Volume_L'].max()
avg_volume = df_pop['Volume_L'].mean()

print(f"\nMinimum colony volume needed: {min_volume:.3f} L (for winter survival)")
print(f"Maximum colony volume reached: {max_volume:.3f} L (summer peak)")
print(f"Average volume: {avg_volume:.3f} L")

print(f"\nRecommended hive volumes:")
print(f"  Minimum: 15 L (2× winter volume for honey storage)")
print(f"  Optimal: 40-45 L (accommodates all seasons)")
print(f"  Maximum: 60+ L (if maximum expansion needed)")

print(f"\nStorage volume needed:")
storage_winter = 4.5  # liters
storage_summer = 30   # liters
print(f"  Winter: ~{storage_winter} L (honey reserves)")
print(f"  Summer: ~{storage_summer} L (honey + pollen)")

print(f"\nTotal hive utilization:")
print(f"  Winter: {min_volume + storage_winter:.1f} L of 45 L hive = {(min_volume + storage_winter) / 45 * 100:.0f}%")
print(f"  Summer: {max_volume + storage_summer:.1f} L of 45 L hive = {(max_volume + storage_summer) / 45 * 100:.0f}%")

# ============================================================================
# Export Data
# ============================================================================

print("\n" + "=" * 80)
print("EXPORT DATA")
print("=" * 80)

export_df = df_pop[['Month', 'Bee_Population', 'Colony_Phase', 'Volume_L', 'Mass_kg', 'Frames_needed']].copy()
export_df.to_csv('bee_colony_volume_analysis.csv', index=False)
print("[OK] Data exported to: bee_colony_volume_analysis.csv")

print("\n" + "=" * 80)
print("ANALYSIS COMPLETE")
print("=" * 80)

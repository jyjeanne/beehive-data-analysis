# Bee Colony Volume and Mass Analysis
## Annual Variation in Colony Size

**Date**: November 13, 2025
**Analysis**: Physical dimensions of bee colonies throughout the year

---

## 📊 Physical Parameters of a Single Bee

### Dimensions
- **Body length**: 12-15 mm
- **Body width**: ~3-4 mm
- **Volume per bee**: 0.1-0.15 cm³ (100-150 mm³)
- **Mass per bee**: ~0.1 grams (100 mg)

### Density Calculation
```
Bee density = Mass / Volume
            = 0.1 g / 0.1 cm³
            = 1.0 g/cm³
(This is approximately the density of water, which makes sense for soft-bodied insects)
```

---

## 🐝 Colony Population Data

Based on `bee_population_year.csv`, monthly population varies:

| Month | Population | Phase | Season |
|-------|-----------|-------|--------|
| January | 9,000 | Hivernage | Winter |
| February | 9,500 | Hivernage | Winter |
| March | 11,500 | Développement | Spring |
| April | 24,000 | Développement | Spring |
| May | 58,000 | Essaimage | Summer |
| June | 58,000 | Essaimage | Summer |
| July | 48,000 | Essaimage | Summer |
| August | 28,000 | Préparation | Fall |
| September | 23,000 | Préparation | Fall |
| October | 19,000 | Préparation | Fall |
| November | 17,000 | Hivernage | Winter |
| December | 13,500 | Hivernage | Winter |

---

## 📐 Volume Calculations

### Formula for Colony Volume

```
V_colony = Population × V_per_bee
```

Where:
- V_colony = Total volume occupied by colony (cm³ or liters)
- Population = Number of bees in colony
- V_per_bee = Volume per individual bee (0.1-0.15 cm³)

### Monthly Colony Volumes

Using V_per_bee = 0.125 cm³ (middle value of 0.1-0.15):

| Month | Population | Volume (cm³) | Volume (Liters) | Volume (mm³) |
|-------|-----------|------------|---------------|-----------:|
| January | 9,000 | 1,125 | 1.125 | 1,125,000 |
| February | 9,500 | 1,188 | 1.188 | 1,187,500 |
| March | 11,500 | 1,438 | 1.438 | 1,437,500 |
| April | 24,000 | 3,000 | 3.000 | 3,000,000 |
| May | 58,000 | 7,250 | 7.250 | 7,250,000 |
| June | 58,000 | 7,250 | 7.250 | 7,250,000 |
| July | 48,000 | 6,000 | 6.000 | 6,000,000 |
| August | 28,000 | 3,500 | 3.500 | 3,500,000 |
| September | 23,000 | 2,875 | 2.875 | 2,875,000 |
| October | 19,000 | 2,375 | 2.375 | 2,375,000 |
| November | 17,000 | 2,125 | 2.125 | 2,125,000 |
| December | 13,500 | 1,688 | 1.688 | 1,687,500 |

**Summary**:
- Minimum volume: 1.125 liters (January)
- Maximum volume: 7.250 liters (May-June)
- Variation: 6.125 liters (6.4x difference)
- Average volume: 3.515 liters

---

## ⚖️ Mass Calculations

### Formula for Colony Mass

```
M_colony = Population × M_per_bee
```

Where:
- M_colony = Total mass of colony (grams)
- Population = Number of bees in colony
- M_per_bee = Mass per individual bee (0.1 grams)

### Monthly Colony Mass

| Month | Population | Mass (g) | Mass (kg) | Variation |
|-------|-----------|---------|----------|-----------|
| January | 9,000 | 900 | 0.900 | -39% |
| February | 9,500 | 950 | 0.950 | -37% |
| March | 11,500 | 1,150 | 1.150 | -30% |
| April | 24,000 | 2,400 | 2.400 | +23% |
| May | 58,000 | 5,800 | 5.800 | +188% |
| June | 58,000 | 5,800 | 5.800 | +188% |
| July | 48,000 | 4,800 | 4.800 | +135% |
| August | 28,000 | 2,800 | 2.800 | +44% |
| September | 23,000 | 2,300 | 2.300 | +18% |
| October | 19,000 | 1,900 | 1.900 | -2% |
| November | 17,000 | 1,700 | 1.700 | -13% |
| December | 13,500 | 1,350 | 1.350 | -31% |

**Summary**:
- Minimum mass: 0.900 kg (January)
- Maximum mass: 5.800 kg (May-June)
- Variation: 4.900 kg (6.4x difference)
- Average mass: 2.804 kg
- Total annual mass requirement: 33.65 kg

---

## 📈 Annual Variation Analysis

### Seasonal Patterns

#### Winter (Hivernage): January, February, November, December
- **Average population**: 12,250 bees
- **Average volume**: 1.531 liters
- **Average mass**: 1.225 kg
- **Characteristics**: Minimal population for survival, compact cluster
- **Percentage of max**: 19% volume, 21% mass

#### Spring (Développement): March, April
- **Average population**: 17,750 bees
- **Average volume**: 2.219 liters
- **Average mass**: 1.775 kg
- **Characteristics**: Rapid growth phase, expanding colony
- **Percentage of max**: 31% volume, 31% mass

#### Summer (Essaimage): May, June, July
- **Average population**: 54,667 bees
- **Average volume**: 6.833 liters
- **Average mass**: 5.467 kg
- **Characteristics**: Peak population for swarming and reproduction
- **Percentage of max**: 94% volume, 94% mass

#### Fall (Préparation): August, September, October
- **Average population**: 23,333 bees
- **Average volume**: 2.917 liters
- **Average mass**: 2.333 kg
- **Characteristics**: Population reduction, preparation for winter
- **Percentage of max**: 40% volume, 40% mass

### Monthly Volume Variation

```
Month         Volume (L)  Change from previous  % of Annual Avg
January       1.125       Start                 32%
February      1.188       +0.063 (↑6%)         34%
March         1.438       +0.250 (↑21%)        41%
April         3.000       +1.562 (↑109%)       85%
May           7.250       +4.250 (↑142%)       206%
June          7.250       = (stable)            206%
July          6.000       -1.250 (↓17%)        171%
August        3.500       -2.500 (↓42%)        100%
September     2.875       -0.625 (↓18%)        82%
October       2.375       -0.500 (↓17%)        68%
November      2.125       -0.250 (↓11%)        60%
December      1.688       -0.437 (↓21%)        48%
```

### Peak to Trough Ratios

| Metric | Value | Ratio |
|--------|-------|-------|
| **Volume** | 7.250 L (May) vs 1.125 L (Jan) | 6.44x |
| **Mass** | 5.800 kg (May) vs 0.900 kg (Jan) | 6.44x |
| **Population** | 58,000 (May) vs 9,000 (Jan) | 6.44x |

The ratio is identical across all three metrics because they're linearly related.

---

## 🏗️ Space Requirements in Hive Frames

### Hive Frame Dimensions (Standard Langstroth)
- Frame width: 19 cm
- Frame height: 23.5 cm
- Frame area: ~450 cm²
- Typical hive depth: 20 cm
- Volume per frame: ~9,000 cm³ = 9 liters

### Frames Required by Season

| Season | Avg Volume (L) | Frames Needed | % of 10-frame hive |
|--------|--------------|---------------|-------------------|
| Winter | 1.531 | 0.17 | 1.7% |
| Spring | 2.219 | 0.25 | 2.5% |
| Summer | 6.833 | 0.76 | 7.6% |
| Fall | 2.917 | 0.32 | 3.2% |

**Key Insight**: Even at peak season (summer), the bees only occupy ~8% of the physical space in a 10-frame Langstroth hive, yet they utilize that space intensively for brood, pollen, and honey storage.

---

## 💾 Space Occupancy Model

### Considering Colony Organization

In reality, bees don't just occupy their own body volume. They organize into:

1. **Brood area** (eggs, larvae, pupae): ~2-3 frames
2. **Pollen storage**: ~1-2 frames
3. **Honey storage**: ~3-4 frames (varies seasonally)
4. **Worker space** (living area): 1-2 frames

### Effective Space Utilization

| Season | Body Volume | Brood Area | Pollen | Honey | Effective Total |
|--------|-----------|-----------|--------|-------|-----------------|
| Winter | 1.5 L | 2 fr | 1 fr | 3 fr | 6 frames |
| Spring | 2.2 L | 3 fr | 2 fr | 2 fr | 7 frames |
| Summer | 6.8 L | 2 fr | 1 fr | 4 fr | 7 frames |
| Fall | 2.9 L | 2 fr | 2 fr | 3 fr | 7 frames |

**Total hive volume utilized**: 70% on average (7 of 10 frames)

---

## 🌡️ Volume and Temperature Relationship

### Thermal Mass Considerations

The volume of the colony affects its thermal properties:

```
Thermal capacity ≈ Volume × Density × Specific Heat
```

With seasonal volume changes:
- **Winter** (1.5 L): Compact, efficient heat retention
- **Summer** (6.8 L): Larger mass distributes heat, allows better cooling

### Insulation Efficiency

Smaller winter volumes:
- ✓ Require less total heat generation
- ✓ Allow tighter cluster formation
- ✓ Improve heat retention efficiency
- ✗ Reduce thermal mass slightly

This aligns with our optimization model findings (smaller hives are more efficient).

---

## 📋 Environmental Space Requirements

### Space Occupied in Different Hive Types

#### Langstroth Hive (Standard)
- Total volume: 60 liters (10 frames × 6 liters each)
- Summer occupancy: 6.8 L bee body volume + storage = ~43 L effective
- **Efficiency**: 71% utilization

#### Warré Hive (Vertical)
- Total volume: 40 liters
- Summer occupancy: 6.8 L bee body volume + storage = ~32 L effective
- **Efficiency**: 80% utilization

#### Top-bar Hive
- Total volume: 50 liters
- Summer occupancy: 6.8 L bee body volume + storage = ~38 L effective
- **Efficiency**: 76% utilization

---

## 📊 Physical Growth Trajectory

### Growth Rate Analysis

**Winter to Spring Growth** (Jan to Apr):
- Volume increase: 1.125 → 3.000 liters
- Duration: 4 months
- Growth rate: +0.469 liters/month (42% per month average)
- Daily growth: +0.015 liters/day

**Spring to Summer Peak** (Apr to May):
- Volume increase: 3.000 → 7.250 liters
- Duration: 1 month
- Growth rate: +4.250 liters/month (142%)
- Daily growth: +0.141 liters/day

**Summer to Fall Decline** (May to Oct):
- Volume decrease: 7.250 → 2.375 liters
- Duration: 5 months
- Decline rate: -0.975 liters/month (13% per month average)
- Daily decline: -0.032 liters/day

---

## 🔬 Physical Implications for Hive Design

### Volume-Based Design Recommendations

#### Winter Design (Minimum 1.5 L)
- Insulation priority: **CRITICAL**
- Space efficiency: **Maximum** (compact cluster)
- Hive volume needed: 10-15 liters minimum
- Design: Small, highly insulated

#### Summer Design (Maximum 7.3 L)
- Ventilation priority: **CRITICAL**
- Space efficiency: **Adequate** (distributed population)
- Hive volume needed: 40-50 liters minimum
- Design: Larger, well-ventilated

#### Optimal Hive Volume (Considering Annual Variation)
- **Minimum**: 15 liters (for winter cluster)
- **Optimal**: 40-45 liters (allows growth without crowding)
- **Maximum**: 60+ liters (accommodates peak population)

---

## 📈 Data Integration with Optimization Model

### How Volume Variation Affects Energy Requirements

From our optimization model:
- Smaller volumes = Better insulation efficiency (winter)
- Larger volumes = Better heat distribution (summer)
- Seasonal volume change = Natural adaptation to environmental needs

### Bee Heat Production Scaling

```
Q_bee = Population × 0.0004 W/bee

Winter (9,000 bees):    3.6 W
Spring (17,750 bees):   7.1 W
Summer (54,667 bees):  21.9 W
Fall (23,333 bees):     9.3 W
```

With seasonal population changes:
- Heat production scales linearly with colony volume
- Winter challenges: Low heat production + high loss ratio
- Summer challenges: Heat dissipation more critical than heat generation
- Both extremes require design adaptations

---

## 🎯 Key Insights

### 1. **Seasonal Compaction Strategy**
The colony naturally:
- Contracts 94% in winter (maximizes insulation)
- Expands 644% in summer (maximizes brood production)
- **Design implication**: Hive should accommodate both extremes

### 2. **Linear Scaling Relationships**
Volume ∝ Population ∝ Mass ∝ Heat Production
- All scale with the same factor (6.44x)
- Simplifies modeling and predictions

### 3. **Space vs. Function Trade-off**
- **Winter**: Tight clustering (survival priority)
- **Summer**: Distributed population (growth priority)
- **Design challenge**: Single hive for both seasons

### 4. **Energy Efficiency Seasons**
- Winter: Energy per bee = HIGHEST (small population, high losses)
- Summer: Energy per bee = LOWEST (large population, distributed heat)
- **Implication**: Winter design is the critical constraint

### 5. **Physical Growth Patterns**
- Fastest growth: **May** (+142% from April)
- Fastest decline: **Jul-Aug** (-42% over 2 months)
- Most stable: **June** (plateau at maximum)
- Most variable: **Spring-Summer** transition

---

## 📚 Using This Analysis

### For Hive Design
Calculate required hive dimensions:
```
V_hive_min = V_colony_winter + V_storage_winter + margin
V_hive_max = V_colony_summer + V_storage_summer + margin

Suggested V_hive = 40-50 liters (accommodates seasonal variation)
```

### For Space Planning
Understand space utilization:
- Winter: 1.5 L bees + 4.5 L storage = 6 L total
- Summer: 6.8 L bees + 30 L storage = 36.8 L total
- **Design target**: 40-50 liter hives allow both scenarios

### For Population Monitoring
Track colony health:
- If summer volume < 5 liters: Underpopulated (weak colony)
- If summer volume > 8 liters: Overcrowded (need space)
- If volume drops > 50% in fall: Normal (preparation phase)

### For Thermal Modeling
The volume changes affect:
- Heat capacity of colony
- Surface area to volume ratio
- Clustering efficiency
- Energy requirements

---

## 📊 Summary Table

| Metric | Min | Max | Avg | Variation |
|--------|-----|-----|-----|-----------|
| **Population** | 9,000 | 58,000 | 26,750 | 6.44x |
| **Volume (L)** | 1.125 | 7.250 | 3.515 | 6.44x |
| **Mass (kg)** | 0.900 | 5.800 | 2.804 | 6.44x |
| **Frames needed** | 0.12 | 0.81 | 0.39 | 6.75x |

---

## 🔗 Connection to Existing Analysis

This volume analysis enriches the optimization model by:
1. **Adding physical dimension** to population data
2. **Explaining seasonal design needs** (winter compaction, summer expansion)
3. **Validating hive size recommendations** (40-45L optimal)
4. **Supporting thermal modeling** (volume affects heat capacity)
5. **Providing practical implementation guidance** (frames needed by season)

---

## 📝 Formulas Reference

### Volume Calculations
```
V_colony(month) = Population(month) × 0.125 cm³/bee

Example (May):
V_colony = 58,000 × 0.125 = 7,250 cm³ = 7.25 liters
```

### Mass Calculations
```
M_colony(month) = Population(month) × 0.1 g/bee

Example (May):
M_colony = 58,000 × 0.1 = 5,800 g = 5.8 kg
```

### Volume Range
```
V_min = Population × 0.1 cm³/bee    (= 900-5800 cm³)
V_max = Population × 0.15 cm³/bee   (= 1350-8700 cm³)
V_avg = Population × 0.125 cm³/bee  (= 1125-7250 cm³)
```

---

**Analysis Created**: November 13, 2025
**Data Source**: bee_population_year.csv
**Integration**: Connects to HiveOptimizationModel for thermal calculations

🐝 *Understanding the physical dimensions of bee colonies helps design hives that accommodate natural seasonal variations*

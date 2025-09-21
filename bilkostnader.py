# bilkostnader.py

# Antall km kjørt per år 
km_per_år = 10000  

# Forsikring
forsikring_el = 5000
forsikring_bensin = 7500

# Trafikkforsikringsavgift (per dag)
trafikkavgift_per_dag = 8.38
trafikkavgift_år= trafikkavgift_per_dag * 365

# Drivstoffkostnader
# Elbil
kwh_per_km = 0.2
strøm_pris = 2.00  # kr/kWh
drivstoff_kost_el = km_per_år * kwh_per_km * strøm_pris

# Bensinbil
drivstoff_kost_bensin = km_per_år* 1.0  # 1 kr per km

# Bomavgifter
bom_el = km_per_år * 0.1
bom_bensin = km_per_år * 0.3

# Totalkostnader
total_el = forsikring_el + trafikkavgift_år + drivstoff_kost_el + bom_el
total_bensin = forsikring_bensin + trafikkavgift_år + drivstoff_kost_bensin + bom_bensin

# Differanse
differanse = total_bensin - total_el

# Utskrift
print("Årlige kostnader:")
print(f"Elbil: {total_el:,.0f} kr")
print(f"Bensinbil: {total_bensin:,.0f} kr")
print(f"Kostnadsdifferanse (bensin - el): {differanse:,.0f} kr")




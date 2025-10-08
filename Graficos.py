import matplotlib.pyplot as plt
import numpy as np


plt.rcParams['figure.figsize'] = (12, 8)
plt.rcParams['font.size'] = 10


fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(15, 10))
fig.suptitle('Análisis de Datos Personales', fontsize=16, fontweight='bold')

# 1. GRÁFICO DE LÍNEA - Horas dormidas
horas_dormidas = [4,6,8,7,4,5,6,8,4,3,0,6,7,7,8,8,5]
dias = range(1, len(horas_dormidas) + 1)

ax1.plot(dias, horas_dormidas, marker='o', linewidth=2, markersize=6, color='#2E86AB')
ax1.set_title('Horas Dormidas por Día', fontweight='bold')
ax1.set_xlabel('Días')
ax1.set_ylabel('Horas de Sueño')
ax1.grid(True, alpha=0.3)
ax1.set_xticks(dias)

# 2. GRÁFICO DE BARRAS - Tazas de café
tazas_cafe = [2,0,1,0,4,0,0,2,2,2,0,0,0,1,0,2,3]  # Corregí "01" a "0,1"
dias_cafe = range(1, len(tazas_cafe) + 1)

barras = ax2.bar(dias_cafe, tazas_cafe, color='#A23B72', alpha=0.8)
ax2.set_title('Tazas de Café Consumidas por Día', fontweight='bold')
ax2.set_xlabel('Días')
ax2.set_ylabel('Tazas de Café')
ax2.set_xticks(dias_cafe)


for barra in barras:
    height = barra.get_height()
    if height > 0:
        ax2.text(barra.get_x() + barra.get_width()/2., height,
                f'{int(height)}', ha='center', va='bottom')

# 3. GRÁFICO DE PASTEL - Red social más usada
redes_sociales = ['Instagram','TikTok','WhatsApp','TikTok','Facebook','TikTok',
                 'Instagram','Facebook','TikTok','TikTok','TikTok','WhatsApp',
                 'TikTok','TikTok','WhatsApp','Instagram']


from collections import Counter
conteo_redes = Counter(redes_sociales)


redes_ordenadas = dict(sorted(conteo_redes.items(), key=lambda x: x[1], reverse=True))

colores = ['#FF6B6B', '#4ECDC4', '#45B7D1', '#FFE66D', '#95E1D3']
ax3.pie(redes_ordenadas.values(), labels=redes_ordenadas.keys(), autopct='%1.1f%%', 
        colors=colores, startangle=90)
ax3.set_title('Red Social Más Usada', fontweight='bold')

# 4. HISTOGRAMA - Tiempo en llegar a la universidad
tiempo_universidad = [120, 120, 45, 30, 120, 75, 240, 200, 120, 90, 90, 60, 120, 120, 60, 90, 120]

ax4.hist(tiempo_universidad, bins=8, color='#F3A712', alpha=0.8, edgecolor='black')
ax4.set_title('Distribución del Tiempo de Viaje a la Universidad', fontweight='bold')
ax4.set_xlabel('Tiempo (minutos)')
ax4.set_ylabel('Frecuencia')
ax4.grid(True, alpha=0.3)


plt.tight_layout()
plt.subplots_adjust(top=0.93)

# Mostrar los gráficos
plt.show()


print("\n" + "="*50)
print("ESTADÍSTICAS RESUMEN:")
print("="*50)
print(f"Horas dormidas - Promedio: {np.mean(horas_dormidas):.1f} horas")
print(f"Tazas de café - Promedio: {np.mean(tazas_cafe):.1f} tazas/día")
print(f"Red social más popular: {max(conteo_redes, key=conteo_redes.get)}")
print(f"Tiempo universidad - Promedio: {np.mean(tiempo_universidad):.1f} minutos")
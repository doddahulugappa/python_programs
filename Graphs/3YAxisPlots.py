import matplotlib.pyplot as plt

fig, host = plt.subplots(figsize=(8, 5), layout='constrained')  # (width, height) in inches


ax2 = host.twinx()
ax3 = host.twinx()

host.set_xlim(0, 2)
host.set_ylim(0, 2)
ax2.set_ylim(0, 4)
ax3.set_ylim(1, 65)

host.set_xlabel("Distance")
host.set_ylabel("Density")
ax2.set_ylabel("Temperature")
ax3.set_ylabel("Velocity")

color1, color2, color3 = plt.cm.viridis([0, .5, .9])

p1 = host.plot([0, 1, 2], [0, 1, 2], color=color1, label="Density")
p2 = ax2.plot([0, 1, 2], [0, 3, 2], color=color2, label="Temperature")
p3 = ax3.plot([0, 1, 2], [50, 30, 15], color=color3, label="Velocity")

host.legend(handles=p1 + p2 + p3, loc='best')

# right, left, top, bottom
ax3.spines['right'].set_position(('outward', 60))

host.xaxis.set_ticks([])

host.yaxis.label.set_color(p1[0].get_color())
ax2.yaxis.label.set_color(p2[0].get_color())
ax3.yaxis.label.set_color(p3[0].get_color())


plt.savefig("pyplot_multiple_y-axis.pdf", bbox_inches='tight')
plt.show()
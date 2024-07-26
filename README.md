# MKSC (MouseKeyboard Stat Collector)
A little Python program that collects stats of your keyboard and mouse usage.

## Getting started

> [!NOTE]
> Binaries will be published upon project completion.

To launch this program, clone this repo (`git clone https://github.com/moontr3/mksc`) and launch `main.pyw`.

After launch, an icon will appear in your taskbar that indicates that the program is currently working. To close the program, press RMB on the icon and click Exit MKSC.

To view the collected stats, launch `dashboard.py`.

> [!NOTE]
> Right now, you can only launch the dashboard as a standalone app, not within the MKSC collector.
> Also, the dashboard currently doesn't show the heatmap of the pressed keys, though the data is still being collected and stored in `data.mksc`. It's actually just a JSON with scan codes as keys and amount of times the key was pressed as values.
from matplotlib.backends.backend_qt5agg \
    import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg \
    import NavigationToolbar2QT as NavigationToolbar
from PyQt5.QtWidgets import (QDialog, QVBoxLayout, QLineEdit, QHBoxLayout,
                             QLabel, QDialogButtonBox, QPushButton)
from PyQt5.QtCore import pyqtSlot, Qt, QSize

import mne
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg \
    import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg \
    import NavigationToolbar2QT as NavigationToolbar


def clear_layout(layout):
    while layout.count():
        child = layout.takeAt(0)
        if child.widget() is not None:
            child.widget().deleteLater()
        elif child.layout() is not None:
            clearLayout(child.layout())


class EvokedStatesDialog(QDialog):
    def __init__(self, parent, evoked):
        super().__init__(parent)
        self.resize(800, 500)
        self.evoked = evoked.copy().pick_types(eeg=True, meg=True)
        times = self.evoked.times
        n_times = len(times)
        if n_times > 3:
            times = ['{:2.1f}'.format(times[int(n_times / 4)]),
                     ' {:2.1f}'.format(times[int(n_times / 2)]),
                     ' {:2.1f}'.format(times[int(3*n_times / 4)])]
            self.times = QLineEdit()
            self.times.setText(",".join(times))
            self.layout = QVBoxLayout(self)
            hbox = QHBoxLayout(self)
            hbox.addWidget(self.times)
            self.button = QPushButton('Plot')
            self.button.clicked.connect(self.plot)
            hbox.addWidget(self.button)
            self.layout.addLayout(hbox)
            self.to_delete = []
            self.plot()

    def plot(self):
        """Erase and plot the new figures."""
        for layout in self.to_delete:
            clear_layout(layout)
        self.to_delete = []
        times = self.times.text().replace(' ', '').split(',')
        try:
            figs = self.evoked.plot_joint(times=times, show=False)
        except Exception as e:
            figs = plt.figure()
            print(e)

        if type(figs) == list:
            self.resize(800, 200 + len(figs)*300)
            for fig in figs:
                canvas = FigureCanvas(fig)
                toolbar = NavigationToolbar(canvas, self)
                toolbar.setOrientation(Qt.Vertical)
                layout = QHBoxLayout()
                layout.addWidget(toolbar)
                layout.addWidget(canvas)
                self.layout.addLayout(layout)
                self.to_delete.append(layout)
        else:
            canvas = FigureCanvas(figs)
            toolbar = NavigationToolbar(canvas, self)
            layout = QVBoxLayout()
            layout.addWidget(toolbar)
            layout.addWidget(canvas)
            self.layout.addLayout(layout)
            self.to_delete.append(layout)

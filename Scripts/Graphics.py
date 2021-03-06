from Setting_Database import DBSetup
import matplotlib.pyplot as plt


class GraphicPerformance:
    def __new__(cls, *args, **kwargs):
        return object.__new__(cls)

    def __init__(self, parameters) -> None:
        self.PNG_Path = ''
        self.Dict_Parameters: dict = parameters
        self.Time_Seconds: list = [x for x in range(1, 660, 1)]
        self.Text_Annotation: str = "[+] Voltage: 220V\n[+] Phase: 3\n[+] Frequency: 60Hz"
        return

    def graphic_plotting(self):
        # _______________________________________________ [Style] ____________________________________________________
        plt.style.use('seaborn-dark')

        for param in ['figure.facecolor', 'axes.facecolor', 'savefig.facecolor']:
            plt.rcParams[param] = '#363636'  # bluish dark grey

        for param in ['text.color', 'axes.labelcolor', 'xtick.color', 'ytick.color']:
            plt.rcParams[param] = '0.4'  # very light grey

        colors = [
            '#08F7FE',  # teal/cyan
            '#FE53BB',  # pink
            '#F5D300',  # yellow
            '#00ff41',  # matrix green
        ]

        # Annotation:
        text_font = {'family': 'sans-serif',
                     'style': 'normal',
                     'color': 'black',
                     'weight': 'light',
                     'size': 8}

        fig, ax = plt.subplots(2)
        # _____________________________________________ [Graphic 01] _________________________________________________
        for n in range(1, 30):
            ax[0].plot(self.Time_Seconds, self.Dict_Parameters['HP'], color=colors[3],
                       ls='-', lw=1+(0.5*n), alpha=0.001*n)

        ax[0].plot(self.Time_Seconds, self.Dict_Parameters['HP'], color=colors[3], ls='-', label='High Pressure')
        ax[0].set_xlabel('Time [Seconds]')
        ax[0].set_ylabel('Pressure [Psig]')
        ax[0].minorticks_on()
        ax[0].set_title('High Pressure Analyze', color='white')
        ax[0].legend(fontsize=12, loc='center left', bbox_to_anchor=(1, 0.5))
        ax[0].text(550, 190, self.Text_Annotation, fontdict=text_font, bbox=dict(facecolor='lightgray', alpha=0.8))
        ax[0].grid(True)

        # _____________________________________________ [Graphic 02] _________________________________________________
        for n in range(1, 30):
            ax[1].plot(self.Time_Seconds, self.Dict_Parameters['LP'], color=colors[0],
                       ls='-', lw=1+(0.5*n), alpha=0.001*n)

        ax[1].plot(self.Time_Seconds, self.Dict_Parameters['LP'], color=colors[0], ls='-', label='Low Pressure')
        ax[1].set_xlabel('Time [Seconds]')
        ax[1].set_ylabel('Pressure [Psig]')
        ax[1].minorticks_on()
        ax[1].set_title('Low Pressure Analyze', color='white')
        ax[1].legend(fontsize=12, loc='center left', bbox_to_anchor=(1, 0.5))
        ax[1].text(550, 60, self.Text_Annotation, fontdict=text_font, bbox=dict(facecolor='lightgray', alpha=0.8))
        ax[1].grid(True)

        # ________________________________________ [Standard Configuration] ___________________________________________
        fig.set_size_inches(8, 8)
        fig.suptitle('Performance Analyze', color='White', fontsize=18)
        fig.tight_layout()
        plt.show()
        return

    def update(self):
        self.graphic_plotting()
        return


if __name__ == '__main__':
    GraphicPerformance(DBSetup().db_setting()).update()

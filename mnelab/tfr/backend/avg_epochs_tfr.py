import h5py
import numpy as np
import mne

from matplotlib.pyplot import imshow
from numpy import log, mean
from .util import eeg_to_montage


class AvgEpochsTFR:
    """
    This class contains the PSD of a set of Epochs. It stores the data of
    the psds of each epoch. The psds are calculated with the Library mne.
    Attributes:
    ============
    picks       (array[int])   : Contains the picked channels
    tfr         (EpochsTFR)    : Contains the EpochsTFR data computed by mne

    Methods:
    ============
    __init__                   : Computes the EpochsTFR data
    plot_time_freq             : Plot the time-frequency display
    plot_freq_ch               : Plot the frequency-channel display
    plot_time_ch               : Plot the time-channel display
    """
    # ------------------------------------------------------------------------
    def __init__(self, epochs=None, freqs=None, n_cycles=None,
                 method='multitaper', time_bandwidth=4., n_fft=512, width=1,
                 picks=None, type='all'):
        """
        Initialize the class with an instance of EpochsTFR corresponding
        to the method.
        """
        self.cmap = 'jet'

        if epochs is not None:
            if type == 'eeg':
                epochs = epochs.copy().pick_types(meg=False, eeg=True)
            elif type == 'mag':
                epochs = epochs.copy().pick_types(meg='mag')
            elif type == 'grad':
                epochs = epochs.copy().pick_types(meg='grad')
            else:
                epochs = epochs.copy()
            self.info = epochs.info

            if picks is not None:
                self.picks = picks
            else:
                self.picks = list(range(0, len(epochs.info['ch_names'])))
            for bad in epochs.info['bads']:
                try:
                    bad_pick = epochs.info['ch_names'].index(bad)
                    self.picks.remove(bad_pick)
                except Exception as e:
                    print(e)

            montage = eeg_to_montage(epochs)
            if montage is not None:
                # First we create variable head_pos for a correct plotting
                self.pos = montage.get_pos2d()
                scale = 1 / (self.pos.max(axis=0) - self.pos.min(axis=0))
                center = 0.5 * (self.pos.max(axis=0) + self.pos.min(axis=0))
                self.head_pos = {'scale': scale, 'center': center}

                # Handling of possible channels without any known coordinates
                no_coord_channel = False
                try:
                    names = montage.ch_names
                    indices = [names.index(epochs.info['ch_names'][i])
                               for i in self.picks]
                    self.pos = self.pos[indices, :]
                except Exception as e:
                    print(e)
                    no_coord_channel = True

                # If there is not as much positions as the number of Channels
                # we have to eliminate some channels from the data of topomaps
                if no_coord_channel:
                    from mne.channels import read_montage
                    from numpy import array

                    index = 0
                    self.pos = []           # positions
                    # index in the self.data of channels with coordinates
                    self.with_coord = []

                    for i in self.picks:
                        ch_name = epochs.info['ch_names'][i]
                        try:
                            ch_montage = read_montage(
                                montage.kind, ch_names=[ch_name])
                            coord = ch_montage.get_pos2d()
                            self.pos.append(coord[0])
                            self.with_coord.append(index)
                        except Exception as e:
                            print(e)
                        index += 1
                    self.pos = array(self.pos)

                else:
                    self.with_coord = [i for i in range(len(self.picks))]

            else:  # If there is no montage available
                self.head_pos = None
                self.with_coord = []

            if method == 'multitaper':
                from mne.time_frequency import tfr_multitaper
                self.tfr = tfr_multitaper(epochs, freqs, n_cycles,
                                          time_bandwidth=time_bandwidth,
                                          picks=self.picks, return_itc=False)

            if method == 'morlet':
                from mne.time_frequency import tfr_morlet
                self.tfr = tfr_morlet(epochs, freqs, n_cycles,
                                      picks=self.picks, return_itc=False)

            if method == 'stockwell':
                from mne.time_frequency import tfr_stockwell
                # The stockwell function does not handle picks like the two
                # other ones ...
                picked_ch_names = [epochs.info['ch_names'][i]
                                   for i in self.picks]
                picked = epochs.copy().pick_channels(picked_ch_names)
                self.tfr = tfr_stockwell(picked, fmin=freqs[0], fmax=freqs[-1],
                                         n_fft=n_fft, width=width)
        else:
            # Only for initializing an empty class...
            self.tfr = None

    # ------------------------------------------------------------------------
    def init_from_hdf(self, fname):
        """Init from hdf file."""
        channel_types = mne.io.pick.get_channel_types()

        # Start by initializing everything
        f = h5py.File(fname, 'r+')
        dic = f['mnepython']['idx_0']['idx_1']
        data = dic['key_data'][()]
        freqs = dic['key_freqs'][()]
        times = dic['key_times'][()]
        method = ''.join([chr(x) for x in dic['key_method'][()]])
        chs = dic['key_info']['key_chs']
        names = []
        locs = []
        ch_types = []
        for key in chs.keys():
            ch = chs[key]
            ch_val = ch['key_kind'][()][0]
            for t, rules in channel_types.items():
                for key, vals in rules.items():
                    try:
                        if ch['key_' + key] not in np.array(vals):
                            break
                    except Exception:
                        break
                else:
                    ch_types.append(t)
            name = ''.join([chr(x) for x in ch['key_ch_name']])
            loc = ch['key_loc'][()][0:3]
            names.append(name)
            locs.append(loc)
        locs = np.array(locs)
        self.picks = [i for i in range(len(names))]
        montage = mne.channels.Montage(locs, names, 'custom',
                                       [i for i in range(len(locs))])
        # First we create variable head_pos for a correct plotting
        self.pos = montage.get_pos2d()
        scale = 1 / (self.pos.max(axis=0) - self.pos.min(axis=0))
        center = 0.5 * (self.pos.max(axis=0) + self.pos.min(axis=0))
        self.head_pos = {'scale': scale, 'center': center}

        # Handling of possible channels without any known coordinates
        no_coord_channel = False
        try:
            names = montage.ch_names
            indices = self.picks
            self.pos = self.pos[indices, :]
        except Exception as e:
            print(e)
            no_coord_channel = True

        # If there is not as much positions as the number of Channels
        # we have to eliminate some channels from the data of topomaps
        if no_coord_channel:
            from mne.channels import read_montage
            from numpy import array

            index = 0
            self.pos = []           # positions
            # index in the self.data of channels with coordinates
            self.with_coord = []

            for i in self.picks:
                ch_name = epochs.info['ch_names'][i]
                try:
                    ch_montage = read_montage(
                        montage.kind, ch_names=[ch_name])
                    coord = ch_montage.get_pos2d()
                    self.pos.append(coord[0])
                    self.with_coord.append(index)
                except Exception as e:
                    print(e)
                index += 1
            self.pos = array(self.pos)

        else:
            self.with_coord = [i for i in range(len(self.picks))]

        self.info = mne.create_info(names, 1, montage=montage,
                                    ch_types='eeg')
        # eeg is just a trick to not raise valueError...
        self.tfr = mne.time_frequency.AverageTFR(
            self.info, data, times, freqs, len(self.picks))
        return self

    # ------------------------------------------------------------------------
    def plot_time_freq(self, index_channel, ax,
                       vmin=None, vmax=None, log_display=False):
        """
        Plot the averaged epochs time-frequency plot for a given channel.
        """
        data = self.tfr.data[index_channel, :, :]
        if log_display:
            data = 10 * log(data / mean(data))
        extent = [self.tfr.times[0], self.tfr.times[-1],
                  self.tfr.freqs[0], self.tfr.freqs[-1]]
        return ax.imshow(data, extent=extent, aspect='auto',
                         origin='lower', vmax=vmax, vmin=vmin, cmap=self.cmap)

    # ------------------------------------------------------------------------
    def plot_freq_ch(self, time_index, ax,
                     vmin=None, vmax=None, log_display=False):
        """Plot the averaged epochs frequency-channel plot for a given time."""
        data = self.tfr.data[:, :, time_index]
        if log_display:
            data = 10 * log(data / mean(data))
        extent = [self.tfr.freqs[0], self.tfr.freqs[-1],
                  .5, len(self.picks)+.5]
        return ax.imshow(data, extent=extent, aspect='auto',
                         origin='lower', vmax=vmax, vmin=vmin, cmap=self.cmap)

    # ------------------------------------------------------------------------
    def plot_time_ch(self, freq_index, ax,
                     vmin=None, vmax=None, log_display=False):
        """
        Plot the averaged epochs time-channel plot for a given frequency
        range.
        """
        data = self.tfr.data[:, freq_index, :]
        if log_display:
            data = 10 * log(data / mean(data))
        extent = [self.tfr.times[0], self.tfr.times[-1],
                  .5,                len(self.picks)+.5]
        return ax.imshow(data, extent=extent, aspect='auto',
                         origin='lower', vmax=vmax, vmin=vmin, cmap=self.cmap)

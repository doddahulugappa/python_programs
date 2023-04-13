import glob
import os
import re
import time
import pandas as pd
import PySimpleGUI as psg
from tkinter import messagebox
import logging

logging.basicConfig(filename='Report.log',
                    filemode='w',
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.DEBUG)


class ReadComparePrepare:

    def __init__(self):
        """
        default constructor
        """
        self.count_col = None

    @staticmethod
    def get_files(filepath):
        """
        Gets all csv files
        :param filepath:
        :return: all csv files
        """
        return glob.glob(filepath + "\\*.csv")

    @staticmethod
    def read_csv(file_name, skip_rows=0):
        """
        Loads csv data to pandas dataframe
        :param file_name:
        :param skip_rows:
        :return: dataframe
        """
        dataframe = pd.read_csv(file_name, skiprows=skip_rows)
        return dataframe

    def count_columns(self, combined_df):
        """
        Counts the number of columns in dataframe
        :param combined_df:
        :return: column count
        """
        self.count_col = len(combined_df.columns) - 5  # deduct first 5 columns
        return self.count_col

    def bath_process(self, combined_df):
        """
        Prepares bath data
        :param combined_df:
        :return: bath data
        """
        logging.info("\n=============Bath Data==============\n")
        timer = [i * 5 for i in range(self.count_col)]
        min_mass_fraction = [min(combined_df.iloc[:, i + 5]) for i in range(self.count_col)]
        max_mass_fraction = [max(combined_df.iloc[:, i + 5]) for i in range(self.count_col)]
        std_mass_fraction = [(combined_df.iloc[:, i + 5]).std() for i in range(self.count_col)]
        vol_avg_mass_fraction = [sum(combined_df.iloc[:, 4] * combined_df.iloc[:, i + 5]) / sum(combined_df.iloc[:, 4])
                                 for i in range(self.count_col)]

        bath_data = pd.DataFrame({"time": timer,
                                  "vol_avg_mass_fraction": vol_avg_mass_fraction,
                                  "min_mass_fraction": min_mass_fraction,
                                  "max_mass_fraction": max_mass_fraction,
                                  "std_mass_fraction": std_mass_fraction
                                  }
                                 )
        return bath_data

    def anode_process(self, combined_df, an_geometry):
        """
        Prepares anode data
        :param combined_df:
        :param an_geometry:
        :return: anode data
        """
        logging.info("\n============Anode Data==============\n")
        anode_dfs = []
        for rec in an_geometry.iterrows():
            try:
                x_min = rec[1][2] / 1000
                x_max = rec[1][3] / 1000
                y_min = rec[1][4] / 1000
                y_max = rec[1][5] / 1000

                combined_df.columns = [c.replace(' ', '') for c in combined_df.columns]
                filtered_df = combined_df[(combined_df['X[m]'] >= x_min) & (combined_df['X[m]'] <= x_max)]
                filtered_df = filtered_df[(filtered_df['Y[m]'] >= y_min) & (filtered_df['Y[m]'] <= y_max)]

                timer = [i * 5 for i in range(self.count_col)]
                min_mass_fraction = [min(filtered_df.iloc[:, i + 5]) for i in range(self.count_col)]
                max_mass_fraction = [max(filtered_df.iloc[:, i + 5]) for i in range(self.count_col)]
                std_mass_fraction = [(filtered_df.iloc[:, i + 5]).std() for i in range(self.count_col)]
                vol_avg_mass_fraction = [sum(filtered_df.iloc[:, 4] * filtered_df.iloc[:, i + 5]) /
                                         sum(filtered_df.iloc[:, 4]) for i in range(self.count_col)]

                anode_rec = pd.DataFrame({"time": timer,
                                          "anode_no": rec[1][0],
                                          "side": rec[1][1],
                                          "vol_avg_mass_fraction": vol_avg_mass_fraction,
                                          "min_mass_fraction": min_mass_fraction,
                                          "max_mass_fraction": max_mass_fraction,
                                          "std_mass_fraction": std_mass_fraction
                                          }
                                         )
                anode_dfs.append(anode_rec)
            except Exception as e:
                logging.error('Empty Set ' + str(rec[1][0]) + '\t' + str(rec[1][1]) + '\t' + str(e))
        anode_data = pd.concat(anode_dfs, axis=0)  # Merge all dataframe
        return anode_data

    def section_process(self, combined_df, sec_geometry):
        """
        Prepares section data
        :param combined_df:
        :param sec_geometry:
        :return: section data
        """
        logging.info("\n============Section Data============\n")
        section_dfs = []
        for rec in sec_geometry.iterrows():
            try:
                x_min = rec[1][3] / 1000
                x_max = rec[1][4] / 1000
                y_min = rec[1][5] / 1000
                y_max = rec[1][6] / 1000
                combined_df.columns = [c.replace(' ', '') for c in combined_df.columns]
                filtered_df = combined_df[(combined_df['X[m]'] >= x_min) & (combined_df['X[m]'] <= x_max)]
                filtered_df = filtered_df[(filtered_df['Y[m]'] >= y_min) & (filtered_df['Y[m]'] <= y_max)]
                timer = [i * 5 for i in range(self.count_col)]
                min_mass_fraction = [min(filtered_df.iloc[:, i + 5]) for i in range(self.count_col)]
                max_mass_fraction = [max(filtered_df.iloc[:, i + 5]) for i in range(self.count_col)]
                std_mass_fraction = [(filtered_df.iloc[:, i + 5]).std() for i in range(self.count_col)]
                vol_avg_mass_fraction = [sum(filtered_df.iloc[:, 4] * filtered_df.iloc[:, i + 5]) /
                                         sum(filtered_df.iloc[:, 4]) for i in range(self.count_col)]

                section_rec = pd.DataFrame({"time": timer,
                                            "anode_no": rec[1][0],
                                            "side": rec[1][1],
                                            "section": rec[1][2],
                                            "vol_avg_mass_fraction": vol_avg_mass_fraction,
                                            "min_mass_fraction": min_mass_fraction,
                                            "max_mass_fraction": max_mass_fraction,
                                            "std_mass_fraction": std_mass_fraction
                                            }
                                           )
                section_dfs.append(section_rec)
            except Exception as e:
                logging.error('Empty Set ' + str(rec[1][0]) + '\t' + str(rec[1][1]) + '\t' + str(e))

        section_data = pd.concat(section_dfs, axis=0)  # Merge all dataframe
        return section_data


if __name__ == "__main__":

    obj = ReadComparePrepare()  # Create obj

    layout = [
        [psg.ProgressBar(100, orientation='h', expand_x=True, size=(20, 20), key='-PBAR-',
                         bar_color=("Green", "White"))],
        [psg.Text('', key='-OUT-', enable_events=True, font=('Arial Bold', 15), justification='center', expand_x=True,
                  background_color="Gray")]
    ]
    window = psg.Window('Report Generator', layout, size=(500, 70), background_color="Gray")
    if window.finalize():

        # Record start time
        start = time.time()
        try:
            folder = "Output"
            if not os.path.exists(folder):
                os.mkdir(folder)  # creates output directory

            folder_path = ".\Data"

            # Get All Mass Fraction Input files
            mf_files = obj.get_files(folder_path)
            geometry_file = None
            for file in mf_files:
                if re.search("Geometry", file, re.IGNORECASE):
                    mf_files.remove(file)
                    geometry_file = file
                    break

            window['-PBAR-'].update(current_count=10)
            window['-OUT-'].update("10%")

            files = []
            for file in mf_files:
                path, filename = os.path.split(file)
                num_match = re.compile(".*t(\d+).*")
                match_obj = num_match.search(filename)
                if match_obj:
                    files.append(match_obj.groups()[0])
            files = sorted(map(int, files))

            if geometry_file is not None:
                master_df = obj.read_csv(geometry_file, skip_rows=5)
                for file in files:
                    full_path = os.path.join(folder_path, "MF_data_t" + str(file) + ".csv")
                    df = obj.read_csv(full_path, skip_rows=5)
                    df.columns = ["Node Number", str(file)]
                    master_df = pd.concat([master_df, df[str(file)]], axis=1)

                window['-PBAR-'].update(current_count=15)
                window['-OUT-'].update("15%")

                # Write combined data to csv
                file_path = os.path.join(folder, "CombinedMFData.csv")
                master_df.to_csv(file_path, index=False)

                window['-PBAR-'].update(current_count=35)
                window['-OUT-'].update("35%")

                # Get the count of columns
                obj.count_columns(master_df)

                # Prepare bath data
                bath_df = obj.bath_process(master_df)
                file_path = os.path.join(folder, "BathData.csv")
                bath_df.to_csv(file_path, index=False)

                window['-PBAR-'].update(current_count=65)
                window['-OUT-'].update("65%")

                # Prepare Anode data
                file_path = "Anodes_geometry.csv"
                anode_geometry = pd.read_csv(file_path)
                anode_df = obj.anode_process(master_df, anode_geometry)
                file_path = os.path.join(folder, "AnodeData.csv")
                anode_df.to_csv(file_path, index=False)

                window['-PBAR-'].update(current_count=80)
                window['-OUT-'].update("80%")

                # Prepare Section data
                file_path = "Sections_geometry.csv"
                section_geometry = pd.read_csv(file_path)
                section_df = obj.section_process(master_df, section_geometry)
                file_path = os.path.join(folder, "SectionData.csv")
                section_df.to_csv(file_path, index=False)

                window['-PBAR-'].update(current_count=99)
                window['-OUT-'].update("99%")
            else:
                messagebox.showerror(title="Error!", message="Geometry file didn't find")
                logging.warning('Geometry file not found')
        except Exception as e:
            logging.error('Something went wrong ' + str(e))
            messagebox.showerror(title="Error!", message="Something is wrong\n" + str(e))

        # Record end time
        end = time.time()

        window['-PBAR-'].update(current_count=100)
        window['-OUT-'].update("100%")
        print(f"Total time taken in seconds:{end - start:.2f}")
        logging.info(f"Total time taken in seconds:{end - start:.2f}")
        window.close()
